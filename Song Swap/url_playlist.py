import webbrowser

from flask import Flask, render_template, session, url_for, redirect, request, flash
import Algorithm
import sqlite3
import Insert
import Comparison
import playlists_grab
import Main

app = Flask(__name__, template_folder='html/Templates/')
app.secret_key = 'your_secret_key'
DATABASE = 'songSwap.db'





def songs_received_page():
    '''Displays the feed page with matched users and sent songs. And the ability to send songs'''
    username = session.get('username')
    if username:
        # Connect to the database
        conn, cursor = connect_to_database(DATABASE)
        # get the user ID based on the username
        cursor.execute("""SELECT id FROM User WHERE username = ?""", (username,))
        user_id = cursor.fetchone()
        user_id_value = user_id[0]
        print(user_id_value)
        # get the spotipy id for a spotify playlist using user id
        cursor.execute("""SELECT spotipy_id FROM Spotify_Playlist WHERE User = ?""", (user_id_value,))
        playlist_id = cursor.fetchone()[0]
        print(playlist_id)
        # get the title and artist for a song
        cursor.execute("""SELECT Title, Artist FROM Song WHERE Playlist_ID = ?""", (playlist_id,))
        songs_and_artists = cursor.fetchall()
        print(songs_and_artists)
        # extract all the songs and artists to a list respectively then zip them together
        songs = []
        artists = []
        for song_and_artist in songs_and_artists:
            song_title = song_and_artist[0]
            song_artist = song_and_artist[1]
            songs.append(song_title)
            artists.append(song_artist)
        song_display = list(zip(songs, artists))

        cursor.execute("""SELECT id FROM User WHERE username = ?""", (session.get('username'),))
        user1id = cursor.fetchone()
        # get all the users current user (user1id) has matched with
        cursor.execute(
            """SELECT CASE WHEN user1_id = ? THEN user2_id ELSE user1_id END AS matched_user_id FROM Matches WHERE user1_id = ? OR user2_id = ?""",
            (user1id[0], user1id[0], user1id[0]))
        matched_user_ids = cursor.fetchall()
        # put all the usernames of the matched users into a list
        matched_users = []
        for id in matched_user_ids:
            cursor.execute("""SELECT username FROM User WHERE id = ?""", (id[0],))
            username = cursor.fetchone()
            matched_users.append(username[0])

        # get the data for any songs that have been sent to the current user
        cursor.execute("""SELECT User.username, SongsSent.song_id 
                                         FROM SongsSent 
                                         JOIN User ON SongsSent.sender_id = User.id
                                         WHERE SongsSent.receiver_id = ?""", (user1id[0],))
        sent_songs_data = cursor.fetchall()
        # get the usernames of users who have sent current user a song
        sender_usernames = [row[0] for row in sent_songs_data]
        # get all the titles of the songs that have been sent to user
        song_titles = []
        for row in sent_songs_data:
            cursor.execute("""SELECT Title FROM Song WHERE Spotipy_ID = ?""", (row[1],))
            title = cursor.fetchone()
            if title:
                song_titles.append(title[0])
            else:
                song_titles.append("Unknown")

        sent_songs = list(zip(sender_usernames, song_titles))

        # close the database connection
        conn.close()

        # Render the feed page
        if len(sent_songs) == 0:
            conn.close()
            return render_template('feed.html', results=matched_users, songs=song_display, sent_songs=None)
        else:
            conn.close()
            return render_template('feed.html', results=matched_users, songs=song_display, sent_songs=sent_songs)
    else:
        # If the user is not logged in, redirect them to the login page
        return render_template('login.html')

def returnSongID(songName):
    conn, cursor = connect_to_database(DATABASE)
    cursor.execute("""SELECT Spotipy_ID FROM Song WHERE Title = ?""", (songName,))
    songID = cursor.fetchone()[0]
    session['current_song_ID'] = songID
    conn.close()


@app.route('/playlist_selector', methods=['GET', 'POST'])
def playlist_selector():
    '''Displays a page that allows the user to select a playlist from their spotify account.'''
    matched_users = []
    # Get the playlist data submitted by the user
    playlist = session.get('playlist')

    user_playlists = session.get('user_playlists', {})

    playlist_id = user_playlists[playlist]
    usergenres, usermood = Algorithm.playlist_extraction(playlist_id)
    registration_data = session.get('registration_data')
    if registration_data:
        username = registration_data['username']
        session['username'] = username
        email = registration_data['email']
        password = registration_data['password']
        spotify_username = registration_data['spotify_username']
        Insert.insert_user(username, email, password, spotify_username, usergenres, usermood)
        session.pop('registration_data', None)
    conn, cursor = connect_to_database(DATABASE)
    cursor.execute("""SELECT id FROM User WHERE username = ?""", (session.get('username'),))
    user_id = cursor.fetchone()[0]
    print("User ID:", user_id)# Fetch the user_id value from the tuple
    Insert.insert_playlist(playlist, playlist_id, user_id)
    cursor.execute("""SELECT spotipy_id FROM Spotify_Playlist WHERE User = ? AND spotipy_id = ?""", (user_id, playlist_id,))
    database_playlist_id = cursor.fetchone()

    cursor.execute("""SELECT id FROM Spotify_Playlist WHERE User = ? AND spotipy_id = ?""",
                   (user_id, playlist_id,))
    playlistIDFromDB = cursor.fetchone()
    session['playlist_id'] = playlistIDFromDB
    if database_playlist_id:
        song_info = Main.get_songs(database_playlist_id[0])
        songs = playlists_grab.song_objects(song_info)
        for song in songs:

            song_id = song.get_id()
            song_name = song.get_name()
            song_artist = song.get_artist()
            song_url = song.get_url()
            Insert.insert_song(song_name, song_artist, database_playlist_id[0], song_id, song_url)
            # get matches
            matched_users = Comparison.main(session.get('username'))
            # insert matches into the database
        if matched_users:
            for user in matched_users:
                cursor.execute("""SELECT id FROM User WHERE username = ?""", (user,))
                user2id = cursor.fetchone()
                Insert.insert_matches(user_id, user2id[0])

            #move matching stuff here

    conn.close()

@app.route('/submit_song', methods=['POST'])
def submit_song():
    """Handles the submission of songs by users. Used for sending to other users"""
    if request.method == 'POST':
        selected_song = session.get('selected_song')
        matched_user = session.get('selected_user')
        username = session.get('username')
        conn, cursor = connect_to_database(DATABASE)
        cursor.execute("""SELECT id FROM User where username = ?""", (username,))
        sender_id = cursor.fetchone()[0]  # Get the first element of the tuple
        cursor.execute("""SELECT id FROM User where username = ?""", (matched_user,))
        receiver_id = cursor.fetchone()[0]  # Get the first element of the tuple
        cursor.execute(
            """SELECT match_id FROM Matches WHERE (user1_id = ? AND user2_id = ?) OR (user1_id = ? AND user2_id = ?)""",
            (sender_id, receiver_id, receiver_id, sender_id))
        match_id = cursor.fetchone()[0]
        cursor.execute("""SELECT Spotipy_ID FROM Song WHERE Title = ?""", (selected_song,))
        song_id = cursor.fetchone()[0]
        # Insert a record into the SongsSent table'
        conn.close()
        Insert.insert_songs_sent(match_id, sender_id, receiver_id, song_id)
        return redirect(url_for('feed'))  # Redirect the user back to the feed page after processing



def check_credentials(username, password):
    """Check user credentials"""
    conn, cursor = connect_to_database(DATABASE)
    cursor.execute("""SELECT * FROM User WHERE username = ?""", (username,))
    user = cursor.fetchone()
    conn.close()
    if user is not None:
        if user[3] == password:
            return True
    else:
        return False




@app.route('/register', methods=['GET', 'POST'])
def register():
    """Allows the user to register a new account"""
    username = session.get('username')
    email = session.get('email')
    password = session.get('password')
    spotify_username = session.get('spotify_username')
    # check if username already exists
    conn, cursor = connect_to_database(DATABASE)
    cursor.execute("""SELECT * FROM User WHERE username = ?""", (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        print("Username already exists. Please choose a different one")
        error = 'Username already exists. Please choose a different one.'
        conn.close()
        return render_template('register.html', error=error)

    conn.close()
    # store registration data into session so it can be accessed and stored into the database after selecting a playlist
    session['registration_data'] = {
        'username': username,
        'email': email,
        'password': password,
        'spotify_username': spotify_username
    }
    # take to playlist selection page
    return render_template('first_playlist_selector.html', playlists=session.get('playlists'))


def get_url_from_id(song_id):
    conn, cursor = connect_to_database(DATABASE)
    cursor.execute("""SELECT * FROM Song WHERE Spotipy_ID = ?""", (song_id,))
    song_id = cursor.fetchone()[0]
    conn.close()
    return song_id
    
    
def connect_to_database(database_name):
    '''connects to the sqlite database and returns the connection object and cursor object'''
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print("Error connecting to the database:", e)
        None, None


if __name__ == '__main__':
    app.run(debug=True)

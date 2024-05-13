import sqlite3
import webbrowser

from flask import Flask, render_template, jsonify, request, \
    session, url_for, redirect, flash  # Jsonify is used to communicate with HTML functions
import os

import Algorithm
import Comparison
import Insert
import Playlist
import PopUpScreen
import url_playlist
import Song
import playlists_grab
import CSC450
import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

# Registration -> Authorization -> playlist selector

DATABASE = 'songSwap.db'
app = Flask(__name__, template_folder='html/Templates/', static_folder="html/Templates/styles")
app.config['SECRET_KEY'] = os.urandom(64)

client_id = "de8dfa5743864623807a250061e269e0"
client_secret = "5f3ce43f0e0b4ae6b9f7f4f33de920cd"
redirect_uri = "http://localhost:5000/callback"

cache_handler = FlaskSessionCacheHandler(session)
sp_oath = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    cache_handler=cache_handler,
    show_dialog=True,
    scope='playlist-modify-public playlist-modify-private'
)
sp = Spotify(auth_manager=sp_oath)

username = None
password = None
spotify_username = None
email = None
new_user = False
currentUsername = None


@app.route("/")  # Login page
def loginScreen():
    global new_user
    new_user = False
    session['logging_in'] = False
    return render_template('login.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle user login"""
    if request.method == 'POST':
        username = request.form['username']
        global currentUsername
        currentUsername = username
        password = request.form['password']
        if url_playlist.check_credentials(username, password):
            session['username'] = username
            session['logging_in'] = True
            return redirect('/callback')
        else:
            flash('Username and/or password is wrong, please retry', 'error')
            return render_template('login.html', success=False)
    else:
        return render_template('login.html')


@app.route("/playlist_selector")
def playlistSelector():
    playlists = get_playlists()
    session['playlists'] = playlists
    return render_template("playlist_selector.html", playlists=session.get('playlists'))


@app.route('/play_song', methods=['POST', 'GET'])
def play_song():
    """
    Starts the song player
    :return: a success string indicating that the song is playing
    """
    ID = session.get('current_song_ID')
    song_url = url_playlist.get_url_from_id(ID)
    webbrowser.open(song_url)
    return 'played'


@app.route('/pause_song', methods=['POST', 'GET'])
def pause():
    current = sp.current_playback()
    if current is not None:
        device = sp.devices()['devices'][0]['id']
        sp.pause_playback(device_id=device)
    return 'paused'


@app.route('/first_playlist_selector_post', methods=['POST', 'GET'])
def first_playlist_selector_post():
    print('got here')
    session['playlist'] = request.form['playlist']
    url_playlist.playlist_selector()
    return redirect('/home')


def get_selected_playlist_songs():
    # If playlist already in DB, change the current playlist id to that
    # Otherwise, add songs
    '''Displays a page that allows the user to select a playlist from their spotify account.'''
    # Get the playlist data submitted by the user
    current_playlist = session.get('playlist')
    conn, cursor = url_playlist.connect_to_database(DATABASE)
    cursor.execute("""SELECT id FROM User WHERE username = ?""", (session.get('username'),))
    user_id = cursor.fetchone()[0]


    # Make sure the playlist doesn't already exist
    cursor.execute("""SELECT id FROM Spotify_Playlist WHERE name = ? AND User = ?""", (current_playlist, user_id))
    playlistInDB = cursor.fetchone()
    if playlistInDB is not None:
        playlist_id = playlistInDB[0]
        cursor.execute("""SELECT id FROM Spotify_Playlist WHERE User = ? AND id = ?""",
        (user_id, playlist_id,))
        database_playlist_id = cursor.fetchone()
        session['playlist_id'] = database_playlist_id
    else:
        conn.close()
        first_playlist_selector_post()
    conn.close()


@app.route("/playlist_selector_post", methods=['POST', 'GET'])
def playlistSelector_post():
    session['playlist'] = request.form['playlist']
    get_selected_playlist_songs()
    return redirect('/home')


@app.route("/register", methods=['GET', 'POST'])
def registerScreen():
    if request.method == "POST":
        session['username'] = request.form['username']
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        session['spotify_username'] = request.form['spotify_username']
        session['registration_data'] = {'username': session.get('username'), 'email': session.get('email'),
                                        'password': session.get('password'),
                                        'spotify_username': session.get('spotify_username')}
        url_playlist.register()
        login()
        return redirect("/select_first_playlist")


@app.route("/authorization")
def authorizationScreen():
    isLoggingIn = session.get('is_logging_in')
    if not isLoggingIn:
        global new_user
        new_user = True
    auth_url = sp_oath.get_authorize_url()
    return redirect(auth_url)


@app.route("/select_first_playlist")
def select_first_playlist():
    playlists = get_playlists()
    session['playlists'] = playlists
    registerScreen = url_playlist.register()
    return registerScreen


@app.route('/callback')
def callbackScreen():
    code = request.args.get('code', '')
    token_info = sp_oath.get_access_token(code)
    session['access_token'] = token_info['access_token']
    if new_user:
        session['playlists'] = get_playlists()
        return render_template("register.html")
    else:
        session['username'] = currentUsername
        return redirect('/home')


@app.route('/home', methods=['post', 'get'])
def index():
    """
    Purpose: Renders the basic HTML main page
    Return: The index page
    """
    if request.method == "POST":
        session['playlist'] = request.form['playlist']
        url_playlist.playlist_selector()
    return render_template('index.html')


@app.route('/logout')
def logout():
    """Allows the user to logout, popping their username from the session"""
    # Clear the user from the session
    session.pop('username', None)
    if session.get('playlist') is not None:
        session.pop('playlist', None)
    if session.get('current_playlist') is not None:
        session.pop('current_playlist', None)
    if session.get('password') is not None:
        session.pop('password', None)
    if session.get('selected_user') is not None:
        session.pop('selected_user', None)
    if session.get('registration_data') is not None:
        session.pop('registration_data', None)
    global new_user
    new_user = False
    return redirect('/')


@app.route('/submit_song', methods=['POST'])
def submitSong():
    session['selected_song'] = request.form['selected_song']
    session['selected_user'] = request.form['selected_user']
    url_playlist.submit_song()
    return redirect('/send_song_screen')


@app.route('/listen_song', methods=['POST', 'GET'])
def listen_song():
    currentSongName = request.args.get('selected_song')
    url_playlist.returnSongID(currentSongName)
    session["current_song_name"] = currentSongName
    session["voted"] = False
    nextScreen = popup_submit()
    return nextScreen


@app.route('/upvote', methods=['POST'])
def upvote():
    upvoteInfo = PopUpScreen.upvote()
    return upvoteInfo


@app.route('/send_song_screen', methods=['POST', 'GET'])
def send_song():
    '''Displays the feed page with matched users and sent songs. And the ability to send songs'''
    username = session.get('username')
    if username:
        # Connect to the database
        conn, cursor = url_playlist.connect_to_database(DATABASE)
        # get the user ID based on the username
        cursor.execute("""SELECT id FROM User WHERE username = ?""", (username,))
        user_id = cursor.fetchone()
        if user_id is None:
            # Handle case where user ID is not found
            conn.close()
            return render_template('error.html', message="User ID not found.")

        user_id_value = user_id[0]
        # get the spotipy id for a spotify playlist using user id
        if session.get('playlist_id') is not None:
            playlist_id = session.get('playlist_id')
            if type(playlist_id) is tuple:
                playlist_id = playlist_id[0]
            cursor.execute("""SELECT spotipy_id FROM Spotify_Playlist WHERE id = ? AND User = ?""", (playlist_id, user_id_value))
            playlist_id = cursor.fetchone()
            if playlist_id is not None:
                playlist_id = playlist_id[0]
        else:
            cursor.execute("""SELECT spotipy_id FROM Spotify_Playlist WHERE User = ?""", (user_id_value,))
            playlist_id = cursor.fetchone()
            if playlist_id is None:
                conn.close()
                return redirect("/playlist_selector")
            else:
                playlist_id = playlist_id[0]

        # get the title and artist for a song
        cursor.execute("""SELECT DISTINCT Title, Artist FROM Song WHERE Playlist_ID = ?""", (playlist_id,))
        songs_and_artists = cursor.fetchall()
        # extract all the songs and artists to a list respectively then zip them together
        songs = []
        artists = []
        for song_and_artist in songs_and_artists:
            if len(song_and_artist) >= 2:
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

        # close the database connection
        conn.close()

        # Render the feed page
        return render_template('send_song.html', results=matched_users, songs=song_display)
    else:
        # If the user is not logged in, redirect them to the login page
        return render_template('login.html')


@app.route('/downvote', methods=['POST'])  # This function triggers once the thumbs down image is clicked
def downvote():
    downvoteInfo = PopUpScreen.downvote()
    return downvoteInfo


@app.route('/popup', methods=['post', 'get'])
def playlist():
    playlists = PopUpScreen.playlist()
    return playlists


@app.route('/feed', methods=['POST', 'GET'])
def feed():
    feedPage = url_playlist.songs_received_page()
    return feedPage


def get_playlists():
    '''
        Retrieves a list of playlist names belonging to the current user.

        Returns:
            list: A list of playlist names.
        '''
    if 'access_token' in session:
        with app.app_context():
            playlists = sp.current_user_playlists()

        playlist_list = []
        playlist_dict = {}
        for playlist in playlists['items']:
            playlist_name = playlist['name']
            playlist_id = playlist['id']
            playlist_list.append(playlist_name)
            playlist_dict[playlist_name] = playlist_id
        session['user_playlists'] = playlist_dict
        return playlist_list
    else:
        return []


def get_songs(playlist_id):
    '''
        Retrieves the songs in a playlist given its ID.

        :param playlist_id (str): The ID of the playlist.

        :return: list: A list of dictionaries, each containing information about a song.
        '''
    results = sp.playlist_items(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


def popup_submit():
    """
    Purpose: Renders the basic HTML popup page
    Return: The popup form
    """
    song = 'spotify' + ':track:' + session.get('current_song_ID')
    art = sp.track(song)['album']['images'][0]['url']
    playlist_name = get_playlists()
    try:
        selected_playlist = request.form['playlist']
        session['selected_playlist'] = selected_playlist
        status = add_song(selected_playlist, song)
        if status:
            print("---------------" * 4, "successfully added", "---------------" * 4)
            return render_template('popup_window.html', playlists=playlist_name,
                                   results="Added successfully", images=art, songname=session.get('current_song_name'))
    except:
        return render_template('popup_window.html', playlists=playlist_name,
                               results="Add this song!", images=art, songname=session.get('current_song_name'))


def add_song(play_name, song):
    """
    Adds a song to a specific playlist
    :param play_name: The specified playlist
    :param artist: Arist of the song being added
    :param song: Song being added
    :return: True if the song was successfully added
    """
    if 'access_token' in session:
        user_id = sp.current_user()['id']
        playlists = sp.user_playlists(user_id)
        for playlist in playlists['items']:
            if playlist['name'] == play_name:
                playlist_id = playlist['id']
                sp.playlist_add_items(playlist_id=playlist_id, items=[song])
    return True


if __name__ == '__main__':
    app.run(debug=True)

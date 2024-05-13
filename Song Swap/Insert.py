import sqlite3
import json

def connect_to_database():
    '''Connects to the SQLite database.'''
    return sqlite3.connect('songSwap.db')

# Function to insert a new user into the User table
def insert_user(username, email, password, spotify, genres, mood_values):
    '''Inserts a new user into the User table.'''
    # Connect to the database
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        # gotta convert the genres and mood values to JSON strings GOTTA
        genres_json = json.dumps(genres)
        mood_json = json.dumps(mood_values)

        #add a query to add new user to database
        cursor.execute("INSERT INTO User (username, email, password, spotify, genres, mood_values) VALUES (?, ?, ?, ?, ?, ?)",
                       (username, email, password, spotify, genres_json, mood_json))

        conn.commit()
        print("user added to database")
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()

def insert_playlist(playlist_name, spotipy_id, user):
    '''Inserts a new playlist into the Spotify_Playlist table.'''
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO Spotify_Playlist (name, spotipy_id, User) VALUES (?, ?, ?)", (playlist_name, spotipy_id, user))
        conn.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()

def insert_song(title, artist, playlist_id, spotipy_id, url):
    '''Inserts a new song into the Song table.'''
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * From Song Where spotipy_id = ?", (spotipy_id,))
        row = cursor.fetchone()
        if row is not None:
            pass
        cursor.execute("INSERT INTO Song (Title, Artist, Playlist_ID, Spotipy_ID, URL) VALUES (?, ?, ?, ?, ?)",(title, artist, playlist_id, spotipy_id, url))
        conn.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()


def delete_matches(user1_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        cursor.execute("""DELETE FROM Matches WHERE user1_id = ?""", (user1_id,))
        conn.commit()
    except sqlite3.Error as error:
        print(error)
    conn.close()
def insert_matches(user1_id, user2_id):
    '''Inserts a new match into the Matches table.'''
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        # Make sure match doesn't exist
        cursor.execute("SELECT * FROM Matches WHERE user1_id = ? AND user2_id =?", (user1_id, user2_id))
        tryCurrentMatch = cursor.fetchone()
        if tryCurrentMatch is None:
            pass
        cursor.execute("INSERT INTO Matches (user1_id, user2_id) VALUES (?, ?)", (user1_id, user2_id))
        conn.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()

def insert_songs_sent(match_id, sender_id, receiver_id, song_id):
    '''Inserts a new record into the SongsSent table.'''
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        print(match_id)
        print(sender_id)
        print(receiver_id)
        print(song_id)
        cursor.execute("INSERT INTO SongsSent (match_id, sender_id, receiver_id, song_id) VALUES (?, ?, ?, ?)", (match_id, sender_id, receiver_id, song_id))
        conn.commit()
    except sqlite3.Error as error:
        print(error)

    finally:
        conn.close()

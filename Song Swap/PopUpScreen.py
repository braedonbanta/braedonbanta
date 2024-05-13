import sqlite3
import webbrowser
import requests
from spotipy import Spotify
from flask import Flask, render_template, jsonify, request, \
    session  # Jsonify is used to communicate with HTML functions
import os
import Playlist
import Song
import playlists_grab
from spotipy.oauth2 import SpotifyOAuth
import random


app = Flask(__name__, static_folder='Templates/Images', template_folder='html/Templates')  # Static_folder is where static asset files are stored
app.config['SECRET_KEY'] = os.urandom(64)

client_id = "de8dfa5743864623807a250061e269e0"
client_secret = "5f3ce43f0e0b4ae6b9f7f4f33de920cd"
redirect_uri = "http://localhost:5000/callback"

sp_oath = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, show_dialog=True)
sp = Spotify(auth_manager=sp_oath)
from flask import Flask, render_template, jsonify  # Jsonify is used to communicate with HTML functions
import Playlist

db = sqlite3.connect('songswap.db', check_same_thread=False)
cursor = db.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS Likes_Dislikes (songName TEXT,artistName TEXT, likes INTEGER DEFAULT 0, dislikes INTEGER DEFAULT 0)")


@app.route("/")
def hello_world():
    """
    Purpose: Renders the basic HTML main page
    Return: The index page
    """
    return render_template('index.html')






def popup():
    song = 'spotify' + ':track:' + session.get('current_song_ID')
    art = sp.track(song)['album']['images'][0]['url']
    playlist_name = playlists_grab.get_playlists()
    return render_template('popup_window.html', playlists=playlist_name, images=art)

# This function triggers once the thumbs up image is clicked
def upvote():
    """
    Purpose: Processes upvotes when user clicks on the upvote button from popup page
    Return: The likeRatio to the html form
    """
    if session.get('voted') == False:
        current_song_ID = session.get("current_song_ID")
        try:
            cursor.execute("SELECT * FROM Likes_Dislikes WHERE song_id = ?",
                           (current_song_ID,))
            isInDB = cursor.fetchall()
            if len(isInDB) == 0:
                print("Adding " + current_song_ID + " to DB")
                cursor.execute("INSERT INTO Likes_Dislikes (song_id, likes, dislikes) VALUES (?, 0, 0)",
                               (current_song_ID,))
            cursor.execute("UPDATE Likes_Dislikes SET likes = likes + 1 WHERE song_id = ?",
                           (current_song_ID,))
            cursor.execute("SELECT likes, dislikes FROM Likes_Dislikes WHERE song_id = ?",
                           (current_song_ID,))
            likes, dislikes = cursor.fetchone()
            db.commit()
            if dislikes != 0:
                likeRatio = likes / (likes + dislikes) * 100
            else:
                likeRatio = 100
        except ValueError:
            print("Could not retrieve song information from DB")
            likeRatio = None
            return jsonify({'result': 'There was an error retrieving like ratios.', 'likeRatio': ''})
        session["voted"] = True
        return jsonify({'result': 'Upvote processed successfully', 'likeRatio': likeRatio})
    else:
        return None


def downvote():
    """
    Purpose: Processes downvotes on the popup page
    Returns: The likeRatio to the html form
    """
    if session.get("voted") == False:
        current_song_ID = session.get("current_song_ID")
        try:
            cursor.execute("SELECT * FROM Likes_Dislikes WHERE song_id = ?",
                           (current_song_ID,))
            isInDB = cursor.fetchall()
            if len(isInDB) == 0:
                print("Adding " + current_song_ID + " to DB")
                cursor.execute("INSERT INTO Likes_Dislikes (song_id, likes, dislikes) VALUES (?, 0, 0)",
                               (current_song_ID,))
            cursor.execute("UPDATE Likes_Dislikes SET dislikes = dislikes + 1 WHERE song_id = ?",
                           (current_song_ID,))
            cursor.execute("SELECT likes, dislikes FROM Likes_Dislikes WHERE song_id = ?",
                           (current_song_ID,))
            likes, dislikes = cursor.fetchone()
            if dislikes != 0:
                likeRatio = likes / (likes + dislikes) * 100
            else:
                likeRatio = 100
            db.commit()
        except ValueError:
            print("Could not retrieve song information from DB")
            likeRatio = None
            return jsonify({'result': 'There was an error retrieving like ratios.', 'likeRatio': ''})

        session["voted"] = True
        return jsonify({'result': 'Downvote processed successfully', 'likeRatio': likeRatio})
    else:
        return None



if __name__ == '__main__':
    app.run(debug=True)
def playlist():
    playlist_name = Playlist.playlist()
    # return render_template('popup_window.html', playlist=playlist_name)
    return jsonify({'playlists': playlist_name})

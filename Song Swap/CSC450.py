import Algorithm
import os
from flask import Flask, session, url_for, redirect, request, render_template
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler
import url_playlist


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)

client_id = "de8dfa5743864623807a250061e269e0"
client_secret = "5f3ce43f0e0b4ae6b9f7f4f33de920cd"
redirect_uri = "http://localhost:5000/callback"
scope = 'playlist-read-private'

'''
@app.route('/get_playlists')
def get_playlists():
    """
        Retrieves user's playlists and generates HTML representation.

        @return: HTML representation of user's playlists
    """
    if not sp_oath.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oath.get_authorize_url()
        return redirect(auth_url)
    playlists = sp.current_user_playlists()

    playlists_info = [(pl['name'],pl['external_urls']['spotify'],pl['id']) for pl in playlists['items']]
    playlists_html = '<br>'.join(f'{name}:{url}\n ID:{id}' for name, url, id, in playlists_info)


    return playlists_html
'''


@app.route('/logout')
def logout():
    """
        Clears session data and redirects to home.

        @return: Redirect response
    """
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
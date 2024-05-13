import spotipy
from flask import session
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import sqlite3
import Song

# Set up your Spotify API credentials
client_id = "de8dfa5743864623807a250061e269e0"
client_secret = "5f3ce43f0e0b4ae6b9f7f4f33de920cd"
redirect_uri = "http://localhost:5000/callback"

conn = sqlite3.connect('songSwap.db')

cur = conn.cursor()

def get_playlists():
    '''
        Retrieves a list of playlist names belonging to the current user.
        Returns:
            list: A list of playlist names.
        '''
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   ))
    playlists = sp.current_user_playlists()
    playlist_list = []
    for playlist in playlists['items']:
        playlist_name = playlist['name']
        playlist_list.append(playlist_name)
    return playlist_list

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


def song_objects(playlist_tracks):
    songs_list = []
    for track in playlist_tracks:
        # Extract relevant information for creating a Song object
        song_name = track['track']['name']
        song_artist = track['track']['artists'][0]['name']
        song_id = track['track']['id']
        song_url = track['track']['external_urls']['spotify']

        # Create a Song object and append it to the list
        song_object = Song.Song(song_name, song_artist, song_id, song_url)
        songs_list.append(song_object)
    return songs_list
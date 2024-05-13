import sqlite3
import re

from flask import session
from spotipy import Spotify
import playlists_grab
from spotipy.oauth2 import SpotifyOAuth

# Set up your Spotify API credentials
client_id = "de8dfa5743864623807a250061e269e0"
client_secret = "5f3ce43f0e0b4ae6b9f7f4f33de920cd"
redirect_uri = "http://localhost:5000/callback"
scope = 'playlist-modify-public'

sp_oath = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope,
                       show_dialog=True)
sp = Spotify(auth_manager=sp_oath)

conn = sqlite3.connect('songSwap.db')

cur = conn.cursor()

# db = sqlite3.connect("songSwap.db")

# class Playlist:
#     userPlaylists = {}
#
#     def __init__(self, username=None):
#         self.size = 0
#         self.username = username
#
#     def set_user(self, username):
#         self.username = username
#
#     def get_user(self):
#         return self.username
#
#     @staticmethod
#     def playlist_size(playlist):
#         """
#         Returns the size of the playlist
#         :param playlist: playlist name
#         :return: the size of the playlist
#         """
#         size = len(Playlist.userPlaylists.get(playlist))
#         return size

def add_playlist(playlist_name):
    """
    Adds a song to a specific playlist
    :param playlistname: The specified playlist
    :return: Nothing
    """
    # db = sqlite3.connect("songSwap.db")
    # db.execute("INSERT INTO playlistName VALUES (?, ?)",
    #            (str(self.username), playlistname))
    # db.commit()
    # db.close()
    sp.user_playlist_create(playlist_name)


def playlist():
    user_playlists = []
    spotify_playlist = sp.current_user_playlists()
    for n in spotify_playlist['items']:
        user_playlists.append(n['name'])
    return user_playlists

# For testing
# songList = ["Dancing in the moonlight", "See the light", "We Dat Nice", "Gimmie the loot", "Big Pappa"]
# artistList = ["King Harvest", "Neelix", "Poor Righteous Teachers", "The Notorious B.I.G", "The Notorious B.I.G"]
#
# test1 = Playlist()
# test1.set_user("Mike")
# test1.add_playlist("My Playlist")
# test1.add_song("My Playlist", "King Harvest", "Dancing in the moonlight")
# for n in range(len(songList)):
#     test1.add_song("My Playlist", artistList[n], songList[n])
#
#
# test2 = Playlist()
# test2.set_user("Nick")
# songList1 = ["Over the Hills and Far Away", "My Old School", "Oh Sarah", "Virginia"]
# artistList1 = ["Led Zeppelin", "Steely Dan", "Sturgill Simpson", "Whiskey Myers"]
# test2.add_playlist("My Second Playlist")
# for i in range(len(songList1)):
#     test2.add_song("My Second Playlist", artistList1[i], songList1[i])

def track(song):
    return sp.track(song)

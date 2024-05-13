"""
This is a test file for Playlist.py, this file grabs all the current user's playlist, adds three songs, and
pulls up the playlist to verify that it worked as intended.
"""

import webbrowser
import Playlist
import playlists_grab

play_list = Playlist.playlist()
acc1 = 1
for n in play_list:
    print("Playlist", acc1, ": " + n)
    acc1 += 1

print("\n" + "--------" * 8 + "\n")

"""
The following is the test playlist and three songs that will be added to the playlist
"""
playlist = "5tv39UVUtkkVkrpYW2ohwo"
tunk_tunk = "spotify:track:131yybV7A3TmC34a0qE8u8"
rick_ashley = "spotify:track:4PTG3Z6ehGkBFwjybzWkR8"
sanic = "spotify:track:1PvottCnfZi3RCZVVZ2WtD"

Playlist.add_song(playlist, tunk_tunk)
Playlist.add_song(playlist, rick_ashley)
Playlist.add_song(playlist, sanic)
songs = playlists_grab.get_songs(playlist)
acc2 = 1
for song in songs:
    print("Song", acc2, ": ", song['track']['name'])
    acc2 += 1

print("\nDictionary containing all the information about the song: ", Playlist.track("131yybV7A3TmC34a0qE8u8"))

webbrowser.open("https://open.spotify.com/playlist/5tv39UVUtkkVkrpYW2ohwo")

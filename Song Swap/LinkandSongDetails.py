from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
# import spotipy
# import sqlite3

# Set up your Spotify API credentials
client_id = "de8dfa5743864623807a250061e269e0"
client_secret = "5f3ce43f0e0b4ae6b9f7f4f33de920cd"
redirect_uri = "http://localhost:5000/callback"
scope = 'playlist-read-private'

sp_oath = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

sp = Spotify(auth_manager=sp_oath)


# Gets all the info to the songs in playlists
def create_playlist_info_list(sp):
    """

    :param sp:
    :return: users playlists along with all song names, artists, ID's and url
    """
    playlist_info_list = []

    # Get user's name
    user_name = sp.me()['display_name']

    # Get all playlists for the authenticated user
    playlists = sp.current_user_playlists()

    # Iterate through each playlist
    for playlist in playlists['items']:
        playlist_id = playlist['id']
        playlist_name = playlist['name']

        # Get the tracks in the playlist, handling pagination
        results = sp.playlist_tracks(playlist_id)
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])

        # Iterate through each track in the playlist
        for track in tracks:
            track_info = track['track']
            track_name = track_info['name']
            track_artist = track_info['artists'][0]['name']
            track_id = track_info['id']
            track_url = track_info['external_urls']['spotify']

            track_dict = {
                "User name": user_name,
                'playlist_name': playlist_name,
                'song_name': track_name,
                'artist': track_artist,
                'song_id': track_id,
                'url': track_url
            }
            print(f"User Name : {user_name}")
            print(f"Playlist Name: {playlist_name}")
            print(f"Song Name: {track_name}")
            print(f"Artist: {track_artist}")
            #  print(f"Genre: ")  # Genre information not available
            print(f"Song ID: {track_id}")
            print(f"URL: {track_url}")
            print("")

            playlist_info_list.append(track_dict)

    return playlist_info_list


# Function to search for a song by playlist name, song name, and artist name
# Will be changed to use in database when song table is implemented
def search_song_in_playlist(playlist_info, playlist_name, song_name, artist_name):
    """
    Searches each song in every playlist returning song URL
    :param playlist_info: list of all playlist ID's
    :param playlist_name: name of playlist
    :param song_name: name of song
    :param artist_name: name of artists
    :return: URL
    """
    for track_info in playlist_info:
        if (track_info['playlist_name'] == playlist_name) and \
                (track_info['song_name'] == song_name) and \
                (track_info['artist'] == artist_name):
            return track_info['url']
    return None


# Call the function to create the playlist info list
playlist_information = create_playlist_info_list(sp)

# Example: Searching for a songs URL by playlist name, song name, and artist name
# Super slow now but when its in database it will process a lot faster
search_playlist_name = "IDEK ANYMORE"
search_song_name = "Jordan Belfort"
search_artist_name = "Wes Walker"

url = search_song_in_playlist(playlist_information, search_playlist_name, search_song_name, search_artist_name)
if url:
    print("URL:", url, " ", "Playlist", search_playlist_name)
else:
    print("Song not found in the specified playlist.")

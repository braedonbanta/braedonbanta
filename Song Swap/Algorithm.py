import spotipy
import re
import sqlite3
from spotipy.oauth2 import SpotifyClientCredentials

# This section sandwiched in the asterisks is important to get everything working. Use for every Spotipy file.
# **********************
# Set up your Spotify API credentials
client_id = "de8dfa5743864623807a250061e269e0"
client_secret = "5f3ce43f0e0b4ae6b9f7f4f33de920cd"

# Initialize Spotipy client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# ************************

def playlist_extraction(playlist_id):
    '''
       Extracts songs from a Spotify playlist and retrieves user taste.

       :param playlist_id: ID of the Spotify playlist.
       :return: Genres and average audio features of the playlist.
       '''
    results = sp.playlist_items(playlist_id)
    track_ids = []
    for item in results['items']:
        track = item['track']
        track_ids.append(track['id'])
    return get_user_taste(track_ids)

def get_song_genre(track_id):
    '''
    Retrieves the genres of a song from its track ID.

    :param track_id: Spotify track ID.
    :return: List of genres associated with the song.
    '''
    # Retrieve track information
    track_info = sp.track(track_id)

    # Spotify doesn't keep track of genres for a song, but instead uses it for artists
    # So we get artist IDs from the track information
    # use a set to avoid duplicates
    artist_genres = set()
    for artist in track_info['artists']:
        artist_info = sp.artist(artist['id'])
        artist_genres.update(artist_info.get('genres', []))

    return list(artist_genres)  # Convert set to list for easier handling

def get_audio_features(track_id):
    '''
    Retrieves the audio features of a song from its track ID.

    :param track_id: Spotify track ID.
    :return: Dictionary of audio features.
    '''
    # get the audio features of the track id
    audio_features = sp.audio_features([track_id])[0]
    return audio_features

def get_user_taste(playlist):
    '''
    Retrieves the genres and average audio features of a playlist.

    :param playlist: List of Spotify track IDs.
    :return: Tuple containing genres (list) and average audio features (dict).
    '''
    sum_features = {'acousticness': 0, 'danceability': 0, 'energy': 0, 'instrumentalness': 0,
                'liveness': 0, 'loudness': 0, 'speechiness': 0, 'tempo': 0, 'valence': 0}
    count_features = {'acousticness': 0, 'danceability': 0, 'energy': 0, 'instrumentalness': 0,
                  'liveness': 0, 'loudness': 0, 'speechiness': 0, 'tempo': 0, 'valence': 0}
# using a set called seen_genres to prevent duplicates
    seen_genres = set()
    songs = sp.tracks(playlist)
    songs = songs['tracks']
    artists = []
    for n in songs:
        song = n['album']['artists'][0]['id']
        artists.append(song)
    audio_features = sp.audio_features(playlist)
    audio_features = audio_features[0]
    artist_info = []
    artists_data = sp.artists(artists)
    artists_data = artists_data['artists']
    for artist in artists_data:
        genres = artist.get('genres', [])
        artist_info.append(genres)
        seen_genres.update(genres)

    for audio_feature in sum_features:
        sum_features[audio_feature] += audio_features[audio_feature]
        if audio_features[audio_feature] is not None:
            count_features[audio_feature] += 1

# To get the average value of a feature throughout a playlist of song
    average_features = {
        audio_feature: sum_features[audio_feature] / count_features[audio_feature] if count_features[audio_feature] != 0 else 0
        for audio_feature in sum_features
    }
    return list(seen_genres), average_features

def genre_comparison(user1_genres, user2_genres):
    '''
    Compares the similarity of genres associated with two users' playlists.

    :param user1_genres: List of genres for user 1.
    :param user2_genres: List of genres for user 2.
    :return: True if genres are similar, False otherwise.
    '''
    # get the length of the intersection between the two lists
    intersection_length = len(set(user1_genres) & set(user2_genres))
    shortest_length = min(len(user1_genres), len(user2_genres))
    similarity_percentage = (intersection_length / shortest_length) * 100
    # the value that is currently 33 can change later
    return similarity_percentage >= 33


def audio_feature_comparison(user1_mood, user2_mood):
    '''
    Compares the similarity of audio features associated with two users' playlists.

    :param user1_mood: Dictionary of audio features for user 1.
    :param user2_mood: Dictionary of audio features for user 2.
    :return: True if audio features are similar, False otherwise.
    '''
    # list that will fill with the boolean values of whether the values of user1's mood and user2's mood are similar
    checks = []
    for mood in user1_mood:
        if mood in user2_mood:
            mood_value1 = user1_mood[mood]
            mood_value2 = user2_mood[mood]
            # Calculate the threshold as a percentage of the maximum mood value
            threshold = 0.45 * max(mood_value1, mood_value2)
            difference = abs(mood_value1 - mood_value2)
            checks.append(difference <= threshold)
    # Count the number of true and false checks
    true_counts = sum(checks)
    false_counts = len(checks) - true_counts
    return true_counts > false_counts




import spotipy
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

# Hard coded artist and song name

artist_ = 'The Police'
song_ = 'De Do Do Do, De Da Da Da'


def songLink(artist, song):
    """
    Method that finds the link to the song on Spotify
    :param artist: The name of the artist
    :param song: The name of the song
    :return: the link to the song on spotify
    """
    # Search that finds the song on Spotify
    result = sp.search(q=f'track:{song} artist:{artist}', type='track')

    # How to get the Songs link
    if result['tracks']['items']:
        # Get the first result for the song
        track = result['tracks']['items'][0]
        # Get the Spotify link to the song
        spotify_link = track['external_urls']['spotify']

        print(f"Spotify link for", song, ":", spotify_link)
    else:
        print(f"No results found for the song")


songLink(artist_, song_)


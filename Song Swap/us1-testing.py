import unittest
from unittest.mock import patch, MagicMock

from url_playlist import app, connect_to_database

class TestRegister(unittest.TestCase):
    """Class that tests the Register function in out Project. Testing this because it is important to get the user to
    the feed page."""
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True

    def tearDown(self):
        pass

    def test_get_register_page(self):
        """Test if the registration page is rendered correctly"""
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        #assert that /register outputs all the things unique to the register page
        self.assertIn(b'<title>Register</title>', response.data)
        self.assertIn(b'<h1>Register</h1>', response.data)
        self.assertIn(b'Username:', response.data)
        self.assertIn(b'Email:', response.data)
        self.assertIn(b'Password:', response.data)
        self.assertIn(b'Spotify Username:', response.data)
        self.assertIn(b'<input type="submit" value="Register">', response.data)

    def test_register_new_user(self):
        """Test if registering a new user redirects to the playlist selection page"""
        data = {'username': 'new_user', 'email': 'new_user@example.com', 'password': 'password', 'spotify_username': 'new_spotify_user'}
        response = self.app.post('/register', data=data, follow_redirects=True)
        self.assertIn(b'Select a Playlist', response.data)
        self.assertIn(b'<h1>Select a Playlist</h1>', response.data)


class TestPlaylistSelector(unittest.TestCase):
    """Testing the PlaylistSelector function in our Flask app because it's part of the registration process"""
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_playlist_selector_get_request(self):
        """Test if the playlist selector page is rendered correctly for GET request"""
        response = self.app.get('/playlist_selector')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Select a Playlist</h1>', response.data)
        self.assertIn(b'<form method="POST" action="/home">', response.data)
        self.assertIn(b'<label for="playlist">Choose a playlist:</label>', response.data)
        self.assertIn(b'<select name="playlist" id="playlist">', response.data)
        self.assertIn(b'<input type="submit" value="Submit">', response.data)


    #patching in the registration data the user needs to register and redirect to Feed page
    @patch('url_playlist.session', {'registration_data': {
        'username': 'test_user',
        'email': 'test@example.com',
        'password': 'test_password',
        'spotify_username': 'test_spotify_user'
    }})
    def test_playlist_selector_post_request_redirect(self):
        """Test if the playlist selector redirects to feed page for POST request"""
        data = {'playlist': 'PLAYLIST'}
        response = self.app.post('/playlist_selector', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Feed</h1>', response.data)

class TestFeed(unittest.TestCase):
    """Testing the feed page's functionality related towards User Story #1: Whether it displays matches if user has matches
    or displays 'no matches yet' if user has no matches."""
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

    @patch('url_playlist.connect_to_database')
    def test_feed_page_logged_in(self, mock_connect):
        """Testing if the feed page only displays if user is logged in"""
        with app.test_client() as client:
            mock_cursor = MagicMock()
            # Simulate a logged-in user by simulating a session object of user's username
            with client.session_transaction() as sess:
                sess['username'] = 'test_user'

            # Mock the return value of connect_to_database
            mock_connect.return_value = (MagicMock(), mock_cursor)

            # Send a GET request to the feed endpoint
            response = client.get('/feed')

            # Check that the response status code is 200 OK
            self.assertEqual(response.status_code, 200)

            # Assert that the expected elements are present in the response data
            self.assertIn(b'Feed', response.data)

    def test_feed_page_not_logged_in(self):
        """Testing the functionality of being redirected to login if user has not logged in"""
        with self.app as client:
            # Simulate not logged in user (no username in session)
            response = client.get('/feed')

            # Assert that response status code is 200 OK (since it renders login page)
            self.assertEqual(response.status_code, 200)

            # Assert that feed page redirects to login page when not logged in
            self.assertIn(b'<h1>Login</h1>', response.data)

    # Acceptance Criteria For User Story #1: User is shown No matches found yet if they haven't matched with user
    @patch('url_playlist.connect_to_database')
    def test_feed_no_matches(self, mock_connect):
        """Simulating a case where a user has no matches."""
        with app.test_client() as client:
            mock_cursor = MagicMock()
            # Simulate a logged-in user
            with client.session_transaction() as sess:
                sess['username'] = 'test_user'

            # Mock the return value of connect_to_database
            mock_connect.return_value = (MagicMock(), mock_cursor)

            # Send a GET request to the feed endpoint
            response = client.get('/feed')

            # Check that the response status code is 200 OK
            self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p>No matches found yet.</p>', response.data)

    # Acceptance Criteria For User Story #2: User is shown matches if they have gotten a match
    @patch('url_playlist.connect_to_database')
    def test_feed_matches(self, mock_connect):
        """Simulating a case where a user has matches."""
        with app.test_client() as client:
            mock_cursor = MagicMock()
            # Simulate a logged-in user
            with client.session_transaction() as sess:
                sess['username'] = 'test_user'

            # Mock the return value of connect_to_database
            mock_connect.return_value = (MagicMock(), mock_cursor)
            # simulate matches being fetched from the database
            mock_cursor.fetchall.return_value = [(1,), (2,)]

            # Send a GET request to the feed endpoint
            response = client.get('/feed')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<th>MATCHES</th>', response.data)

if __name__ == '__main__':
    unittest.main()

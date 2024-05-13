import unittest
from unittest.mock import patch, MagicMock

from url_playlist import app


class TestCheckCredentials(unittest.TestCase):
    """Class that tests the Check credentials function in out Project. Testing this because it is important to correctly notify if the
    users credentials are correct or not."""

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True

    def tearDown(self):
        pass

    def test_get_login_page(self):
        """Test if the login page is rendered correctly"""
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        # assert that /login outputs all the things unique to the register page
        self.assertIn(b'<title>Login</title>', response.data)
        self.assertIn(b'<h1>Login</h1>', response.data)
        self.assertIn(b'Username:', response.data)
        self.assertIn(b'Password:', response.data)
        self.assertIn(b'<input type="submit" value="Login">', response.data)

    @patch('url_playlist.redirect')
    @patch('url_playlist.url_for')
    # Acceptance Criteria For User Story #6: The user is redirected to the applications home page after a successful login.
    def test_login_correct_credentials(self, mock_url_for, mock_redirect):
        """Test if correct credentials redirects you to the feed"""
        data = {'username': 'cat', 'password': 'cat', }
        mock_url_for.return_value = '/feed'  # Simulate correct redirection
        response = self.app.post('/login', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)  # Assuming 'feed' page returns 200
        mock_redirect.assert_called_with('/feed')

    # Acceptance Criteria For User Story #6:The user is prompted to reenter credentials after failing to validate credentials.
    def test_login_incorrect_credentials(self):
        """Tests if the user is prompted to re-enter the correct credentials"""
        data = {'username': 'cat', 'password': 'peanut', }
        response = self.app.post('/login', data=data, follow_redirects=True)
        self.assertIn(b'Username and/or password is wrong, please retry', response.data)

    # Acceptance Criteria For User Story #6:The user is prompted to reenter credentials after failing to validate credentials.
    def test_login_missing_username(self):
        """Tests if the user is prompted to re-enter the correct credentials"""
        data = {'username': '', 'password': 'cat', }
        response = self.app.post('/login', data=data, follow_redirects=True)
        self.assertIn(b'required', response.data)

    # Acceptance Criteria For User Story #6:The user is prompted to reenter credentials after failing to validate credentials.
    def test_login_missing_password(self):
        """Tests if the user is prompted to re-enter the correct credentials"""
        data = {'username': 'cat', 'password': '', }
        response = self.app.post('/login', data=data, follow_redirects=True)
        self.assertIn(b'required', response.data)


if __name__ == '__main__':
    unittest.main()

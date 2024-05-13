import unittest
from unittest.mock import patch, MagicMock

import PopUpScreen
from PopUpScreen import app

# These tests reference user story number 18
# Acceptance criteria:
#   -The user is shown like and dislike percentages after picking whether they like the song
#   -The user is shown an error message if like/dislike ratios can not be retrieved from our database
class TestPopUpScreen(unittest.TestCase):

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch('PopUpScreen.cursor')
    def test_upvote_success(self, mock_cursor):
        # Make sure upvotes are working correctly
        # Mocking the database cursor
        mock_cursor.fetchone.return_value = (50, 20)  # Simulating the database response
        song = PopUpScreen.NewSong  # Using a test song
        like_ratio_before = 50 / (50 + 20) * 100  # Expected like ratio before upvote

        # Calling the upvote function
        result = PopUpScreen.upvote(song)
        data = result.get_json()

        # Asserting the result
        self.assertEqual(data['result'], 'Upvote processed successfully')
        self.assertEqual(data['likeRatio'], like_ratio_before)

    @patch('PopUpScreen.cursor')
    def test_downvote_success(self, mock_cursor):
        # Make sure that downvotes work
        # Mocking the database cursor
        mock_cursor.fetchone.return_value = (60, 30)
        song = PopUpScreen.NewSong  # Using a test song
        like_ratio_before = 60 / (60 + 30) * 100  # Expected like ratio (before downvote)

        # Calling the downvote function
        result = PopUpScreen.downvote(song)
        data = result.get_json()

        # Asserting the result
        self.assertEqual(data['result'], 'Downvote processed successfully')
        self.assertEqual(data['likeRatio'], like_ratio_before)

    @patch('PopUpScreen.cursor')
    def test_upvote_error(self, mock_cursor):
        # Tests to make sure upvote error messages are shown
        # Mocking the database cursor
        mock_cursor.fetchone.side_effect = ValueError("Database error")  # Simulating database error
        song = PopUpScreen.NewSong  # Using a test song

        # Calling the upvote function
        result = PopUpScreen.upvote(song)
        data = result.get_json()

        # Asserting the error message
        self.assertEqual(data['result'], 'Error: Could not retrieve like ratio from database')

    @patch('PopUpScreen.cursor')
    def test_downvote_error(self, mock_cursor):
        # Tests to make sure downvote error messages are shown
        mock_cursor.fetchone.side_effect = ValueError("Database error")  # Simulating database error
        song = PopUpScreen.NewSong  # Using a test song

        # Calling the downvote function
        result = PopUpScreen.downvote(song)
        data = result.get_json()

        # Asserting the error message
        self.assertEqual(data['result'], 'Error: Could not retrieve like ratio from database')


if __name__ == "__main__":
    unittest.main()

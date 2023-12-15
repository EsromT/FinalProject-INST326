import pandas as pd
import unittest
from unittest import mock

# Import functions and classes
from recommender import process_movie_data, MovieRecommender, GenrePicker

class TestMovieRecommendation(unittest.TestCase):
    """A test class for Movie Recommendation functions and classes."""

    def setUp(self):
        """Set up data for testing."""
        self.sample_data_path = "titles.csv"

    def test_process_movie_data(self):
        """Test the process_movie_data function."""
        processed_data = process_movie_data(self.sample_data_path)
        self.assertIsInstance(processed_data, pd.DataFrame)

    def test_movie_recommender(self):
        """Test the MovieRecommender class."""
        # Create a sample DataFrame for testing
        sample_data = pd.DataFrame({
            'genres': [['action'], ['drama'], ['war']]
        })

        # Initialize MovieRecommender with the sample data
        recommender = MovieRecommender(sample_data)

        # Test the recommend_movie method
        recommended_movie = recommender.recommend_movie('action')

        # Assert that the recommended_movie is a DataFrame
        self.assertIsInstance(recommended_movie, pd.Series)

    def test_genre_picker(self):
        """Test the GenrePicker class."""
        # Create a sample list of genres for testing
        sample_genres = ['action', 'drama', 'war']

        # Initialize GenrePicker with the sample genres
        genre_picker = GenrePicker(sample_genres)

        # Test get_genre_choice method
        with unittest.mock.patch('builtins.input', return_value='action'):
            user_choice = genre_picker.get_genre_choice()

        # Assert that the user_choice is the expected genre
        self.assertEqual(user_choice, 'action')

if __name__ == '__main__':
    unittest.main()

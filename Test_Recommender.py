import unittest
import pandas as pd

from recommender import process_movie_data, Rate, GenrePicker, MovieRecommender

class TestMovieFunctions(unittest.TestCase):

    def setUp(self):
        #Set up any necessary data or objects for your tests here
        self.movies_data = process_movie_data("titles.csv")

    def test_process_movie_data(self):
        self.assertIsInstance(self.movies_data, pd.DataFrame)
        self.assertGreater(len(self.movies_data), 0)
        self.assertTrue('title' in self.movies_data.columns)
        self.assertTrue('type' in self.movies_data.columns)
        self.assertTrue('release_year' in self.movies_data.columns)
        self.assertTrue('genres' in self.movies_data.columns)
        self.assertTrue('imdb_score' in self.movies_data.columns)
        self.assertTrue('tmdb_score' in self.movies_data.columns)
        
    def test_best_rated_movie(self):
        # Test if best_rated_movie returns a valid result
        rate_instance = Rate()
        result = rate_instance.best_rated_movie(self.movies_data)
        self.assertIsInstance(result, pd.Series)
        self.assertTrue('imdb_score' in result.index)
        self.assertTrue('tmdb_score' in result.index)
        





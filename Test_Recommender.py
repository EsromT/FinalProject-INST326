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
        

### Test Case for the other reco.py code in case.
import unittest
from tkinter import Tk
from tkinter import ttk
from tkinter import Label

class TestMovieGenreSelector(unittest.TestCase):
    def test_show_movie(self):
        # Create the main window
        root = Tk()
        root.title("Movie Genre Selector")

        # Genre selection dropdown
        genre_var = tk.StringVar()
        genre_label = Label(root, text="Select Genre:")
        genre_label.pack(pady=10)
        genre_dropdown = ttk.Combobox(root, textvariable=genre_var, values=["crime", "drama", "comedy"])
        genre_dropdown.pack(pady=10)

        # Button to show selected movie
        show_button = tk.Button(root, text="Show Movie", command=show_movie)
        show_button.pack(pady=10)

        # Label to display the result
        result_label = tk.Label(root, text="")
        result_label.pack(pady=10)

        # Set the selected genre and trigger the show_movie function
        genre_var.set("crime")
        show_movie()

        # Assert that the result_label text is as expected
        self.assertEqual(result_label.cget("text"), "No movies found for the selected genre.")

if __name__ == '__main__':
    unittest.main()




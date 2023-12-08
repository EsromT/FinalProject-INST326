import pandas as pd
# Simple Content-Based Movie Recommendation Prototype 
# David Onafuwa, Esrom Tesfay, Ricardo Siles-Herrera
class GenrePicker:
    """
    Class to prompt the user to pick a movie genre.

    Attributes:
        genres (list): List of available movie genres.
    """

    def __init__(self):
        """
        Initialize the GenrePicker object.
        """
        self.genres = []

    def get_genre_choice(self):
        """
        Prompt the user to pick a movie genre.

        Returns:
            str: Chosen movie genre.
        """
        print("Available Genres:")
        for genre in self.genres:
            print(f"- {genre}")
        
        while True:
            chosen_genre = input("Enter the genre you want to watch: ").strip().capitalize()
            if chosen_genre in self.genres:
                return chosen_genre
            else:
                print("Invalid genre. Please choose from the available genres.")

class MovieRecommendation:
    """
    Simple Content-Based Movie Recommendation Prototype.

    Attributes:
        file_path (str): The file path to the CSV file containing movie data.
        df (pd.DataFrame): The DataFrame containing movie data.
    """

    def __init__(self, file_path):
        """
        Initialize the MovieRecommendation object.

        Parameters:
            file_path (str): The file path to the CSV file containing movie data.
        """
        self.df = pd.read_csv(file_path)
        self.genres = self.get_unique_genres()

    def get_unique_genres(self):
        """
        Get the unique movie genres from the DataFrame.

        Returns:
            list: List of unique movie genres.
        """
        return self.df['genres'].str.split(', ').explode().unique()

    def filter_movies(self, genre=None):
        """
        Filter the DataFrame to include only movies of the specified genre.

        Parameters:
            genre (str): Optional genre to filter by.

        Returns:
            pd.DataFrame: DataFrame containing only movies of the specified genre.
        """
        if genre:
            return self.df[self.df['genres'].str.contains(genre, case=False, na=False)]
        else:
            return self.df[self.df['titleType'].str.upper() == 'MOVIE']

    def sample_movies(self, n=100, genre=None):
        """
        Sample a subset of movies from the DataFrame.

        Parameters:
            n (int): Number of movies to sample.
            genre (str): Optional genre to filter by.

        Returns:
            pd.DataFrame: Sampled DataFrame containing movies.
        """
        return self.filter_movies(genre=genre).head(n=n)

    def clean_data(self, df):
        """
        Remove unnecessary columns from the DataFrame.

        Parameters:
            df (pd.DataFrame): Input DataFrame.

        Returns:
            pd.DataFrame: DataFrame with unnecessary columns removed.
        """
        unnecessary_columns = ['tconst', 'runtimeMinutes', 'genres', 'startYear',
                               'endYear', 'averageRating', 'numVotes']
        return df.drop(columns=unnecessary_columns)

    def recommend_movies(self, n=100, genre=None):
        """
        Recommend movies by applying filtering and sampling.

        Parameters:
            n (int): Number of movies to recommend.
            genre (str): Optional genre to filter by.

        Returns:
            pd.DataFrame: Recommended movies DataFrame.
        """
        sampled_movies = self.sample_movies(n=n, genre=genre)
        cleaned_movies = self.clean_data(sampled_movies)
        return cleaned_movies

if __name__ == "__main__":
    file_path = "C:\\Users\\esrom\\OneDrive\\Documents\\Final Project\\titles.csv"

    genre_picker = GenrePicker()
    genre_picker.genres = ["Action", "Comedy", "Drama", "Horror", "Science Fiction"]

    chosen_genre = genre_picker.get_genre_choice()

    movie_recommendation = MovieRecommendation(file_path)
    recommended_movies = movie_recommendation.recommend_movies(n=5, genre=chosen_genre)
    
    print(f"\nRecommended {chosen_genre} Movies:")
    print(recommended_movies)

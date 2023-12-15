import pandas as pd
# Simple Content-Based Movie Recommendation Prototype
# David Onafuwa, Esrom Tesfay, Ricardo Siles-Herrera
def process_movie_data(csv_path):
    # Read in CSV file as a dataframe
    df = pd.read_csv(csv_path)

    # Sorts the dataframe to only movies
    df_movies = df[df['type'].str.upper() == 'MOVIE']

    # Delete unnecessary columns from our dataset
    df_further_sampled_movies = df_movies.drop(columns=['id', 'runtime', 'production_countries', 'seasons',
                                                        'imdb_id', 'imdb_votes', 'tmdb_popularity', 'description',
                                                        'age_certification'])

    # Used only to import data to a CSV file to see the entirety of the updated dataframe
    df_further_sampled_movies.to_csv("output.csv", index=False)

    # Resets index of dataset from 1 to n to properly label the movies.
    df_further_sampled_movies = df_further_sampled_movies.reset_index(drop=True)
    df_further_sampled_movies.index += 1

    return df_further_sampled_movies

class Rate():
    def best_rated_movie(self, movies_data):
        mean_data = ['imdb_score', 'tmdb_score']
        mean_scores = movies_data[mean_data].mean()
        return mean_scores

class GenrePicker():
    """ Initialize the GenrePicker object. """

    def __init__(self, genres):
        self.genres = genres

    def get_genre_choice(self):
        print("Available Genres:")

        for genre in self.genres:
            print(f"- {genre}")

        while True:
            chosen_genre = input("Enter the genre you want to watch: ").strip().capitalize()
            if chosen_genre in self.genres:
                return chosen_genre
            else:
                print("Invalid genre. Please choose from the available genres.")

class MovieRecommender():
    def __init__(self, movies_data):
        self.movies_data = movies_data

    def recommend_movie(self, genre):
        genre_movies = self.movies_data[self.movies_data['genres'].apply(lambda x: genre.lower() in x.lower())]
        if not genre_movies.empty:
            top_movie = genre_movies.loc[genre_movies['imdb_score'].idxmax()]
            return top_movie
        else:
            return None

if __name__ == "__main__":
    # Process movie data and get genres from the entire dataset
    processed_data = process_movie_data("C:\\Users\\esrom\\OneDrive\\Documents\\FinalProject-INST326\\titles.csv")
    available_genres = processed_data['genres'].explode().unique()

    # Initialize GenrePicker with available genres
    genre_picker = GenrePicker(available_genres)

    # Get user's genre choice
    user_genre_choice = genre_picker.get_genre_choice()

    # Initialize MovieRecommender with the entire movie dataset
    recommender = MovieRecommender(processed_data)

    # Recommend a movie based on the user's chosen genre
    recommended_movie = recommender.recommend_movie(user_genre_choice)

    if recommended_movie is not None:
        print(f"\nWe recommend the following movie for the genre '{user_genre_choice}':")
        print(recommended_movie[['title', 'genres', 'imdb_score', 'tmdb_score']])
    else:
        print(f"\nSorry, no movie found for the genre '{user_genre_choice}'.")

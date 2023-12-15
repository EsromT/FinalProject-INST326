import pandas as pd
# Simple Content-Based Movie Recommendation Prototype
# David Onafuwa, Esrom Tesfay, Ricardo Siles-Herrera
def process_movie_data(csv_path):
    # Read in CSV file as a dataframe
    df = pd.read_csv(csv_path)

    # Sorts the dataframe to only movies
    df_movies = df[df['type'].str.upper() == 'MOVIE']

    # Delete unnecessary columns from our dataset
    df_movies = df_movies.drop(columns=['id', 'runtime', 'production_countries', 'seasons',
                                                        'imdb_id', 'imdb_votes', 'tmdb_popularity',
                                                        'age_certification'])

    #removes unnessesary characters from the column
    df_movies['genres'] = df_movies['genres'].apply(lambda x: [genre.strip("[]',\"") for genre in eval(x)])
    
    # Used only to import data to a CSV file to see the entirety of the updated dataframe
    df_movies.to_csv("output.csv", index=False)

    # Resets index of dataset from 1 to n to properly label the movies.
    df_movies = df_movies.reset_index(drop=True)
    df_movies.index += 1

    return df_movies




class GenrePicker():
    """ Initialize the GenrePicker object. """

    def __init__(self, genres):
        self.genres = genres
        
    
    def get_genre_choice(self):
        print("Available Genres:")

        #prints each genre in the list of genres
        for genre in self.genres:
            print(genre)

        #ask user for genre 
        while True:
            chosen_genre = input("Enter the genre you want to watch: ").strip()
            if chosen_genre in self.genres:
                return chosen_genre
            else:
                print("Invalid genre. Please choose from the available genres.")

class MovieRecommender():
    #recommends a movie from a choosen genre that is has higest imdb score
    def __init__(self, movies_data):
        self.movies_data = movies_data

    def recommend_movie(self, genre):
        #sorts genres column by genre choosen 
        genre_movies = self.movies_data[self.movies_data['genres'].apply(lambda x: genre.lower() in [g.lower() for g in x])]
        if not genre_movies.empty:
            #displays the highest rated movie in that particular genre
            top_movie = genre_movies.loc[genre_movies['imdb_score'].idxmax()]
            return top_movie
        else:
            return None

if __name__ == "__main__":
    # Process movie data and get genres from the entire dataset
    processed_data = process_movie_data("titles.csv")

    # Combines all genres list into one list to show the user a list of genres
    all_genres = [genre for genres_list in processed_data['genres'] for genre in genres_list]

    # Get unique genres and sort them
    unique_genres = sorted(set(all_genres))

    # Clean up unwanted characters in genres
    cleaned_genres = [str(genre).strip("[],'\"") for genre in unique_genres]

    #Displays Genres
    print("Available Genres:")
    for genre in cleaned_genres:
        print(genre)

    # Initialize GenrePicker with available genres
    genre_picker = GenrePicker(cleaned_genres)

    # Get user's genre choice
    user_genre_choice = genre_picker.get_genre_choice()

    # Initialize MovieRecommender with the entire movie dataset
    recommender = MovieRecommender(processed_data)

    # Recommend a movie 
    recommended_movie = recommender.recommend_movie(user_genre_choice)

    #Prints information about movie
    if recommended_movie is not None:
        print(f"\nWe recommend the following movie for the genre '{user_genre_choice}':")
        print(f"Title: {recommended_movie['title']}")
        print(f"Genres: {recommended_movie['genres']}")
        print(f"IMDb Score: {recommended_movie['imdb_score']}")
        print(f"TMDB Score: {recommended_movie['tmdb_score']}")
        print(f"Description: {recommended_movie['description']}")
    else:
        print(f"\nSorry, no movie found for the genre '{user_genre_choice}'.")

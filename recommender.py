import pandas as pd
# Simple Content-Based Movie Recommendation Prototype
# David Onafuwa, Esrom Tesfay, Ricardo Siles-Herrera
def process_movie_data(csv_path):
    #Read in CSV file as a dataframe
    df = pd.read_csv(csv_path)

    #Sorts the dataframe to only movies
    df_movies = df[df['type'].str.upper() == 'MOVIE']

    #We sample our dataset to the first 100 movies
    df_sampled_movies = df_movies.head(n=100)

    #Delete unnecessary columns from our dataset
    df_further_sampled_movies = df_sampled_movies.drop(columns=['id','runtime','production_countries', 'seasons', 
    'imdb_id', 'imdb_votes', 'tmdb_popularity', 'description', 'age_certification'])

    #Used only to import data to a csv file inorder to see entirety of updated dataframe
    df_further_sampled_movies.to_csv("output.csv", index=False)

    #Resets index of dataset from 1 to 100. Inorder to properly label first 100 movies.
    df_further_sampled_movies = df_further_sampled_movies.reset_index(drop=True)
    df_further_sampled_movies.index+=1

    return df_further_sampled_movies

#Checks if processed_data works
"""
processed_data = process_movie_data("C:\\Users\\esrom\\OneDrive\\Documents\\FinalProject-INST326\\titles.csv")
print(processed_data)"""


class Rate():
    def best_rated_movie(self, movies_data):
        mean_data = ['imdb_score', 'tmdb_score']
        mean_scores = movies_data[mean_data].mean()
        return mean_scores

#Tests mean of scores    
"""rate_instance = Rate()
result = rate_instance.best_rated_movie(df_further_sampled_movies)

print(result)"""


class GenrePicker():

    """ Initialize the GenrePicker object. """

    def __init__(self, ):
          self.genres = []
    

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
    

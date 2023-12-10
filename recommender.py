import pandas as pd
# Simple Content-Based Movie Recommendation Prototype
# David Onafuwa, Esrom Tesfay, Ricardo Siles-Herrera

#Read in CSV file as a dataframe
df = pd.read_csv("C:\\Users\\esrom\\OneDrive\\Documents\\FinalProject-INST326\\titles.csv")

#Sorts the dataframe to only movies
df_movies = df[df['type'].str.upper() == 'MOVIE']

#We sample our dataset to the first 100 movies
df_sampled_movies = df_movies.head(n=100)

#Delete unnecessary columns from our dataset
df_further_sampled_movies = df_sampled_movies.drop(columns=['id','runtime','production_countries', 'seasons', 
'imdb_id', 'imdb_votes', 'tmdb_popularity', 'description', 'age_certification'])

#Used only to import data to a csv file inorder to see entirety of updated dataframe
"""df_further_sampled_movies.to_csv("output.csv", index=False)"""

#Resets index of dataset from 1 to 100. Inorder to properly label first 100 movies.
df_further_sampled_movies = df_further_sampled_movies.reset_index(drop=True)
df_further_sampled_movies.index+=1


"""print(df_further_sampled_movies)"""

class Rate():
    def best_rated_movie(self, movies_data):
        mean_data = ['imdb_score', 'tmdb_score']
        mean_scores = movies_data[mean_data].mean()
        return mean_scores
    
"""rate_instance = Rate()
result = rate_instance.best_rated_movie(df_further_sampled_movies)

print(result)"""


class GenrePicker():
    def __init__(self, ):
          self.genres = []

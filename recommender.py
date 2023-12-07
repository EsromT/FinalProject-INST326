import pandas as pd
# Simple Content-Based Movie Recommendation Prototype
# David Onafuwa, Esrom Tesfay, Ricardo Siles-Herrera

#Read in CSV file as a dataframe
df = pd.read_csv("C:\\Users\\esrom\\OneDrive\\Documents\\Final Project\\titles.csv")

#Sorts the dataframe to only movies
df_movies = df[df['type'].str.upper() == 'MOVIE']

#We sample our dataset to the first 100 movies
df_sampled_movies = df_movies.head(n=100)

#Delete unnecessary columns from our dataset
df_further_sampled_movies = df_sampled_movies.drop(columns=['id','runtime','production_countries', 'seasons', 
'imdb_id', 'imdb_votes', 'tmdb_popularity'])

print(df_further_sampled_movies)

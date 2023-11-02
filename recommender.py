# Simple Content-Based Movie Recommendation Prototype
# David Onafuwa, Esrom Tesfay, Ricardo Siles-Herrera
# Sample dataset
data = {
    'Romance': ['The Notebook', 'Titanic', 'Sleepless in Seattle'],
    'Action': ['Die Hard', 'The Terminator', 'Rambo'],
    'Comedy': ['The Hangover', 'Superbad', 'Anchorman']
}


def recommend_movies(genre):
    if genre in data:
        return data[genre]
    else:
        return "Genre not found in the dataset."


print(recommend_movies('Romance'))
print(recommend_movies('Action'))
print(recommend_movies('Comedy'))
print(recommend_movies('Drama'))

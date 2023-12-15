import tkinter as tk
from tkinter import ttk

def show_movie():
    """
    Display selected movie(s) and their rating(s) based on the chosen genre.

    Reads the selected genre from the dropdown, filters movies based on the genre,
    and updates the result_label with movie information.

    Returns:
    - None
    """
    selected_genre = genre_var.get()
    selected_movies = [movie for movie in movies_data if selected_genre in movie['genres']]

    if selected_movies:
        movie_info = ""
        for movie in selected_movies:
            movie_info += f"{movie['title']} - Rating: {movie['imdb_score']}\n"
        result_label.config(text=movie_info)
    else:
        result_label.config(text="No movies found for the selected genre.")

# Reading movie data from the CSV file
with open('output.csv', 'r') as file:
    lines = file.readlines()
    header = lines[0].strip().split(',')
    movies_data = []
    for line in lines[1:]:
        values = line.strip().split(',')
        # Adjusted the indexing to correctly handle the 'genres' field
        movie = {header[i]: values[i].strip('\'') if i == 3 else values[i] for i in range(len(header))}
        movies_data.append(movie)

# Create the main window
root = tk.Tk()
root.title("Movie Genre Selector")

# Genre selection dropdown
genre_var = tk.StringVar()
genre_label = tk.Label(root, text="Select Genre:")
genre_label.pack(pady=10)
genre_dropdown = ttk.Combobox(root, textvariable=genre_var, values=list(set(genre.strip('[]\'') for movie in movies_data for genre in movie['genres'].strip('[]\'').split(', '))))
genre_dropdown.pack(pady=10)

# Button to show selected movie
show_button = tk.Button(root, text="Show Movie", command=show_movie)
show_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the main loop
root.mainloop()

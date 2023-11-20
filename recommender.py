# Simple Content-Based Movie Recommendation Prototype
# David Onafuwa, Esrom Tesfay, Ricardo Siles-Herrera
# Sample dataset
data = {
    'Romance': ['The Notebook', 'Titanic', 'Sleepless in Seattle'],
    'Action': ['Die Hard', 'The Terminator', 'Rambo'],
    'Comedy': ['The Hangover', 'Superbad', 'Anchorman'],
    'Pop': ['Shape of You', 'Blinding Lights', 'Happy'],
    'Rock': ['Bohemian Rhapsody', 'Stairway to Heaven', 'Hotel California'],
    'Podcasts': ['The Joe Rogan Experience', 'Serial', 'TED Talks']
}

"""
    Recommends media based on user interests.

    Parameters:
    - interests (list): A list of user interests (e.g., ['Romance', 'Pop', 'Podcasts']).

    Returns:
    - list: A list of recommended media based on the user interests.
"""
def recommend_media(interests):
    recommended_media = []

    for interest in interests:
        if interest in data:
            recommended_media.extend(data[interest])
        else:
            print(f"Genre '{interest}' not found in the dataset.")
    
    return recommended_media

if __name__ == '__main__':
    print("Welcome to the Media Recommender System!")

    # Get user interests
    user_input = input("Enter your interests (comma-separated): ")
    user_interests = [interest.strip() for interest in user_input.split(',')]

    # Get recommendations
    recommendations = recommend_media(user_interests)

    # Display recommendations
    if recommendations:
        print(f"\nRecommended media based on interests: {recommendations}")
    else:
        print("No recommendations found.")

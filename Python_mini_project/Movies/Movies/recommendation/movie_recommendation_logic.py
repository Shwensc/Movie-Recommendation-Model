from .models import Movie
import pandas as pd
from django.core.exceptions import ObjectDoesNotExist

def load_movie_data():
    try:
        # Load movie data from CSV file into Django models
        # Ensure the file path is correct
        movies_df = pd.read_csv(r"C:\Movies\movies_cleaned.csv")
        for _, row in movies_df.iterrows():
            movie = Movie.objects.create(
                movieId=row['movieId'],
                title=row['clean_title'],
                genres=row['genres'],
            )
        print("Data loaded successfully!")
    except Exception as e:
        print("Error loading data:", str(e))

def get_recommendations(movie_name):
    try:
        # Get the movie objects based on the movie name
        movies = Movie.objects.filter(title__iexact=movie_name)
        
        # Handle case where there are multiple movies with the same title
        if len(movies) == 0:
            print("Movie not found:", movie_name)
            return []
        elif len(movies) > 1:
            print("Multiple movies found with the same title:", movie_name)
            # You may want to choose one of the movies or present options to the user
        
        # Select the first movie (or handle multiple matches differently)
        movie = movies[0]
        
        # Perform recommendation logic (e.g., similar genres)
        similar_movies = Movie.objects.filter(genres__icontains=movie.genres).exclude(title__iexact=movie_name)[:5]
        recommendations = [
            {"title": similar_movie.title, "genres": similar_movie.genres}
            for similar_movie in similar_movies
        ]
        return recommendations
    except Exception as e:
        print("Error getting recommendations:", str(e))


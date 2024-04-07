import pandas as pd
import re

# Load movies data
movies = pd.read_csv("movies.csv")

# Function to clean movie titles
def clean_title(title):
    # Remove anything within parentheses (usually the year)
    title = re.sub(r'\([^)]*\)', '', title)
    title = re.sub("[^a-zA-Z0-9 ]", "", title)
    return title.strip()

# Clean movie titles
movies["clean_title"] = movies["title"].apply(clean_title)

# Save modified DataFrame back to the original CSV file
movies.to_csv("movies_cleaned.csv", index=False)

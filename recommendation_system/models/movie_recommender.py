import pandas as pd

movies = pd.read_csv("data/movies.csv")

def get_movies():

    return movies.head(5)
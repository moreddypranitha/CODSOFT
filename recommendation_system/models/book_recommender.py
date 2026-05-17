import pandas as pd

books = pd.read_csv("data/books.csv")

def get_books():

    return books.head(5)
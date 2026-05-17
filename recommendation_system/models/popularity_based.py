def get_popular_items(dataset):

    return dataset.sort_values(
        by='rating',
        ascending=False
    ).head(5)
def search_items(dataset, query):

    query = query.lower()

    return dataset[
        dataset['title']
        .str.lower()
        .str.contains(query)
    ]
def filter_by_category(dataset, category):

    return dataset[
        dataset['category']
        .str.contains(
            category,
            case=False
        )
    ]
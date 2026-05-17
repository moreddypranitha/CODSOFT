import pandas as pd

ratings = pd.read_csv("data/ratings.csv")

def get_collaborative_recommendations(user_id, dataset):

    user_ratings = ratings[
        ratings['userId'] == user_id
    ]

    liked_items = user_ratings[
        user_ratings['rating'] >= 4
    ]

    recommendations = []

    for item_id in liked_items['itemId']:

        similar_users = ratings[
            (ratings['itemId'] == item_id)
            & (ratings['rating'] >= 4)
        ]

        for user in similar_users['userId'].unique():

            if user != user_id:

                user_items = ratings[
                    (ratings['userId'] == user)
                    & (ratings['rating'] >= 4)
                ]

                recommendations.extend(
                    user_items['itemId'].tolist()
                )

    recommendations = list(set(recommendations))

    return dataset[
        dataset['id'].isin(recommendations)
    ].head(5)
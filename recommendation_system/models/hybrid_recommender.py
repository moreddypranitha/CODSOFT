from models.content_based import get_content_recommendations
from models.collaborative_filtering import get_collaborative_recommendations
from models.popularity_based import get_popular_items
import pandas as pd

def hybrid_recommendation(
    dataset,
    item_name,
    user_id
):

    content = get_content_recommendations(
        dataset,
        item_name
    )

    collaborative = get_collaborative_recommendations(
        user_id,
        dataset
    )

    popular = get_popular_items(dataset)

    final = pd.concat([
        content,
        collaborative,
        popular
    ])

    final = final.drop_duplicates()

    return final.head(5)
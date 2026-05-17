from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def get_content_recommendations(dataset, item_name):

    dataset['title'] = dataset['title'].str.strip()

    item_name = item_name.strip()

    tfidf = TfidfVectorizer(stop_words='english')

    tfidf_matrix = tfidf.fit_transform(
        dataset['category']
    )

    cosine_sim = cosine_similarity(tfidf_matrix)

    indices = pd.Series(
        dataset.index,
        index=dataset['title']
    ).drop_duplicates()

    if item_name not in indices:

        return dataset.head(5)

    idx = indices[item_name]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(
        sim_scores,
        key=lambda x: x[1],
        reverse=True
    )

    sim_scores = sim_scores[1:6]

    item_indices = [i[0] for i in sim_scores]

    return dataset.iloc[item_indices]
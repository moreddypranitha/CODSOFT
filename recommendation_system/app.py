from flask import Flask, render_template, request
import pandas as pd

from models.content_based import get_content_recommendations
from models.collaborative_filtering import get_collaborative_recommendations
from models.popularity_based import get_popular_items
from models.hybrid_recommender import hybrid_recommendation

from models.movie_recommender import get_movies
from models.book_recommender import get_books
from models.product_recommender import get_products

from beginner_upgrades.search_system import search_items
from beginner_upgrades.genre_filter import filter_by_category
from beginner_upgrades.ratings_display import get_rating_stars
from beginner_upgrades.poster_loader import get_image_path
from beginner_upgrades.recommendation_history import save_history

app = Flask(__name__)

movies_df = pd.read_csv("data/movies.csv")
books_df = pd.read_csv("data/books.csv")
products_df = pd.read_csv("data/products.csv")

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":

        category = request.form.get("category")
        recommendation_type = request.form.get("recommendation_type")
        selected_item = request.form.get("item")
        user_id = int(request.form.get("user_id"))
        selected_filter = request.form.get("filter")
        search_query = request.form.get("search")

        if category == "movies":
            dataset = movies_df

        elif category == "books":
            dataset = books_df

        else:
            dataset = products_df

        if search_query:

            recommendations = search_items(
                dataset,
                search_query
            )

        else:

            if recommendation_type == "content":

                recommendations = get_content_recommendations(
                    dataset,
                    selected_item
                )

            elif recommendation_type == "collaborative":

                recommendations = get_collaborative_recommendations(
                    user_id,
                    dataset
                )

            elif recommendation_type == "popular":

                recommendations = get_popular_items(
                    dataset
                )

            elif recommendation_type == "hybrid":

                recommendations = hybrid_recommendation(
                    dataset,
                    selected_item,
                    user_id
                )

            if selected_filter:

                recommendations = filter_by_category(
                    recommendations,
                    selected_filter
                )

        recommendations = recommendations.to_dict('records')

        for item in recommendations:

            item['stars'] = get_rating_stars(
                item['rating']
            )

            item['image_path'] = get_image_path(
                item['image']
            )

        save_history(selected_item)

        items_list = dataset['title'].tolist()

    else:

        items_list = movies_df['title'].tolist()

    return render_template(
        "index.html",
        recommendations=recommendations,
        items=items_list
    )

if __name__ == "__main__":
    app.run(debug=True)
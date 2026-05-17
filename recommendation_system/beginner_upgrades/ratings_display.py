def get_rating_stars(rating):

    try:
        rating = float(rating)

    except:
        return "No Rating"

    if rating >= 4.5:
        return "⭐⭐⭐⭐⭐"

    elif rating >= 4.0:
        return "⭐⭐⭐⭐"

    elif rating >= 3.0:
        return "⭐⭐⭐"

    return "⭐⭐"
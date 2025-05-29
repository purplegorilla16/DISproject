from flask import Blueprint, render_template, request, redirect
from models.movie import get_all_movies, add_movie
from models.genre import get_all_genres

movie_bp = Blueprint("movie", __name__)

@movie_bp.route("/movies", methods=["GET", "POST"])
def movies():
    if request.method == "POST":
        title = request.form["title"]
        genre_id = int(request.form["genre_id"])
        rating = int(request.form["rating"])
        add_movie(title, genre_id, rating)
        return redirect("/movies")

    movies = get_all_movies()
    genres = get_all_genres()
    return render_template("movies.html", movies=movies, genres=genres)

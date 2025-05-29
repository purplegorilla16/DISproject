from flask import Blueprint, request, render_template, redirect
from models.todo import get_all_movies, add_movie
from models.category import get_all_genres

movie_bp = Blueprint("movie", __name__)

@movie_bp.route("/movies", methods=["GET", "POST"])
def movies():
    if request.method == "POST":
        title = request.form["title"]
        genre_id = request.form["genre_id"]
        rating = request.form["rating"]
        add_movie(title, genre_id, rating)
        return redirect("/movies")

    movies = get_all_movies()
    genres = get_all_genres()
    return render_template("movies.html", movies=movies, genres=genres)

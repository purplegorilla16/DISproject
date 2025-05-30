from flask import Blueprint, render_template
from models.movie import get_all_movies

movie_bp = Blueprint("movie", __name__)

@movie_bp.route("/browse")
def browse():
    movies = get_all_movies()
    return render_template("browse.html", movies=movies)

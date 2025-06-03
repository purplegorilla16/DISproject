from flask import Blueprint, render_template, request, redirect, make_response
from models.movie import get_all_movies
from models.rating import add_rating, get_user_id, get_all_usernames, create_user
from database import get_connection

movie_bp = Blueprint("movie", __name__)

@movie_bp.route("/", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        if username:
            create_user(username)
            resp = make_response(redirect("/browse"))
            resp.set_cookie("username", username)
            return resp

    users = get_all_usernames()
    return render_template("start.html", users=users)

@movie_bp.route("/browse", methods=["GET", "POST"])
def browse():
    username = request.cookies.get("username")
    if not username:
        return redirect("/")

    user_id = get_user_id(username)
    if not user_id:
        return redirect("/")

    conn = get_connection()
    cur = conn.cursor()

    if request.method == "POST":
        movie_id = int(request.form["movie_id"])
        user_rating = int(request.form["user_rating"])
        user_review = request.form["user_review"]
        add_rating(movie_id, user_rating, user_review, user_id)
        return redirect("/browse")

    query = request.args.get("q", "").strip()
    page = int(request.args.get("page", 1))
    per_page = 20
    offset = (page - 1) * per_page

    if query:
        cur.execute("""
            SELECT id, title, year, rating, runtime
            FROM movies
            WHERE LOWER(title) LIKE ?
            ORDER BY rating DESC
            LIMIT ? OFFSET ?
        """, (f"%{query.lower()}%", per_page, offset))
        movies = cur.fetchall()

        cur.execute("SELECT COUNT(*) FROM movies WHERE LOWER(title) LIKE ?", (f"%{query.lower()}%",))
        total_movies = cur.fetchone()[0]
    else:
        cur.execute("""
            SELECT id, title, year, rating, runtime
            FROM movies
            ORDER BY rating DESC
            LIMIT ? OFFSET ?
        """, (per_page, offset))
        movies = cur.fetchall()

        cur.execute("SELECT COUNT(*) FROM movies")
        total_movies = cur.fetchone()[0]

    total_pages = (total_movies + per_page - 1) // per_page

    cur.execute("""
        SELECT m.title, r.user_rating, r.user_review
        FROM ratings r
        JOIN movies m ON r.movie_id = m.id
        WHERE r.user_id = ?
        ORDER BY r.user_rating DESC
    """, (user_id,))
    rated_movies = cur.fetchall()

    conn.close()
    return render_template("browse.html",
                           movies=movies,
                           rated_movies=rated_movies,
                           current_page=page,
                           total_pages=total_pages,
                           search_query=query)

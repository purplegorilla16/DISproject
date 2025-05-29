from database import get_connection
import sqlite3

def get_all_movies():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT movies.title, genres.genre_name, movies.rating
        FROM movies
        JOIN genres ON movies.genre_id = genres.id
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def add_movie(title, genre_id, rating):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO movies (title, genre_id, rating) VALUES (?, ?, ?)",
            (title, genre_id, rating)
        )
        conn.commit()
        return True  # succes
    except sqlite3.IntegrityError:
        return False  # titel findes allerede
    finally:
        conn.close()

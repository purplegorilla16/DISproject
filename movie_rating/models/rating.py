from database import get_connection

def add_rating(movie_id, user_rating, user_review, username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO ratings (movie_id, user_rating, user_review, username)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(movie_id, username)
        DO UPDATE SET user_rating = excluded.user_rating,
                      user_review = excluded.user_review
    """, (movie_id, user_rating, user_review, username))
    conn.commit()
    conn.close()

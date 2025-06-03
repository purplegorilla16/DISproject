from database import get_connection

def add_rating(movie_id, user_rating, user_review, user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO ratings (movie_id, user_rating, user_review, user_id)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(movie_id, user_id)
        DO UPDATE SET user_rating = excluded.user_rating,
                      user_review = excluded.user_review
    """, (movie_id, user_rating, user_review, user_id))
    conn.commit()
    conn.close()

def get_user_id(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()
    return row["id"] if row else None

def get_all_usernames():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT username FROM users ORDER BY username")
    users = [row["username"] for row in cur.fetchall()]
    conn.close()
    return users

def create_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users (username) VALUES (?)", (username,))
    conn.commit()
    conn.close()

import sqlite3

def get_connection():
    conn = sqlite3.connect('movies.db', timeout=10)
    conn.row_factory = sqlite3.Row
    return conn

def init_ratings():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id INTEGER NOT NULL,
            user_rating INTEGER CHECK(user_rating BETWEEN 1 AND 10),
            user_review TEXT,
            username TEXT NOT NULL,
            UNIQUE (movie_id, username),
            FOREIGN KEY (movie_id) REFERENCES movies(id)
        )
    """)

    conn.commit()
    conn.close()

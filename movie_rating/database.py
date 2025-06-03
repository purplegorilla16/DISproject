import sqlite3

def get_connection():
    conn = sqlite3.connect('movies.db', timeout=10)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Drop eksisterende for testing (kan fjernes i produktion)
    cur.execute("DROP TABLE IF EXISTS ratings")
    cur.execute("DROP TABLE IF EXISTS users")

    cur.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE
        )
    """)

    cur.execute("""
        CREATE TABLE ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            user_rating INTEGER,
            user_review TEXT,
            UNIQUE (movie_id, user_id),
            FOREIGN KEY (movie_id) REFERENCES movies(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()
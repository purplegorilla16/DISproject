import sqlite3

def get_connection():
    conn = sqlite3.connect('movies.db', timeout=10)  # Tilføjet timeout for at undgå "database is locked"
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()

    # Drop tables to reset on each run
    conn.execute('DROP TABLE IF EXISTS movies')
    conn.execute('DROP TABLE IF EXISTS genres')

    # Create genres table
    conn.execute('''
        CREATE TABLE genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            genre_name TEXT NOT NULL UNIQUE
        )
    ''')

    # Create movies table with foreign key to genres
    conn.execute('''
        CREATE TABLE movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            rating INTEGER,
            genre_id INTEGER NOT NULL,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    ''')

    c = conn.cursor()

    # Insert initial genres
    genres = ['Action', 'Drama', 'Comedy']
    for genre in genres:
        c.execute('INSERT OR IGNORE INTO genres (genre_name) VALUES (?)', (genre,))

    # Insert initial movies with NULL ratings
    movies = [
        ('The Dark Knight', 'Action'),
        ('The Godfather', 'Drama'),
        ('Superbad', 'Comedy')
    ]

    for (title, genre_name) in movies:
        c.execute('''
            INSERT OR IGNORE INTO movies (title, rating, genre_id)
            VALUES (?, NULL, (SELECT id FROM genres WHERE genre_name = ?))
        ''', (title, genre_name))

    conn.commit()
    conn.close()

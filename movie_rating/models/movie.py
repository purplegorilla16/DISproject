from database import get_connection

def get_all_movies():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT title, year, rating, runtime
        FROM movies
        ORDER BY rank ASC
        LIMIT 20
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

# midlertidig tom placeholder til gamle afhængigheder
def add_movie(title, genre_id, rating):
    pass

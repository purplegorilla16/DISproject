from database import get_connection

def get_all_genres():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM genres")  # <-- korrekt tabelnavn med 's'
    genres = cur.fetchall()
    conn.close()
    return genres

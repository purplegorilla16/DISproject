import csv
import sqlite3

DB_PATH = "movies.db"
CSV_PATH = "imdb_top_250.csv"

def import_movies():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS movies")
    cur.execute("""
        CREATE TABLE movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rank INTEGER,
            title TEXT NOT NULL,
            year INTEGER,
            rating REAL,
            runtime TEXT
        )
    """)

    with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rank = int(row.get("Rank", 0))
            title = row.get("Title", "Unknown")
            year = int(row.get("Year", 0))
            rating = float(row.get("Rating", 0.0))
            runtime = row.get("Runtime", "Unknown")

            cur.execute("""
                INSERT INTO movies (rank, title, year, rating, runtime)
                VALUES (?, ?, ?, ?, ?)
            """, (rank, title, year, rating, runtime))

    conn.commit()
    conn.close()
    print("✅ Imported movies into database.")

if __name__ == "__main__":
    import_movies()

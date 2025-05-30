import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

# Vis kolonnenavne og datatyper for 'movies'-tabellen
cursor.execute("PRAGMA table_info(movies)")
columns = cursor.fetchall()

print("📋 Kolonner i 'movies':")
for col in columns:
    print(f"- {col[1]} ({col[2]})")

conn.close()

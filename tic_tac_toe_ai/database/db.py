import sqlite3

conn = sqlite3.connect("database/scores.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    result TEXT
)
""")

conn.commit()
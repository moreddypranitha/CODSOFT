import sqlite3

def get_stats():

    conn = sqlite3.connect("database/scores.db")

    cursor = conn.cursor()

    cursor.execute("SELECT result, COUNT(*) FROM scores GROUP BY result")

    data = cursor.fetchall()

    conn.close()

    return data
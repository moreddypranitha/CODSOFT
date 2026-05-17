import sqlite3

def save_result(result):

    conn = sqlite3.connect("database/scores.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO scores(result) VALUES(?)",
        (result,)
    )

    conn.commit()
    conn.close()
# ~/app/db.py

import pathlib
import sqlite3

APP_DIR = pathlib.Path(__file__).resolve().parent
DB_PATH = APP_DIR / "baby.db"


# Connect to db
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
# Create a table
cur.execute("""DROP TABLE IF EXISTS weight_table""")

cur.execute(
    """CREATE TABLE IF NOT EXISTS weight_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                week INTEGER,
                weight REAL);"""
)

# Write changes
conn.commit()
conn.close()


# Populate db
weight_tuple = ((0, 3.486), (1, 3.6), (2, 3.75), (3, 4.2))

# Create a table
with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()
    for entry in weight_tuple:
        cur.execute(
            "INSERT OR IGNORE INTO weight_table (week, weight) VALUES (?,?);" "", entry
        )


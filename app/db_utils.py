# ~/app/db_utils.py

import pathlib
import sqlite3

APP_DIR = pathlib.Path(__file__).resolve().parent
DB_PATH = APP_DIR / "baby.db"


def get_weight_data():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT week, weight FROM weight_table;")
        result = cur.fetchall()
    return result


# if __name__ == "__main__":
#     result = get_weight_data()
#     xx = [result[i][0] for i in range(len(result))]
#     print(xx)

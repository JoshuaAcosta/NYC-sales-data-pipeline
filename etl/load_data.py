"""
Create database in Postgres and loads
csv file containing cleaned data
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def load_data(file):
    """Copies csv file created from dataframe into Postgres """
    conn = psycopg2.connect("host=localhost dbname=transactions user=joshuaacosta")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    with open(file, "r") as f:
        next(f)
        cur.copy_from(f, 'transactions', sep=",")
    conn.close()

if __name__ == "__main__":
    load_data("../data/Clean_NYC_sales_data.csv")

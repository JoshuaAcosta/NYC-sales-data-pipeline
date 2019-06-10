import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_database(dbname):
    
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("DROP DATABASE IF EXISTS " + dbname)
    cur.execute("CREATE DATABASE " + dbname)
    conn.close()

def create_table():
    conn = psycopg2.connect("host=localhost dbname=sales user=postgres")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS transactions")
    cur.execute("""
        CREATE TABLE transactions(
        id INTEGER PRIMARY KEY,
        borough TEXT,
        neighborhood TEXT,
        building_class_category TEXT,
        address TEXT,
        apartment_number TEXT,
        zip_code INTEGER,
        residential_units INTEGER,
        commercial_units INTEGER,
        total_units INTEGER,
        land_square_feet INTEGER,
        gross_square_feet INTEGER,
        year_built INTEGER,
        building_class_at_time_of_sale TEXT,
        sale_price FLOAT,
        sale_date DATE)
        """)

def copy_data(file):
    conn = psycopg2.connect("host=localhost dbname=sales user=postgres")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    with open(file, "r") as f:
        next(f) 
        cur.copy_from(f, 'transactions', sep=",")
    conn.close()

if __name__ == "__main__":
    create_database("sales")
    create_table()
    copy_data("data/Clean_NYC_sales_data.csv")
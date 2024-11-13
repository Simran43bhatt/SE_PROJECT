# backend/database.py
import sqlite3

def create_tables():
    connection = sqlite3.connect('data/billing.db')
    cursor = connection.cursor()

    # User table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT CHECK(role IN ('admin', 'customer')) NOT NULL
    )
    ''')

    # Bills table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        units_consumed INTEGER,
        amount REAL,
        status TEXT CHECK(status IN ('paid', 'unpaid')) NOT NULL,
        due_date TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    ''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()


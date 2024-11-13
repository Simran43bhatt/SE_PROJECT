# backend/user_management.py
import sqlite3
import bcrypt

def register_user(username, password, role):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    connection = sqlite3.connect('data/billing.db')
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed_password, role))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        connection.close()

def login_user(username, password):
    connection = sqlite3.connect('data/billing.db')
    cursor = connection.cursor()
    cursor.execute("SELECT password, role FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    connection.close()

    if user and bcrypt.checkpw(password.encode(), user[0]):
        return user[1]  # Return role if successful
    return None


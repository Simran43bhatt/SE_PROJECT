# backend/billing.py
import sqlite3

TARIFF_RATE = 5.0  # Price per unit

def calculate_bill(units):
    return units * TARIFF_RATE

def generate_bill(user_id, units, due_date):
    amount = calculate_bill(units)
    connection = sqlite3.connect('data/billing.db')
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO bills (user_id, units_consumed, amount, status, due_date) VALUES (?, ?, ?, 'unpaid', ?)",
                   (user_id, units, amount, due_date))
    connection.commit()
    connection.close()

def pay_bill(bill_id):
    connection = sqlite3.connect('data/billing.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE bills SET status = 'paid' WHERE id = ?", (bill_id,))
    connection.commit()
    connection.close()


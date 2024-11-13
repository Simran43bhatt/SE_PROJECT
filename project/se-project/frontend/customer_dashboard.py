# frontend/customer_dashboard.py
import tkinter as tk
from backend import billing

def view_bills():
    # This function would normally retrieve the bills from the database for the logged-in customer
    # For demonstration, it uses dummy data
    bills = [(1, 200, "unpaid", "2024-11-30"), (2, 150, "paid", "2024-10-30")]
    for bill in bills:
        listbox.insert(tk.END, f"Bill ID: {bill[0]}, Amount: {bill[1]}, Status: {bill[2]}, Due Date: {bill[3]}")

app = tk.Tk()
app.title("Electricity Billing System - Customer Dashboard")

tk.Label(app, text="Your Bills").pack()
listbox = tk.Listbox(app, width=50, height=10)
listbox.pack()

view_bills_button = tk.Button(app, text="View Bills", command=view_bills)
view_bills_button.pack()

app.mainloop()


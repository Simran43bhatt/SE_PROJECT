# frontend/bill_calculation.py
import tkinter as tk
from tkinter import messagebox
from backend import billing

def calculate():
    try:
        units = int(units_entry.get())
        amount = billing.calculate_bill(units)
        messagebox.showinfo("Bill Amount", f"Your bill amount is: {amount}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of units.")

app = tk.Tk()
app.title("Electricity Billing System - Bill Calculation")

tk.Label(app, text="Enter Units Consumed").pack()
units_entry = tk.Entry(app)
units_entry.pack()

calculate_button = tk.Button(app, text="Calculate Bill", command=calculate)
calculate_button.pack()

app.mainloop()


# frontend/payment.py
import tkinter as tk
from tkinter import messagebox
from backend import billing

def pay_bill():
    try:
        bill_id = int(bill_id_entry.get())
        billing.pay_bill(bill_id)
        messagebox.showinfo("Payment Successful", "Your bill has been paid.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid Bill ID.")

app = tk.Tk()
app.title("Electricity Billing System - Pay Bill")

tk.Label(app, text="Enter Bill ID").pack()
bill_id_entry = tk.Entry(app)
bill_id_entry.pack()

pay_button = tk.Button(app, text="Pay Bill", command=pay_bill)
pay_button.pack()

app.mainloop()

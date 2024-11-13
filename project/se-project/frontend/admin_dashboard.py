# frontend/admin_dashboard.py
import tkinter as tk
from tkinter import messagebox
from backend import billing, notifications

class AdminDashboard:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Admin Dashboard")
        self.root.geometry("500x400")
        self.root.configure(bg="#D3E4CD")

        tk.Label(self.root, text="Admin Dashboard", font=("Arial", 18, "bold"), bg="#D3E4CD").pack(pady=20)

        tk.Label(self.root, text="Unpaid Bills", font=("Arial", 14), bg="#D3E4CD").pack()
        self.listbox = tk.Listbox(self.root, width=60, height=10, font=("Arial", 12))
        self.listbox.pack(pady=10)

        tk.Button(self.root, text="View Unpaid Bills", command=self.view_unpaid_bills, bg="#91C788", font=("Arial", 12)).pack(pady=10)

        tk.Label(self.root, text="Send Payment Reminder (Enter Bill ID)", font=("Arial", 12), bg="#D3E4CD").pack(pady=10)
        self.bill_id_entry = tk.Entry(self.root, font=("Arial", 12))
        self.bill_id_entry.pack()

        tk.Button(self.root, text="Send Reminder", command=self.send_reminder, bg="#91C788", font=("Arial", 12)).pack(pady=10)

    def view_unpaid_bills(self):
        unpaid_bills = [(1, "John Doe", 100, "2024-11-30"), (2, "Jane Doe", 150, "2024-12-15")]
        self.listbox.delete(0, tk.END)
        for bill in unpaid_bills:
            self.listbox.insert(tk.END, f"Bill ID: {bill[0]}, Customer: {bill[1]}, Amount: {bill[2]}, Due Date: {bill[3]}")

    def send_reminder(self):
        bill_id = self.bill_id_entry.get()
        email = "customer@example.com"
        amount = 100
        due_date = "2024-11-30"
        
        notifications.send_payment_reminder(email, amount, due_date)
        messagebox.showinfo("Reminder Sent", f"Payment reminder sent to {email}.")



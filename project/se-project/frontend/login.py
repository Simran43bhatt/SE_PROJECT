# frontend/login.py
import tkinter as tk
from tkinter import messagebox
from backend import user_management

class LoginFrame:
    def __init__(self, root, app):
        self.app = app
        self.root = tk.Toplevel(root)
        self.root.title("Login - Electricity Billing System")
        self.root.geometry("400x400")
        self.root.protocol("WM_DELETE_WINDOW", root.quit)  # Close main app when login window is closed

        # Create Frame for Login
        self.frame = tk.Frame(self.root, bg="#D3E4CD", padx=20, pady=20)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Electricity Billing System", font=("Arial", 18, "bold"), bg="#D3E4CD").grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # Username
        tk.Label(self.frame, text="Username:", font=("Arial", 12), bg="#D3E4CD").grid(row=1, column=0, sticky="w")
        self.username_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.username_entry.grid(row=1, column=1, pady=5)

        # Password
        tk.Label(self.frame, text="Password:", font=("Arial", 12), bg="#D3E4CD").grid(row=2, column=0, sticky="w")
        self.password_entry = tk.Entry(self.frame, show="*", font=("Arial", 12))
        self.password_entry.grid(row=2, column=1, pady=5)

        # Role Selection
        self.role_var = tk.StringVar(value="customer")
        tk.Radiobutton(self.frame, text="Customer", variable=self.role_var, value="customer", font=("Arial", 12), bg="#D3E4CD").grid(row=3, column=0, pady=10)
        tk.Radiobutton(self.frame, text="Admin", variable=self.role_var, value="admin", font=("Arial", 12), bg="#D3E4CD").grid(row=3, column=1, pady=10)

        # Buttons
        tk.Button(self.frame, text="Login", font=("Arial", 12), command=self.login, bg="#91C788", width=10).grid(row=4, column=0, pady=20)
        tk.Button(self.frame, text="Register", font=("Arial", 12), command=self.register, bg="#91C788", width=10).grid(row=4, column=1, pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = user_management.login_user(username, password)
        
        if role:
            messagebox.showinfo("Login Successful", f"Welcome, {role}")
            self.root.destroy()  # Close the login window
            
            # Navigate to the appropriate dashboard based on role
            if role == "admin":
                self.app.open_admin_dashboard()
            elif role == "customer":
                self.app.open_customer_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()

        if user_management.register_user(username, password, role):
            messagebox.showinfo("Registration Successful", "You can now log in.")
        else:
            messagebox.showerror("Registration Failed", "Username already exists.")







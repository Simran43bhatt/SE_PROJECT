# app.py
import tkinter as tk
from frontend import login, admin_dashboard, customer_dashboard
from backend.database import create_tables

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Electricity Billing System")
        self.root.geometry("400x300")
        
        create_tables()  # Ensure database tables are created
        self.show_login()  # Start with login screen

    def show_login(self):
        login.LoginFrame(self.root, self)

    def open_admin_dashboard(self):
        admin_dashboard.AdminDashboard(self.root)

    def open_customer_dashboard(self):
        customer_dashboard.CustomerDashboard(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()




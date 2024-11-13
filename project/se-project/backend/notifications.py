# backend/notifications.py
import smtplib
from email.mime.text import MIMEText

def send_email(recipient, subject, body):
    sender = "youremail@example.com"
    password = "yourpassword"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())

def send_payment_reminder(email, amount, due_date):
    subject = "Electricity Bill Payment Reminder"
    body = f"Your bill of {amount} is due on {due_date}. Please pay it on time to avoid late fees."
    send_email(email, subject, body)

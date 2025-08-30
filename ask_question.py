#!/usr/bin/env python3
"""
Module to send one time code for 2FA
"""
import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()

def send_email(to_email, name, phone_number, message):
    """
    Sends a one-time password (OTP) to the specified email address.
    """
    sender_email = os.getenv("SENDER_EMAIL")
    print(sender_email)
    sender_app_password = os.getenv("SENDER_APP_PASSWORD")
    print(sender_app_password)
    if not sender_email or not sender_app_password:
        raise ValueError("Email credentials are not set in the environment variables.")
    msg = MIMEText(f"{message}\n{phone_number}\n{to_email}")
    msg["Subject"] = f"I want to connect-{name}"
    msg["From"] = sender_email
    msg["To"] = to_email

    # connect to the SMTP server and send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_app_password)
        server.sendmail(sender_email, to_email, msg.as_string())

if __name__ == "__main__":
    send_email(to_email, phone_number, message)

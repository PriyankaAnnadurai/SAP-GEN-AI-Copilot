import smtplib
from email.message import EmailMessage


def send_email_alert(subject, content, to="receiver@example.com"):
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = "your-email@gmail.com"
    msg['To'] = to

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("your-email@gmail.com", "your-app-password")
        smtp.send_message(msg)

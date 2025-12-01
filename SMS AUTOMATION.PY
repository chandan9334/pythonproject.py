import smtplib
import ssl
from email.message import EmailMessage

EMAIL = "chandanpatel9334@gmail.com"
APP_PASSWORD ="" 
RECEIVER = "rohitmittal7889@gmail.com"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"]= RECEIVER
msg["Subject"] = "your father is here......"

msg.set_content("hlo beta how is your college going....")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)

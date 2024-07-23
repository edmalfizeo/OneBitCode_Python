from email.message import EmailMessage
import smtplib
import ssl
import os

password = os.environ.get('SENHA_EMAIL_PYTHON')
from_email = os.environ.get('EMAIL_PYTHON')
to_email = os.environ.get('EMAIL_PYTHON')
subject = 'Curiosidades e Lembretes Diários'
body = open('email_content.txt', 'r', encoding='utf-8').read()

# 1 - Create the email
msg = EmailMessage()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.set_content(body)
safe = ssl.create_default_context()

# 2 - Send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as server:
    server.login(from_email, password)
    server.sendmail(
        from_email,
        to_email,
        msg.as_string()
    )

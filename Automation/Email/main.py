from email.message import EmailMessage
import smtplib
import ssl
import os

password = os.getenv('SENHA_EMAIL_PYTHON')
from_email = os.getenv('EMAIL_PYTHON')
to_email = os.getenv('EMAIL_PYTHON')
subject = 'Testing automation email'

body = '''
Hello, this is a test email sent from Python.
This is so cool!
'''

# 1 - Create the email message
msg = EmailMessage()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.set_content(body)
safe = ssl.create_default_context()

# 2 - Sending the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as server:
    server.login(from_email, password)
    server.sendmail(
        from_email,
        to_email,
        msg.as_string()
    )
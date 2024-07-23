from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes

password = os.environ.get('SENHA_EMAIL_PYTHON')
from_email = os.environ.get('EMAIL_PYTHON')
to_email = os.environ.get('EMAIL_PYTHON')
subject = 'Informes BB - Python'
body = open('emai_bb.txt', 'r', encoding='utf-8').read()

msg = EmailMessage()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

msg.set_content(body)
safe = ssl.create_default_context()

# Adding Attachment
attachment_path = 'C:/Users/dudum/OneDrive/Documents/OneBitCode_Python/Automation/Actions/bb.png'
mime_type, mime_subtype = mimetypes.guess_type(attachment_path)[0].split('/')
with open(attachment_path, 'rb') as file:
    msg.add_attachment(
        file.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=file.name
    )

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        msg.as_string()
    )
    print('Email enviado com sucesso!')

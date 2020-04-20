import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Mohammed Amr'
email['to'] = 'spring.test.mail.server@gmail.com'
email['subject'] = 'Note to self!'

email.set_content(html.substitute({'name': 'Mohammed'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('smtp.test.mail.server1@gmail.com', 'Pass@12345')
    smtp.send_message(email)
    print('all good boss!')

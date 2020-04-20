import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Mohammed Amr'
email['to'] = 'spring.test.mail.server@gmail.com'
email['subject'] = 'You won the lottery!'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('smtp.test.mail.server1@gmail.com', 'Pass@12345')
    smtp.send_message(email)
    print('all good boss!')

# coding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


email_adress = "@gmail.com"
email_password = ""
email_receiver = '@gmail.com'

msg = MIMEMultipart()
msg['From'] =  email_adress
msg['To'] = email_receiver
msg['Subject'] = 'Le sujet de mon mail' 
message = 'Bonjour !'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login(email_adress, email_password)
mailserver.sendmail(email_adress ,email_receiver, msg.as_string())
mailserver.quit()
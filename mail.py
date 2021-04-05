# coding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendmail(email_receiver, Subject, message):
    email_adress = "@@gmail.com"
    email_password = "g"

    msg = MIMEMultipart()
    msg['From'] =  email_adress
    msg['To'] = email_receiver
    msg['Subject'] = Subject 

    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(email_adress, email_password)
    mailserver.sendmail(email_adress ,email_receiver, msg.as_string())
    mailserver.quit()

sendmail("pgmendormi@gmail.com", "Sujet", "comment tu vas mon ptit pote")
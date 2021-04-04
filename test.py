import smtplib, ssl

# on rentre les renseignements pris sur le site du fournisseur
smtp_adress = 'smtp.gmail.com'
smtp_port = 465

# on rentre les informations sur notre adresse e-mail
email_adress = "bestgaraneuw@gmail.com"
email_password = "guiguidu94"

# on rentre les informations sur le destinataire
email_receiver = 'pgmendormi@gmail.com'

# on crée la connexion
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_adress, smtp_port, context=context) as server:
  # connexion au compte
  server.login(email_adress, email_password)
  # envoi du mail
  server.sendmail(email_adress, email_receiver, 'le contenu de l\'e-mail')
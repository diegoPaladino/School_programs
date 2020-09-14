#setransp_email_send_2
#based in the tutorial:How To Send an Email in Python With Attachments Easy for Beginners
#link of tutorial: https://www.youtube.com/watch?v=bXRYJEKjqIM&t=287s

#import libraries
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#declarations
email_user = 'diegopaladinoemfrc@gmail.com'
email_send = 'diegopaladinofoto@gmail.com'
password = 'paladino804680'
subject = 'Python'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Setransp-Agosto'
msg.attach(MIMEText(body,'plain'))
text = msg.as_string()

#executing the code

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,password)
# server.password(password)

server.sendmail(email_user,email_send,text)
print('email enviado com sucesso',datetime.now())


server.quit()
#setransp_email_send_2
#based in the tutorial:How To Send an Email in Python With Attachments Easy for Beginners
#link of tutorial: https://www.youtube.com/watch?v=bXRYJEKjqIM&t=287s

#import libraries
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#declarations
email_user = 'diegopaladinoemfrc@gmail.com'
email_send = 'emfrafael@gmail.com'
password = 'paladino804680'
subject = 'Python_bot'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

#executing the code
body = 'Setransp-Agosto'
msg.attach(MIMEText(body,'plain'))

filename = 'SETRANSP-AGOSTO.txt'
attachment = open(filename,'rb')

part = MIMEBase('aplication','octet-sream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,password)


server.sendmail(email_user,email_send,text)
print('email enviado com sucesso',datetime.now())
server.quit()
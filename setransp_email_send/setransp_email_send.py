#setransp_email_send
#was unsucessfull

#import libraries
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


#declaretes
#dates of email:
email_login = 'diegopaladinoemfrc@gmail.com'
senha = 'paladino804680'

msg = MIMEMultipart()

msg['From'] = email_login
msg['To'] = senha
msg['Subject'] = "Setransp-Agosto"

body = 'Setransp-Agosoto'
msg.attach(MIMEText(body))

filename = 'SETRANSP-AGOSTO.txt'
attachment = open(filename)

#https://www.freeformatter.com/mime-types-list.html
mimetypes_anexo = mimetypes.guess_type(filename)[0].split('/')
part = MIMEBase(mimetypes_anexo[0],mimetypes_anexo[1])

part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition',"attachment; filename = %s",%filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com','587')
server.starttls()
server.login(email_login, open('senha.txt').read().strip())
text = msg.as_string()
server.sendmail(email_login,senha,text)
server.quit()

#execution
# program this to execute every month





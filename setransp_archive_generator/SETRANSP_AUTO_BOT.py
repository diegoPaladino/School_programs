#SETRANSP_AUTO_BOT
#This bot has access of Gemul(the school County plataform), save the document and after that sends to specific email
#checkbox tutorial: Python tkinter | Open Notepad on Button Click | https://www.youtube.com/watch?v=nz-jZ-9k3Dw
#opening notepad: Python tkinter | Open Notepad on Button Click | https://www.youtube.com/watch?v=Qe75weKk8e8


#importing the libs
import pyautogui as p
import time as t
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import winsound
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import schedule
import os
import tkinter as tk
# TOTAL: 13 libs


#defining the functions
def envio_email_setransp():
    sender_email= "diegopaladinoemfrc@gmail.com"
    # rec_email="emfrafael@gmail.com"
    rec_email="diegopaladinofoto@gmail.com"
    password='Paladio804680'
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email, password)

    subject = 'FREQUENCIA_SETRANSP'
    body = 'ANEXO'

    msg = f'Subject: {subject}\n\n{body}'

    print("Login succes")
    server.sendmail(sender_email,rec_email,msg)
    print("Email has sent to",rec_email)

envio_email_setransp()


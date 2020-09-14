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
    password='paladino804680'
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email, password)

    subject = 'FREQUENCIA_SETRANSP'
    body = 'ANEXO'

    msg = f'Subject: {subject}\n\n{body}'

    print("Login succes")
    server.sendmail(sender_email,rec_email,msg)
    print("Email has sent to",rec_email)

#searching the executable of selenium webdriver
operadriver='C://Users//diego//OneDrive//Desktop//DESKTOP//PROGRAMAS//MOZILA//geckodriver.exe'
driver = webdriver.Firefox()

#requesting the opening of a page
driver.get('http://www.gemul.com.br/')
driver.set_window_position(166,-700)
driver.maximize_window()

#clicking in the "LOGIN" botton
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/ul/li[2]/a/img').click()
driver.find_element_by_xpath('//*[@id="frm"]/div/p/strong[3]/a').click()

#selecting the "Username" box and writing the username to make login
username = driver.find_element_by_xpath('//*[@id="txtLogin"]')
username.send_keys('DIEGO.CSF')
#selecting the "Password" box and writing the pasword to make login
password = driver.find_element_by_xpath('//*[@id="txtSenha"]')
password.send_keys('GMLPALADINO')
p.hotkey('tab','enter')

#selecting the "Academico" module
driver.find_element_by_xpath('/html/body/div[1]/form/div/div[2]/div[2]/div[2]/div[1]/div/div/div/a/img').click()

#selecting the "Manutenção" tab and clicking in the "Setransp" archive generator
# p.keyDown('ctrl')
# p.hotkey('t')
# p.keyUp('ctrl')

#writing the link of the setransp archive generator
# p.write('http://www.gemul-aparecida.com.br/gemul2015/Sistema/SCA/GeraArquivoSetransp_con.asp')
# p.hotkey('enter')
# t.sleep(2)

#clicking in the checkbox "Gerar Arquivo"
p.moveTo(211,-671)
t.sleep(0.5)
p.moveTo(195,-278)
t.sleep(0.5)
p.click()

#checking the box "Gerar Arquivo"
checkboxes=[]
checkboxes=driver.find_elements_by_name('optOpcao')
checkboxes[1].click()

#saving the archive
p.moveTo(-96,-402)
p.click()
t.sleep(1)

#clicking in the .txt archive to open the text
driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[1]/td/a/strong').click()

#clicking in the text
p.moveTo(181,-704)
p.click()

#opening the notepad
# os.system('cmd /c notepad')
# t.sleep(1)
# parentwindow.mainloop()
p.hotkey('win')
t.sleep(1)
p.write('notepad')
t.sleep(1)
p.hotkey('enter')
t.sleep(1)

#copying the text of the Gemul plataform with all the informations of the students
    #selecting the Chrome window
p.keyDown('alt')
p.hotkey('tab')
p.keyUp('alt')
    #selecting the text and copying
p.keyDown('ctrl')
p.hotkey('a')
p.keyUp('ctrl')
p.keyDown('ctrl')
p.hotkey('c')
p.keyUp('ctrl')

#pasting the contenius
p.keyDown('alt')
p.hotkey('tab')
p.keyUp('alt')
p.keyDown('ctrl')
p.hotkey('v')
p.keyUp('ctrl')
p.keyDown('ctrl')
p.hotkey('s')
p.keyUp('ctrl')

#saving the .txt
p.write('SETRANSP')
t.sleep(0.5)

#copying the link of folder the file is in
p.keyDown('ctrl')
p.hotkey('l')
p.keyUp('ctrl')
p.write('Documentos',interval=0.5)
p.hotkey('enter')

#using the tkinter to copy date of birth to "c" variable
# root = tk.Tk()
# root.withdraw()
# a=root.clipboard_get()
# t.sleep(0.5)

# #pressing the 'save' button
p.press('tab', presses=10)
p.hotkey('enter')

#closing the notepad window
p.hotkey('ctrl','w')


#in this momment the archive is saved, now is the process of the send to email.


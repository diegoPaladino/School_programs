#SETRANSP_AUTOBOT_202009102025

#import libs:
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
import subprocess
import tkinter as tk
from datetime import datetime
# TOTAL: 13 libs


#definitions of functions:

def mes_atual():
    mes = datetime.now().month

print(mes_atual)

# def escrever_mes_atual():
#     if (mes_atual == 1):
#         p.write('SETRANSP_DEZEMBRO')
#     if (mes_atual == 2):
#         p.write('SETRANSP_JANEIRO') 
#     if (mes_atual == 3):
#         p.write('SETRANSP_FEVEREIRO')
#     if (mes_atual == 4):
#         p.write('SETRANSP_MARCO')
#     if (mes_atual == 5):
#         p.write('SETRANSP_ABRIL')
#     if (mes_atual == 6):
#         p.write('SETRANSP_MAIO')
#     if (mes_atual == 7):
#         p.write('SETRANSP_JUNHO')
#     if (mes_atual == 8):
#         p.write('SETRANSP_JULHO')
#     if (mes_atual == 9):
#         p.write('SETRANSP_AGOSTO')
#     if (mes_atual == 10):
#         p.write('SETRANSP_SETEMBRO')
#     if (mes_atual == 11):
#         p.write('SETRANSP_OUTUBRO')
#     if (mes_atual == 12):
#         p.write('SETRANSP_NOVEMBRO')


#code of archive generator
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
t.sleep(2)

    #selecting the "Academico" module
p.moveTo(288,-202,duration=0.2)
p.click()
t.sleep(2)

    #selecting the "Manutenção"
p.moveTo(329,-711,duration=0.2)
p.click()
t.sleep(0.3)

    #selecting the "Setransp"
p.moveTo(329,-326,duration=0.2)
p.click()
t.sleep(0.3)

    #selecting the "Gerar Arquivo" check box
p.moveTo(178,-634,duration=0.2)
p.click()
t.sleep(0.3)

    #selecting the "ou Arquivo" to generate the archive
p.moveTo(33,-444,duration=0.2)
p.click()
t.sleep(0.3)

    #clicking in the "SETRANSP" to open the txt in the screen
p.moveTo(721,-525,duration=0.2)
p.click()
t.sleep(1)

    #Copyng the txt archive on the screen
p.moveTo(721,-525,duration=0.2)
p.click()
t.sleep(0.3)
p.hotkey('ctrl','a')
t.sleep(0.3)
p.hotkey('ctrl','c')
t.sleep(0.3)

    #pasting in the notepad
    #opening the notepad
subprocess.Popen(["notepad"])
t.sleep(0.3)
    #copying the transfer area data
p.hotkey('ctrl','v')
t.sleep(0.3)
    #saving the notepad
p.hotkey('ctrl','s')
t.sleep(1)
# escrever_mes_atual()
p.write('SETRANSP-AGOSTO')
p.press('tab',presses=7,interval=0.1)
p.hotkey('enter')
p.write(r'C:\Users\diego\OneDrive\Desktop\DESKTOP\DATA_SCIENCE\PYTHON\SETRANSP_AUTO_BOT',interval=0.01)
p.hotkey('enter')
#moving the cursor to 'save' button
p.press('tab',presses=7,interval=0.1)
p.hotkey('enter')

#closing the notebook and the mozila window:
p.hotkey('ctrl','w')
t.sleep(0.2)
p.moveTo(1416,-882)
p.click()


#send email have be in a diferent program. OK.
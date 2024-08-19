import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pyautogui as p
import time as t
import clipboard as c
import pyperclip as pp
import tkinter as tk #recurso para criação de interface IHM
from tkinter import simpledialog
import os



# DECLARAÇÕES DE BIBLIOTECAS
def abrir_nova_aba():
    p.keyDown('ctrl')
    t.sleep(0.2)
    p.hotkey('t')
    t.sleep(0.3)
    p.keyUp('ctrl')
    t.sleep(0.2)
def ctrl_pageup():
    p.keyDown('ctrl')
    t.sleep(0.2)
    p.hotkey('pageup')
    t.sleep(0.3)
    p.keyUp('ctrl')
    t.sleep(0.2)
def ctrl_pagedown():
    p.keyDown('ctrl')
    t.sleep(0.2)
    p.hotkey('pagedown')
    t.sleep(0.3)
    p.keyUp('ctrl')
    t.sleep(0.2)
def pageup():
    p.hotkey('pageup')
    t.sleep(0.3)
def pagedown():
    p.hotkey('pagedown')
    t.sleep(0.3)
def procurar():
    p.keyDown('ctrl')
    t.sleep(0.2)
    p.hotkey('f')
    t.sleep(0.3)
    p.keyUp('ctrl')
    t.sleep(0.2)
def copiar():
    p.keyDown('ctrl')
    t.sleep(0.2)
    p.hotkey('c')
    t.sleep(0.3)
    p.keyUp('ctrl')
    t.sleep(0.2)
def colar():
    p.keyDown('ctrl')
    t.sleep(0.2)
    p.hotkey('v')
    t.sleep(0.3)
    p.keyUp('ctrl')
    t.sleep(0.2)
def enter():
    p.press('enter')
    t.sleep(0.3)
def tab():
    p.press('tab')
    t.sleep(0.3)
def alt():
    p.press('tab')
    t.sleep(0.3)
def alt_tab():
    p.keyDown('alt')
    t.sleep(0.2)
    p.hotkey('tab')
    t.sleep(0.3)
    p.keyUp('alt')
    t.sleep(0.2)
def alt_tab_tab():
    p.keyDown('alt')
    t.sleep(0.2)
    p.hotkey('tab')
    t.sleep(0.2)
    p.hotkey('tab')
    t.sleep(0.3)
    p.keyUp('alt')
    t.sleep(0.2)
def alt_tab_tab_tab():
    p.keyDown('alt')
    t.sleep(0.2)
    p.hotkey('tab')
    t.sleep(0.2)
    p.hotkey('tab')
    t.sleep(0.2)
    p.hotkey('tab')
    t.sleep(0.3)
    p.keyUp('alt')
    t.sleep(0.2)
def imprimir():
    p.keyDown('ctrl')
    t.sleep(0.2)
    p.hotkey('p')
    t.sleep(0.3)
    p.keyUp('ctrl')
    t.sleep(0.2)
def enter():
    p.keyDown('enter')
    t.sleep(0.2)
    p.keyUp('enter')
    t.sleep(0.2)
def down():
    p.keyDown('down')
    t.sleep(0.2)
    p.keyUp('down')
    t.sleep(0.2)
def esc():
    p.hotkey('esc')
    t.sleep(0.3)
def right():
    p.hotkey('right')
    t.sleep(0.2)
def left():
    p.hotkey('left')
    t.sleep(0.2)
def up():
    p.hotkey('up')
    t.sleep(0.2)
def down():
    p.hotkey('down')
    t.sleep(0.2)
def click():
    p.click()
    t.sleep(0.2)
def end():
    p.hotkey('end')
    t.sleep(0.2)




# Caminho para o executável do ChromeDriver
chrome_driver_path = "C:\\Users\\diego\\Desktop\\001-Desktop\\programas\\ChromeDriver\\chromedriver.exe"

# Opções do Chrome
options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Serviço do ChromeDriver
service = Service(executable_path=chrome_driver_path)

# Inicializa o navegador Chrome
driver = webdriver.Chrome(service=service, options=options)

# Maximiza a janela do navegador
driver.maximize_window()

# Abre a página de login
driver.get("https://www.gemul-aparecida.com.br/login.asp")

# Localiza o campo de usuário e insere o nome de usuário
username_field = driver.find_element(By.XPATH, '//*[@id="txtLogin"]')
username_field.send_keys("DIEGO.CSF")

# Localiza o campo de senha e insere a senha
password_field = driver.find_element(By.XPATH, '//*[@id="txtSenha"]')
password_field.send_keys("GMLPALADINO")

# Localiza o botão de login e clica nele
login_button = driver.find_element(By.XPATH, '//*[@id="frm"]/div[4]/div[2]/a')
login_button.click()

# Pausa a execução para manter a janela aberta
input("Pressione Enter para fechar o navegador...")

'''
EXPLICAÇÕES DO PROGRAMA
1. Arquivo Excel (ELENCO AUTOMÁTICO 2024 - VESPERTINO-(...)) deve estar aberto 
2. 



'''


# Bibliotecas
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, NoAlertPresentException
import pyautogui as p
import clipboard as c
import pyperclip as pp
import tkinter as tk
from tkinter import simpledialog, ttk
import os

# Início da contagem do tempo
start_time = time.time()  # Início do cronômetro

# Funções de automação de teclado e mouse
def abrir_nova_aba():
    p.keyDown('ctrl')
    time.sleep(0.2)
    p.hotkey('t')
    time.sleep(0.3)
    p.keyUp('ctrl')
    time.sleep(0.2)

def ctrl_pageup():
    p.keyDown('ctrl')
    time.sleep(0.2)
    p.hotkey('pageup')
    time.sleep(0.3)
    p.keyUp('ctrl')
    time.sleep(0.2)

def ctrl_pagedown():
    p.keyDown('ctrl')
    time.sleep(0.2)
    p.hotkey('pagedown')
    time.sleep(0.3)
    p.keyUp('ctrl')
    time.sleep(0.2)

def pageup():
    p.hotkey('pageup')
    time.sleep(0.3)

def pagedown():
    p.hotkey('pagedown')
    time.sleep(0.3)

def procurar():
    p.keyDown('ctrl')
    time.sleep(0.2)
    p.hotkey('f')
    time.sleep(0.3)
    p.keyUp('ctrl')
    time.sleep(0.2)

def copiar():
    p.keyDown('ctrl')
    time.sleep(0.2)
    p.hotkey('c')
    time.sleep(0.3)
    p.keyUp('ctrl')
    time.sleep(0.2)

def colar():
    p.keyDown('ctrl')
    time.sleep(0.2)
    p.hotkey('v')
    time.sleep(0.3)
    p.keyUp('ctrl')
    time.sleep(0.2)

def enter():
    p.press('enter')
    time.sleep(0.3)

def tab():
    p.press('tab')
    time.sleep(0.3)

def alt():
    p.press('tab')
    time.sleep(0.3)

def alt_tab():
    p.keyDown('alt')
    time.sleep(0.2)
    p.hotkey('tab')
    time.sleep(0.3)
    p.keyUp('alt')
    time.sleep(0.2)

def alt_tab_tab():
    p.keyDown('alt')
    time.sleep(0.2)
    p.hotkey('tab')
    time.sleep(0.2)
    p.hotkey('tab')
    time.sleep(0.3)
    p.keyUp('alt')
    time.sleep(0.2)

def alt_tab_tab_tab():
    p.keyDown('alt')
    time.sleep(0.2)
    p.hotkey('tab')
    time.sleep(0.2)
    p.hotkey('tab')
    time.sleep(0.2)
    p.hotkey('tab')
    time.sleep(0.3)
    p.keyUp('alt')
    time.sleep(0.2)

def imprimir():
    p.keyDown('ctrl')
    time.sleep(0.2)
    p.hotkey('p')
    time.sleep(0.3)
    p.keyUp('ctrl')
    time.sleep(0.2)

def enter():
    p.keyDown('enter')
    time.sleep(0.2)
    p.keyUp('enter')
    time.sleep(0.2)

def down():
    p.keyDown('down')
    time.sleep(0.2)
    p.keyUp('down')
    time.sleep(0.2)

def esc():
    p.hotkey('esc')
    time.sleep(0.3)

def right():
    p.hotkey('right')
    time.sleep(0.2)

def left():
    p.hotkey('left')
    time.sleep(0.2)

def up():
    p.hotkey('up')
    time.sleep(0.2)

def down():
    p.hotkey('down')
    time.sleep(0.2)

def click():
    p.click()
    time.sleep(0.2)

def end():
    p.hotkey('end')
    time.sleep(0.2)











# Término da contagem do tempo
end_time = time.time()  # Fim do cronômetro
elapsed_time = end_time - start_time
minutes, seconds = divmod(elapsed_time, 60)
milliseconds = (elapsed_time - int(elapsed_time)) * 1000
print(f"Tempo decorrido: {int(minutes):02}:{int(seconds):02}.{int(milliseconds):03}")
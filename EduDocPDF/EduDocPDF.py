
'''
ESTE PROGRAMA FOI CRIADO PARA SALVAR EM PDF NA PASTA ESPECIFICADA OS ARQUIVOS REFERENTES AS FICHAS DESCRITIVAS DOS ALUNOS
preparo:
1. EXCEL preparado aberto (FICHAS_DESCRITIVAS-CONFERENCIA_AUTOMATIZADA)
2. NAVEGADOR aberta já na lista de ficha descritiva
3. ter salvo ao menos uma única ficha como PDF, para haver memorização da atual impressora

'''



import os
import json
import pyautogui as p
import time as t
import clipboard as c
import pyperclip as pp
import tkinter as tk #recurso para criação de interface IHM
from tkinter import simpledialog
from tkinter import messagebox  # Importar messagebox especificamente
import keyboard
import winsound



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
    t.sleep(0.2)
    p.keyUp('alt')
    t.sleep(0.2)
def down():
    p.press('down')
    t.sleep(0.3)
def copy():
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
def ctrl_w():
    p.keyDown('ctrl')
    t.sleep(0.2)
    p.hotkey('w')
    t.sleep(0.3)
    p.keyUp('ctrl')
    t.sleep(0.2)
def get_and_click_mouse_position():
    root = tk.Tk()
    root.withdraw()
    clipboard_content = pp.paste()  # Obtém o conteúdo do clipboard
    # alerta sonoro para clicar manualmente
    winsound.Beep(500, 200)  # Toca um beep de 1000 Hz por 1 segundo
    # Mostra uma messagebox com o conteúdo do clipboard
    messagebox.showinfo("Instrução", f"Posicione o mouse no local desejado e pressione OK.\nConteúdo do Clipboard: {clipboard_content}")
    x, y = p.position()  # Obtém a posição atual do mouse
    p.click(x, y)  # Clica na posição obtida
    root.destroy()  # Fecha a janela Tkinter
    
def safety_exit():
    print("Safety exit activated. Exiting script.")
    exit()
    
# Start a listener for the 'esc' or '-' key
keyboard.add_hotkey('esc', safety_exit)
keyboard.add_hotkey('-', safety_exit)

alt_tab_tab()   #busca o navegador
alt_tab_tab()   #busca o excel


while True:
    
        
    
    down()
    copy()
    copied_content = pp.paste()
    
    alt_tab()
    get_and_click_mouse_position()
    #coordinate_str = pp.paste()
    #x, y = map(int, coordinate_str.split(','))
    
    

    # Click at the obtained coordinate
    p.click()
    t.sleep(5)
    p.keyDown('ctrl')   #ctrl + p para salvar PDF
    t.sleep(0.2)
    p.hotkey('p')
    t.sleep(2)
    p.keyUp('ctrl')
    t.sleep(1)
    enter()
    t.sleep(1)
    colar()
    enter()
    ctrl_w()
    alt_tab()

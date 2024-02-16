import os
import json
import pyautogui as p
import time as t
import clipboard as c
import pyperclip as pp
import tkinter as tk #recurso para criação de interface IHM
from tkinter import simpledialog




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
def alt_tab():
    p.keyDown('alt')
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
def right():
    p.keyDown('right')
    t.sleep(0.2)
    p.keyUp('right')
    t.sleep(0.2)
def ctrl_a():
    p.keyDown('ctrl')
    t.sleep(0.2)
    p.hotkey('a')
    t.sleep(0.3)
    p.keyUp('ctrl')
    t.sleep(0.2)
def esc():
    p.keyDown('esc')
    t.sleep(0.2)
    p.keyUp('esc')
    t.sleep(0.2)
def left():
    p.keyDown('left')
    t.sleep(0.2)
    p.keyUp('left')
    t.sleep(0.2)


#alternando para a janela excel
alt_tab()

while True:
    
    
    ctrl_pagedown() #alternar para janela excel onde está a lista
    down()  #mudando para a célula de baixo
    copiar()    #copiando o número da matrícula
    ctrl_pageup()   #alternar para janela excel onde está a FICHA
    colar() #colando número matrícula
    ctrl_pagedown() #voltando para Excel para copiar o nome do arquivo que será salvo
    right() #selecionando célula contendo matrícula + nome do aluno
    right()
    right()
    p.click(x=417, y=182)   #indo para o local da barra de endereço excel
    t.sleep(0.2)
    ctrl_a()    #selecionando tudo
    copiar()  #copiando
    esc()   #desselecionando
    left()  #indo 3x para a esquerda; célula origem (matrícula)
    left()
    left()
    ctrl_pageup()   #voltando para a planilha PNLD
    imprimir()  #salvar como PDF
    t.sleep(2)
    enter() #enter para selecinar 'imprimir'
    t.sleep(3)
    colar()
    enter() #mandando imprimir, para salvar como PDF
    t.sleep(2)
#IMPORTANDO BIBLIOTECAS ###################################################################################################################
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
    
#DECLARAÇÕES ESPECÍFICAS DESTE CÓDIGO
    


# CÓDIGO

# Caminhos dos arquivos
arquivos = [
    r'\\LAB\Users\Public\PNLD\FICHA LIVRO DIDÁTICO 2024.xlsm',
    r'C:\Users\Public\Videos\DIEGO\ETIQUETA - CHAVES.xlsx',
    r'C:\Users\Public\Videos\DIEGO\ORGANIZAR\NORMAS ESCOLARES 2024 - COM AUTORIZAÇÃO PARA SAÍDA.docx'
]


def abrir(arquivos):
    for arquivo in arquivos:
        try:
            # Abrir o arquivo
            os.startfile(arquivo)
            # Esperar um tempo para o arquivo abrir completamente
            t.sleep(2)
        except Exception as e:
            print("Erro ao abrir ou imprimir o arquivo:", e)

abrir(arquivos)
'''
def abrir_e_imprimir(arquivos):
    for arquivo in arquivos:
        try:
            # Abrir o arquivo
            os.startfile(arquivo)
            # Esperar um tempo para o arquivo abrir completamente
            t.sleep(2)
            # Pressionar as teclas de atalho para imprimir (Ctrl + P)
            p.hotkey('ctrl', 'p')
            # Esperar um tempo para a janela de impressão aparecer
            t.sleep(2)
            # Pressionar a tecla Enter para confirmar a impressão
            p.press('enter')
            # Esperar um tempo para a impressão ser enviada
            t.sleep(2)
        except Exception as e:
            print("Erro ao abrir ou imprimir o arquivo:", e)

abrir_e_imprimir(arquivos)

abrir(arquivos)

def capturar_posicao(event):
    global posicao_capturada
    posicao_capturada = {'x': event.x, 'y': event.y}
    root.destroy()

def criar_janela(texto):
    root = tk.Tk()
    root.geometry("300x100")
    root.title("Capturar Posição")
    label = tk.Label(root, text=texto)
    label.pack()
    root.bind('<Button-1>', capturar_posicao)
    root.mainloop()

# 1. Capturar a posição do navegador
criar_janela("Clique onde está o navegador")
with open('posicoes.json', 'r') as file:
    posicoes = json.load(file)
posicoes['navegador'] = posicao_capturada
with open('posicoes.json', 'w') as file:
    json.dump(posicoes, file)

# 2. Capturar a posição do novo aluno
criar_janela("Selecione TODA a linha com os dados do(a) novo(a) aluno(a)")
with open('posicoes.json', 'r') as file:
    posicoes = json.load(file)
posicoes['novo_aluno'] = posicao_capturada
with open('posicoes.json', 'w') as file:
    json.dump(posicoes, file)

# 3. Capturar a posição do Excel e das planilhas
criar_janela("Clique onde está o Excel")
with open('posicoes.json', 'r') as file:
    posicoes = json.load(file)
posicoes['excel'] = posicao_capturada
with open('posicoes.json', 'w') as file:
    json.dump(posicoes, file)

criar_janela("Clique onde está a planilha 'FICHA DE LIVRO'")
with open('posicoes.json', 'r') as file:
    posicoes = json.load(file)
posicoes['ficha_livro'] = posicao_capturada
with open('posicoes.json', 'w') as file:
    json.dump(posicoes, file)

criar_janela("Clique onde está a planilha 'etiqueta(chaves)'")
with open('posicoes.json', 'r') as file:
    posicoes = json.load(file)
posicoes['etiqueta_chaves'] = posicao_capturada
with open('posicoes.json', 'w') as file:
    json.dump(posicoes, file)
'''

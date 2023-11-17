import os
import json
import pyautogui as p
import time as t
import clipboard as c
import pyperclip as pp
import tkinter as tk #recurso para criação de interface IHM
from tkinter import simpledialog

#DECLARANDO FUNÇÕES #######################################################################################################################


# Inicialize o contador de tempo
start_time = t.time()


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
def alt_tab():
    p.keyDown('alt')
    t.sleep(0.2)
    p.hotkey('tab')
    t.sleep(0.3)
    p.keyUp('alt')
    t.sleep(0.2)
    
    
    
# Tente abrir o arquivo 'coordinates.json' e carregar as coordenadas
try:
    with open('coordinates.json', 'r') as f:
        coordinates = json.load(f)
        print("Arquivo coordinates.json lido com sucesso!")  
        brave_x, brave_y = coordinates['brave']
        endereco_x, endereco_y = coordinates['endereco']
        janela1_x, janela1_y = coordinates['janela1']
    p.click(brave_x,brave_y)    
        
        
except (FileNotFoundError, json.JSONDecodeError, KeyError):
    p.alert('Posicione o mouse onde desejar capturar o LOCAL do BRAVE e pressione OK')  #brave
    brave_x, brave_y = p.position()
    t.sleep(0.3)
    p.click(brave_x, brave_y)
    t.sleep(0.5)
    p.alert('Posicione o mouse onde desejar capturar o LOCAL da BARRA DE ENDERECO e pressione OK')  #endereco
    endereco_x,endereco_y = p.position()
    p.alert('Posicione o mouse onde desejar capturar o LOCAL da JANELA1 e pressione OK')    #janela1
    janela1_x,janela1_y = p.position()
    print("Arquivo coordinates.json registrados com sucesso!")  
    
    with open('coordinates.json', 'w') as f:
        json.dump({'brave': (brave_x, brave_y), 'endereco':(endereco_x,endereco_y), 'janela1': (janela1_x, janela1_y) }, f)
        
        
        
p.click(brave_x,brave_y)
t.sleep(0.5)
p.click(janela1_x,janela1_y)    #janela1 - listagem geral dos alunos
t.sleep(0.3)
ctrl_pagedown()
p.click(endereco_x,endereco_y)
t.sleep(0.3)
p.typewrite('https://www.gemul-aparecida.com.br/app/sca_aluno.asp') #janela2 - Ficha Cadastral
t.sleep(0.3)
enter()
ctrl_pagedown()
p.click(endereco_x,endereco_y)
t.sleep(0.3)
p.typewrite('https://www.gemul-aparecida.com.br/app/sca_historico_escolarCon.asp')  #janela3 - Cadastro do histórico escolar do aluno
t.sleep(0.3)
enter()
ctrl_pagedown()
p.click(endereco_x,endereco_y)
t.sleep(0.3)
p.typewrite('https://www.gemul-aparecida.com.br/app/sca_rel_historico_escolar_educacao_infantilCon.asp')    #janela4 - Histórico escolar da educação Infantil
t.sleep(0.3)
enter()
ctrl_pagedown()
p.click(endereco_x,endereco_y)
t.sleep(0.3)
p.typewrite('https://www.gemul-aparecida.com.br/app/sca_rel_historico_escolar_ensino_fundamentalCon.asp')    #janela5 - Histórico escolar do ensino fundamental
t.sleep(0.3)
enter()
ctrl_pagedown()
p.click(endereco_x,endereco_y)
t.sleep(0.3)
p.typewrite('https://www.gemul-aparecida.com.br/App/sca_rel_ficha_descritivaCon.asp')    #janela6 - Ficha Descritiva
t.sleep(0.3)
enter()
ctrl_pagedown()
p.click(endereco_x,endereco_y)
t.sleep(0.3)
p.typewrite('https://www.gemul-aparecida.com.br/app/sca_rel_extrato_nota_faltaCon.asp')    #janela7 - Extrato de notas e faltas
t.sleep(0.3)
enter()
alt_tab()

# Obtenha o tempo decorrido
end_time = t.time()

# Imprima o indicativo do programa que rodou
print('programa RESET_JANELAS executado com sucesso')

# Imprima o tempo decorrido
print("Tempo decorrido:", end_time - start_time)
import pyautogui as p
import time as t
import pyperclip
import tkinter as tk
from tkinter import messagebox


#INFORMAÇÕES IMPORTANTES
#Utiliza-se da folha de ponto anterior como base de lista de nomes




def folha_atestado():
    # clicando na PASTA na barra de tarefas
    p.moveTo(x=409, y=881)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)
    # clicando na PASTA de SCANNER
    p.moveTo(x=302, y=785)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)


    # clicando na PASTA na barra de tarefas
    p.moveTo(x=409, y=881)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)
    # clicando na PASTA de LISTA de funcionários, do MES referente aos lançamentos
    p.moveTo(x=520, y=773)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)


    # clicando na primeira pasta, estrategicamente posicionada
    p.moveTo(x=1060, y=156)
    t.sleep(0.1)
    p.click()
    t.sleep(0.5)
    p.click()
    t.sleep(0.5)
    p.hotkey('ctrl','a')
    t.sleep(0.5)

    # copiando o que está no CLIPBOARD e escrevendo na pasta que receberá o nome do funcionario
    # Get the content from the clipboard
    clipboard_content = pyperclip.paste()
    # Use pyautogui to write the clipboard content
    p.write(clipboard_content)

    # pressionando 'enter'
    p.press('enter')
    t.sleep(0.5)
    # entrando na pasta
    p.press('enter')
    t.sleep(0.2)


    # selecionando a janela de SCANNERS e selecionando o primeiro arquivo para arrastar para a janela ao lado
    # clicando na PASTA na barra de tarefas
    p.moveTo(x=409, y=881)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)
    # clicando na PASTA de SCANNER
    p.moveTo(x=302, y=785)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)
    # selecionando o primeiro arquivo 
    p.moveTo(x=260, y=157)
    t.sleep(0.1)
    p.click()
    t.sleep(0.5)
    p.hotkey('ctrl','x')
    t.sleep(0.3)

    # alternando para a nanela ao lado
    # clicando na PASTA na barra de tarefas
    p.moveTo(x=409, y=881)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)
    # clicando na PASTA de LISTA 
    p.moveTo(x=520, y=773)
    t.sleep(0.3)
    p.click()
    t.sleep(0.3)
    # colando o arquivo na pasta LISTA
    p.hotkey('ctrl','v')
    t.sleep(0.3)



    # selecionando nome para altera-lo
    p.moveTo(x=1060, y=156)
    t.sleep(0.1)
    p.click()
    t.sleep(0.5)
    p.click()
    t.sleep(0.5)
    p.hotkey('ctrl','a')
    t.sleep(0.3)

    # escrevendo "FOLHA + NOME DO FUNCIONARIO"
    text_to_write = ("FOLHA - " + clipboard_content).upper()
    # Use pyautogui to write the concatenated text
    p.write(text_to_write)
    
    
    
    
    # selecionando o outro arquivo (ATESTADOS) que ficou na pasta de SCANNER
    # arrastando os arquivos para dentro da pasta ao lado
    # clicando na PASTA na barra de tarefas
    p.moveTo(x=409, y=881)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)
    # clicando na PASTA de SCANNER
    p.moveTo(x=302, y=785)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)
    # selecionando o primeiro arquivo 
    p.moveTo(x=260, y=157)
    t.sleep(0.1)
    p.click()
    t.sleep(0.5)
    p.hotkey('ctrl','x')
    t.sleep(0.3)

    # alternando entre janelas
    # clicando na PASTA na barra de tarefas
    p.moveTo(x=409, y=881)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)
    # clicando na PASTA de LISTA 
    p.moveTo(x=520, y=773)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)
    # colando o arquivo na pasta LISTA
    p.hotkey('ctrl','v')
    t.sleep(0.3)



    # selecionando nome para altera-lo
    p.moveTo(x=1069, y=180)
    t.sleep(0.1)
    p.click()
    t.sleep(0.5)
    p.click()
    t.sleep(0.5)
    p.hotkey('ctrl','a')
    t.sleep(0.3)

    # escrevendo "ATESTADO + NOME DO FUNCIONARIO"
    text_to_write = ("ATESTADO - " + clipboard_content).upper()
    # Use pyautogui to write the concatenated text
    p.write(text_to_write)


    t.sleep(0.3)
    p.press('enter')
    t.sleep(0.3)
    # voltando um nível de pasta
    p.press('backspace')

    # selecionando o Word (que tem os nomes dos funcionários para alimentar novamente o clipboard com o nome do próximo profissional)
    p.moveTo(x=291, y=879)
    t.sleep(0.1)
    p.click()
    p.press('pagedown', presses=2)
    
def folha():
    
    # clicando na PASTA na barra de tarefas
    p.moveTo(x=409, y=881)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)
    # clicando na PASTA de SCANNER
    p.moveTo(x=302, y=785)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)


    # clicando na PASTA na barra de tarefas
    p.moveTo(x=409, y=881)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)
    # clicando na PASTA de LISTA de funcionários, do MES referente aos lançamentos
    p.moveTo(x=520, y=773)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)


    # clicando na primeira pasta, estrategicamente posicionada
    p.moveTo(x=1060, y=156)
    t.sleep(0.1)
    p.click()
    t.sleep(0.5)
    p.click()
    t.sleep(0.5)
    p.hotkey('ctrl','a')
    t.sleep(0.5)

    # copiando o que está no CLIPBOARD e escrevendo na pasta que receberá o nome do funcionario
    # Get the content from the clipboard
    clipboard_content = pyperclip.paste()
    # Use pyautogui to write the clipboard content
    p.write(clipboard_content)

    # pressionando 'enter'
    p.press('enter')
    t.sleep(0.5)
    # entrando na pasta
    p.press('enter')
    t.sleep(0.2)


    # selecionando a janela de SCANNERS e selecionando o primeiro arquivo para arrastar para a janela ao lado
    # clicando na PASTA na barra de tarefas
    p.moveTo(x=409, y=881)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)
    # clicando na PASTA de SCANNER
    p.moveTo(x=302, y=785)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)
    # selecionando o primeiro arquivo 
    p.moveTo(x=260, y=157)
    t.sleep(0.1)
    p.click()
    t.sleep(0.5)
    p.hotkey('ctrl','x')
    t.sleep(0.3)

    # alternando para a nanela ao lado
    # clicando na PASTA na barra de tarefas
    p.moveTo(x=409, y=881)
    t.sleep(0.1)
    p.click()
    t.sleep(0.1)
    # clicando na PASTA de LISTA 
    p.moveTo(x=520, y=773)
    t.sleep(0.3)
    p.click()
    t.sleep(0.3)
    # colando o arquivo na pasta LISTA
    p.hotkey('ctrl','v')
    t.sleep(0.3)



    # selecionando nome para altera-lo
    p.moveTo(x=1060, y=156)
    t.sleep(0.1)
    p.click()
    t.sleep(0.5)
    p.click()
    t.sleep(0.5)
    p.hotkey('ctrl','a')
    t.sleep(0.3)

    # escrevendo "FOLHA + NOME DO FUNCIONARIO"
    text_to_write = ("FOLHA - " + clipboard_content).upper()
    # Use pyautogui to write the concatenated text
    p.write(text_to_write)
    
    t.sleep(0.3)
    p.press('enter')
    t.sleep(0.3)
    # voltando um nível de pasta
    p.press('backspace')

    # selecionando o Word (que tem os nomes dos funcionários para alimentar novamente o clipboard com o nome do próximo profissional)
    p.moveTo(x=291, y=879)
    t.sleep(0.1)
    p.click()
    p.press('pagedown', presses=2)



def on_confirm():
    resposta = var.get()
    if resposta == 1:
        folha_atestado()
    else:
        folha()
    root.destroy()

root = tk.Tk()
root.title("Verificação de Atestado")

var = tk.IntVar()

label = tk.Label(root, text="Há atestado?")
label.pack()

rb1 = tk.Radiobutton(root, text="Sim", variable=var, value=1)
rb1.pack()

rb2 = tk.Radiobutton(root, text="Não", variable=var, value=2)
rb2.pack()

button = tk.Button(root, text="Confirmar", command=on_confirm)
button.pack()

root.mainloop()
import pyautogui as p
import tkinter as tk
import time as t

def get_position():
    t.sleep(0.5)
    return p.position()

def countdown(count):
    # Altera o texto do label para o valor atual da contagem regressiva
    label['text'] = "Posicione o mouse no local desejado. A contagem regressiva é: " + str(count)
    
    if count > 0:
        # Chama a função countdown novamente após 1000 milissegundos (1 segundo)
        root.after(1000, countdown, count - 1)
    else:
        # Se a contagem regressiva chegou a zero, obtemos a posição do mouse e fechamos a janela
        global pos
        pos = get_position()
        root.destroy()

root = tk.Tk()
root.geometry('400x100')  # Definindo o tamanho da janela

# Criando um label (texto) que será atualizado pela contagem regressiva
label = tk.Label(root, text="")
label.pack()

# Iniciando a contagem regressiva
countdown(0.5)

root.mainloop()


print(get_position())
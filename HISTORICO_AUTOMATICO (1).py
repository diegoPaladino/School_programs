




import os
import json
import pyautogui as p
import time as t
import clipboard as c
import pyperclip as pp
import tkinter as tk #recurso para criação de interface IHM
from tkinter import simpledialog

#PRIMEIRA ETAPA:
#   PERGUNTA QUAL O NÚMERO DA MATRÍCULA
#   LANÇA O NÚMERO DA MATRÍCULA EM TODOS OS CAMPOS NECESSÁRIOS (EXCEL, ABAS DO GEMUL NO NAVEGADOR)

# Tente abrir o arquivo 'coordinates.json' e carregar as coordenadas
try:
    with open('coordinates.json', 'r') as f:
        coordinates = json.load(f)
    brave_x, brave_y = coordinates['brave']
        
except (FileNotFoundError, json.JSONDecodeError, KeyError):
    # Se o arquivo não existir, não puder ser lido ou as chaves não estiverem presentes,
    # pedimos ao usuário para fornecer as coordenadas

    p.alert('Posicione o mouse onde desejar capturar o LOCAL do BRAVE e pressione OK')
    brave_x, brave_y = p.position()
    
    with open('coordinates.json', 'w') as f:
        json.dump({'brave': (brave_x, brave_y)},f)

# Agora você pode usar as variáveis em seu código



#ABERTURA DE JANELA PERGUNTANDO QUAL É O NÚMERO DA MATRÍCULA
# Cria uma nova janela Tkinter. Isso é necessário porque a janela de diálogo precisa de uma janela principal.
ROOT = tk.Tk()

# Esconde a janela principal porque só queremos mostrar a janela de diálogo.
ROOT.withdraw()

# Solicita ao usuário que insira o número de matrícula do aluno.
student_id = simpledialog.askstring(title="Matrícula do Aluno",
                                    prompt="Insira o número de matrícula do aluno:")

# Agora você pode usar a variável student_id em seu código.
print(f"O número de matrícula do aluno é {student_id}")



#COPIANDO NÚMERO DE MATRÍCULA NOS CAMPOS DE BUSCA
#selecionando janela brave
t.sleep(0.3)
p.click(brave_x, brave_y)
t.sleep(0.3)
#clicando na 5ª aba (5. GEMUL-FICHA DESCRITIVA)
p.click(x=623, y=14)
t.sleep(0.3)
#clicando no campo de matrícula
p.click(x=233, y=674)
t.sleep(0.3)
#escrevendo o número da matrícula salvo na memória
p.typewrite(student_id)
t.sleep(0.3)
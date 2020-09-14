#print_month_current_experience

from datetime import datetime
import subprocess
import time as t
import pyautogui as p

#definitions
mes_atual = datetime.now().month
D=mes_atual

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

def escrever_mes_atual():
    if (mes_atual == 1):
        mes='SETRANSP_DEZEMBRO'
    if (mes_atual == 2):
        mes='SETRANSP_JANEIRO' 
    if (mes_atual == 3):
        mes='SETRANSP_FEVEREIRO'
    if (mes_atual == 4):
        mes='SETRANSP_MARCO'
    if (mes_atual == 5):
        mes='SETRANSP_ABRIL'
    if (mes_atual == 6):
        mes='SETRANSP_MAIO'
    if (mes_atual == 7):
        mes='SETRANSP_JUNHO'
    if (mes_atual == 8):
        mes='SETRANSP_JULHO'
    if (mes_atual == 9):
        mes='SETRANSP_AGOSTO'
    if (mes_atual == 10):
        mes='SETRANSP_SETEMBRO'
    if (mes_atual == 11):
        mes='SETRANSP_OUTUBRO'
    if (mes_atual == 12):
        mes='SETRANSP_NOVEMBRO'


# print(mes_atual)

subprocess.Popen(['notepad'])
t.sleep(1.5)

# print(mes_atual)
# p.write(mes_atual)
# p.write(escrever_mes_atual())
# print(escrever_mes_atual)
p.write(D)
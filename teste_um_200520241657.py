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


# DECLARAÇÕES DE BIBLIOTECAS ESPECÍFICAS PARA ESTE PROGRAMA

def abrir_chrome():
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
    
    return driver

def logar(driver):
    # Localiza o campo de usuário e insere o nome de usuário
    username_field = driver.find_element(By.XPATH, '//*[@id="txtLogin"]')
    username_field.send_keys("DIEGO.CSF")

    # Localiza o campo de senha e insere a senha
    password_field = driver.find_element(By.XPATH, '//*[@id="txtSenha"]')
    password_field.send_keys("GMLPALADINO")

    # Localiza o botão de login e clica nele
    login_button = driver.find_element(By.XPATH, '//*[@id="frm"]/div[4]/div[2]/a')
    login_button.click()
    
def abrir_novas_abas(driver):
    urls = [
        "https://www.gemul-aparecida.com.br/app/sca_aluno.asp",
        "https://www.gemul-aparecida.com.br/app/sca_historico_escolarCon.asp",
        "https://www.gemul-aparecida.com.br/app/sca_rel_historico_escolar_educacao_infantilCon.asp",
        "https://www.gemul-aparecida.com.br/app/sca_rel_historico_escolar_ensino_fundamentalCon.asp",
        "https://www.gemul-aparecida.com.br/App/sca_rel_ficha_descritivaCon.asp",
        "https://www.gemul-aparecida.com.br/app/sca_rel_extrato_nota_faltaCon.asp"
    ]
    
    for url in urls:
        # Abre uma nova aba
        driver.execute_script(f"window.open('{url}', '_blank');")
        # Alterna para a nova aba (a última aberta)
        driver.switch_to.window(driver.window_handles[-1])
    
    # Alterna de volta para a primeira aba
    driver.switch_to.window(driver.window_handles[0])
    
# Função para exibir a janela de entrada de matrícula
def obter_matricula():
    # Cria uma janela Tkinter
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Solicita a entrada do número de matrícula
    matricula = simpledialog.askstring("Entrada de Matrícula", "Qual número da matrícula?", parent=root)
    
    return matricula

def digita_matricula_todas():
    
    t.sleep(1)
    ctrl_pagedown()
    
    # Obter a matrícula do input do Tkinter
    matricula = matricula_input.get()
    
    # Encontrar o campo de matrícula e inserir o valor
    campo_matricula = driver.find_element(By.XPATH, '//*[@id="txtMatricula"]')
    campo_matricula.send_keys(matricula)
    
    # Clicar no botão
    botao = driver.find_element(By.XPATH, '//*[@id="button-addon5"]')
    botao.click()


# Obtém o número de matrícula do usuário
numero_matricula = obter_matricula()

if numero_matricula and len(numero_matricula) == 9:
    # CÓDIGO
    driver = abrir_chrome()  # chama a função que abre o selenium chromedriver 
    logar(driver)  # loga no gemul

    # Abre as novas abas com as URLs desejadas
    abrir_novas_abas(driver)
    
    #  Chama a função que digitará o número de matrícula
    digita_matricula_todas()

    # Pausa a execução para manter a janela aberta
    input("Pressione Enter para fechar o navegador...")
    
    
    
else:
    print("Número de matrícula inválido. Certifique-se de que tenha 9 dígitos.")

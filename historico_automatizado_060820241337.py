import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Adicionada a importação de Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyautogui as p
import time as t
import clipboard as c
import pyperclip as pp
import tkinter as tk
from tkinter import simpledialog, ttk
import os

# Funções de automação de teclado e mouse
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
# Funções específicas do programa
def abrir_chrome():
    chrome_driver_path = "C:\\Users\\diego\\Desktop\\001-Desktop\\programas\\ChromeDriver\\chromedriver.exe"
    options = Options()
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get("https://www.gemul-aparecida.com.br/login.asp")
    return driver
def logar(driver):
    username_field = driver.find_element(By.XPATH, '//*[@id="txtLogin"]')
    username_field.send_keys("DIEGO.CSF")
    password_field = driver.find_element(By.XPATH, '//*[@id="txtSenha"]')
    password_field.send_keys("GMLPALADINO")
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
        driver.execute_script(f"window.open('{url}', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
    
    # Volta para a primeira aba
    driver.switch_to.window(driver.window_handles[0])

def seleciona_segunda_janela(driver):
    # Espera até que haja pelo menos 2 janelas abertas
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    # Seleciona a segunda janela aberta
    driver.switch_to.window(driver.window_handles[1])

def seleciona_terceira_janela(driver):
    # Seleciona a segunda janela aberta
    driver.switch_to.window(driver.window_handles[2])

def seleciona_quarta_janela(driver):
    # Seleciona a segunda janela aberta
    driver.switch_to.window(driver.window_handles[3])

def seleciona_quinta_janela(driver):
    # Seleciona a segunda janela aberta
    driver.switch_to.window(driver.window_handles[4])

def seleciona_setima_janela(driver):
    # Seleciona a segunda janela aberta
    driver.switch_to.window(driver.window_handles[6])

def obter_matricula():
    root = tk.Tk()
    root.withdraw()
    matricula = simpledialog.askstring("Entrada de Matrícula", "Qual número da matrícula?", parent=root)
    return matricula

def digita_matricula(driver, numero_matricula):
    # Encontre o campo de digitação pelo xpath e digite o número da matrícula
    campo_matricula = driver.find_element(By.XPATH, '//*[@id="txtMatricula"]')
    campo_matricula.clear()  # Limpa o campo antes de digitar
    campo_matricula.send_keys(numero_matricula)
    campo_matricula.send_keys(Keys.RETURN)
    
def obter_dados():
    def on_ok():
        global agrupamento, nome_escola, cidade, uf, carga_horaria
        agrupamento = combo.get()
        nome_escola = nome_escola_entry.get()
        cidade = cidade_entry.get()
        uf = uf_entry.get()
        carga_horaria = carga_horaria_entry.get()
        root.destroy()

    def on_cancel():
        root.destroy()

    root = tk.Tk()
    root.title("Entrada de Dados")

    tk.Label(root, text="Série").grid(row=0, column=0, padx=10, pady=5)
    combo = ttk.Combobox(root, values=[
        "AGRUPAMENTO 4",
        "AGRUPAMENTO 5",
        "1º ANO",
        "2º ANO",
        "3º ANO",
        "4º ANO",
        "5º ANO"
    ])
    combo.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Nome da Escola").grid(row=1, column=0, padx=10, pady=5)
    nome_escola_entry = tk.Entry(root)
    nome_escola_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Cidade").grid(row=2, column=0, padx=10, pady=5)
    cidade_entry = tk.Entry(root)
    cidade_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="UF").grid(row=2, column=2, padx=10, pady=5)
    uf_entry = tk.Entry(root, width=5)
    uf_entry.grid(row=2, column=3, padx=10, pady=5)

    tk.Label(root, text="Carga Horária").grid(row=3, column=0, padx=10, pady=5)
    carga_horaria_entry = tk.Entry(root)
    carga_horaria_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(root, text="OK", command=on_ok).grid(row=4, column=0, padx=10, pady=10)
    tk.Button(root, text="Cancelar", command=on_cancel).grid(row=4, column=1, padx=10, pady=10)

    root.mainloop()
    
numero_matricula = obter_matricula()

if numero_matricula and len(numero_matricula) == 9:
    driver = abrir_chrome()
    logar(driver)
    abrir_novas_abas(driver)
    seleciona_segunda_janela(driver)
    digita_matricula(driver, numero_matricula)
    seleciona_terceira_janela(driver)
    digita_matricula(driver, numero_matricula)
    seleciona_quarta_janela(driver)
    digita_matricula(driver, numero_matricula)
    seleciona_quinta_janela(driver)
    digita_matricula(driver, numero_matricula)
    seleciona_setima_janela(driver)
    digita_matricula(driver, numero_matricula)
    seleciona_terceira_janela(driver)
    obter_dados()
    
        # Verifica a opção selecionada e executa o código correspondente
    if agrupamento == "AGRUPAMENTO 4":
        # Código para AGRUPAMENTO 4
        print("selecionado AGRUPAMENTO 4")
    elif agrupamento == "AGRUPAMENTO 5":
        # Código para AGRUPAMENTO 5
        pass
    elif agrupamento == "1º ANO":
        t.sleep(2)
        esc()
        # Seleciona a terceira janela aberta
        seleciona_terceira_janela(driver)
        # Código para 1º ANO
        print("Selecionado 1º ANO, tentando clicar no botão incluir")
        incluir_btn = driver.find_element(By.XPATH, '//*[@id="panel-8"]/div[2]/div/div[3]/button[1]')
        incluir_btn.click()
        print("Botão incluir clicado com sucesso")

    elif agrupamento == "2º ANO":
        # Código para 2º ANO
        pass
    elif agrupamento == "3º ANO":
        # Código para 3º ANO
        pass
    elif agrupamento == "4º ANO":
        # Código para 4º ANO
        pass
    elif agrupamento == "5º ANO":
        # Código para 5º ANO
        pass
    
    
    input("Pressione Enter para fechar o navegador...")
    
    
else:
    print("Número de matrícula inválido. Certifique-se de que tenha 9 dígitos.")

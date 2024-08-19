# explicações do código ############################################################################################################




# Bibliotecas ############################################################################################################
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
import pyautogui as p
import clipboard as c
import pyperclip as pp
import tkinter as tk
from tkinter import simpledialog, ttk
import os


# Funções de automação de teclado e mouse #################################################################################
def abrir_nova_aba():
    p.keyDown('ctrl')
    time.sleep(0.2)
    p.hotkey('t')
    time.sleep(0.3)
    p.keyUp('ctrl')
    time.sleep(0.2)

def ctrl_pageup():
    p.keyDown('ctrl')
    time.sleep(0.2)
    p.hotkey('pageup')
    time.sleep(0.3)
    p.keyUp('ctrl')
    time.sleep(0.2)

def ctrl_pagedown():
    p.keyDown('ctrl')
    time.sleep(0.2)
    p.hotkey('pagedown')
    time.sleep(0.3)
    p.keyUp('ctrl')
    time.sleep(0.2)

def pageup():
    p.hotkey('pageup')
    time.sleep(0.3)

def pagedown():
    p.hotkey('pagedown')
    time.sleep(0.3)

def procurar():
    p.keyDown('ctrl')
    time.sleep(0.2)
    p.hotkey('f')
    time.sleep(0.3)
    p.keyUp('ctrl')
    time.sleep(0.2)

def copiar():
    p.keyDown('ctrl')
    time.sleep(0.2)
    p.hotkey('c')
    time.sleep(0.3)
    p.keyUp('ctrl')
    time.sleep(0.2)

def colar():
    p.keyDown('ctrl')
    time.sleep(0.2)
    p.hotkey('v')
    time.sleep(0.3)
    p.keyUp('ctrl')
    time.sleep(0.2)

def enter():
    p.press('enter')
    time.sleep(0.3)

def tab():
    p.press('tab')
    time.sleep(0.3)

def alt():
    p.press('tab')
    time.sleep(0.3)

def alt_tab():
    p.keyDown('alt')
    time.sleep(0.2)
    p.hotkey('tab')
    time.sleep(0.3)
    p.keyUp('alt')
    time.sleep(0.2)

def alt_tab_tab():
    p.keyDown('alt')
    time.sleep(0.2)
    p.hotkey('tab')
    time.sleep(0.2)
    p.hotkey('tab')
    time.sleep(0.3)
    p.keyUp('alt')
    time.sleep(0.2)

def alt_tab_tab_tab():
    p.keyDown('alt')
    time.sleep(0.2)
    p.hotkey('tab')
    time.sleep(0.2)
    p.hotkey('tab')
    time.sleep(0.2)
    p.hotkey('tab')
    time.sleep(0.3)
    p.keyUp('alt')
    time.sleep(0.2)

def imprimir():
    p.keyDown('ctrl')
    time.sleep(0.2)
    p.hotkey('p')
    time.sleep(0.3)
    p.keyUp('ctrl')
    time.sleep(0.2)

def enter():
    p.keyDown('enter')
    time.sleep(0.2)
    p.keyUp('enter')
    time.sleep(0.2)

def down():
    p.keyDown('down')
    time.sleep(0.2)
    p.keyUp('down')
    time.sleep(0.2)

def esc():
    p.hotkey('esc')
    time.sleep(0.3)

def right():
    p.hotkey('right')
    time.sleep(0.2)

def left():
    p.hotkey('left')
    time.sleep(0.2)

def up():
    p.hotkey('up')
    time.sleep(0.2)

def down():
    p.hotkey('down')
    time.sleep(0.2)

def click():
    p.click()
    time.sleep(0.2)

def end():
    p.hotkey('end')
    time.sleep(0.2)

# Funções específicas do programa #################################################################################
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
    # Seleciona a terceira janela aberta
    driver.switch_to.window(driver.window_handles[2])

def seleciona_quarta_janela(driver):
    # Seleciona a quarta janela aberta
    driver.switch_to.window(driver.window_handles[3])

def seleciona_quinta_janela(driver):
    # Seleciona a quinta janela aberta
    driver.switch_to.window(driver.window_handles[4])

def seleciona_setima_janela(driver):
    # Seleciona a sétima janela aberta
    driver.switch_to.window(driver.window_handles[6])
    
def selecionar_opcao(driver, xpath, valor):
    attempts = 3
    while attempts > 0:
        try:
            elemento = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            elemento.click()
            for option in elemento.find_elements(By.TAG_NAME, 'option'):
                if option.text == valor:
                    option.click()
                    break
            break
        except (StaleElementReferenceException, ElementClickInterceptedException):
            attempts -= 1
            print(f"Tentativa restante: {attempts}")
            if attempts == 0:
                raise

def escrever_texto(driver, xpath, texto):
    attempts = 3
    while attempts > 0:
        try:
            elemento = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            driver.execute_script("arguments[0].value = '';", elemento)  # Limpa o campo usando JavaScript
            driver.execute_script("arguments[0].value = arguments[1];", elemento, texto)  # Define o valor usando JavaScript
            break
        except (StaleElementReferenceException, ElementClickInterceptedException):
            attempts -= 1
            print(f"Tentativa restante: {attempts}")
            if attempts == 0:
                raise

def marcar_checkbox(driver, xpath):
    attempts = 3
    while attempts > 0:
        try:
            checkbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            if not checkbox.is_selected():
                checkbox.click()
            break
        except (StaleElementReferenceException, ElementClickInterceptedException):
            attempts -= 1
            print(f"Tentativa restante: {attempts}")
            if attempts == 0:
                raise

def incluir_enviar_dados(driver):
    botao = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="panel-8"]/div[2]/div/div[3]/div[3]/button[1]'))
    )
    botao.click()
def escrever_ano_na_caixa(driver, ano):
    attempts = 3
    while attempts > 0:
        try:
            # Espera até que o elemento esteja visível e interagível
            ano_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'txtAnoHistorico'))
            )
            driver.execute_script("arguments[0].value = '';", ano_input)  # Limpa o campo usando JavaScript
            driver.execute_script("arguments[0].value = arguments[1];", ano_input, ano)  # Define o valor usando JavaScript
            break
        except (StaleElementReferenceException, ElementClickInterceptedException):
            attempts -= 1
            print(f"Tentativa restante: {attempts}")
            if attempts == 0:
                raise

def combo_cadastramento_dados():
    # Escreve o valor da variável 'ano' na caixa de texto
    escrever_ano_na_caixa(driver, ano)

    # Seleciona a opção no item de xpath '//*[@id="cmbCurso"]'
    selecionar_opcao(driver, '//*[@id="cmbCurso"]', "EI-EDUCAÇÃO INFANTIL")

    # Seleciona a opção no item de xpath '//*[@id="cmbPeriodo"]'
    selecionar_opcao(driver, '//*[@id="cmbPeriodo"]', "AGRUPAMENTO IV")

    # Escreve o valor da variável 'nome_escola' na caixa de texto '//*[@id="txtEscola"]'
    escrever_texto(driver, '//*[@id="txtEscola"]', nome_escola)

    # Escreve o valor da variável 'cidade' na caixa de texto '//*[@id="txtCidade"]'
    escrever_texto(driver, '//*[@id="txtCidade"]', cidade)

    # Seleciona a opção no item de xpath '//*[@id="cmbUFResidencia"]'
    selecionar_opcao(driver, '//*[@id="cmbUFResidencia"]', uf)
    enter()
    tab()

    # Escreve o valor da variável 'carga_horaria' na caixa de texto '//*[@id="txtCHTotal"]'
    escrever_texto(driver, '//*[@id="txtCHTotal"]', carga_horaria)

    # Escreve 'teste' na caixa de texto '//*[@id="txtObservacao"]'
    escrever_texto(driver, '//*[@id="txtObservacao"]', 'teste')
    
    # Seleciona a opção no item de xpath '//*[@id="cmbDisciplina"]'
    selecionar_opcao(driver, '//*[@id="cmbDisciplina"]', "1º MOMENTO")

    # Seleciona a opção no item de xpath '//*[@id="cmbSituacaoPromocao"]'
    selecionar_opcao(driver, '//*[@id="cmbSituacaoPromocao"]', "Aprovado")

    # Marca o checkbox no item de xpath '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input'
    marcar_checkbox(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input')

    


def obter_matricula():
    root = tk.Tk()
    root.title("Entrada de Dados")
    
    dados = {}

    def submit():
        dados['numero_matricula'] = numero_matricula_var.get()
        dados['agrupamento'] = agrupamento_var.get()
        dados['nome_escola'] = nome_escola_var.get()
        dados['cidade'] = cidade_var.get()
        dados['ano'] = ano_var.get()
        dados['uf'] = uf_var.get()
        dados['carga_horaria'] = carga_horaria_var.get()

        root.quit()  # Termina o mainloop do Tkinter
    
    numero_matricula_var = tk.StringVar()
    agrupamento_var = tk.StringVar()
    nome_escola_var = tk.StringVar()
    cidade_var = tk.StringVar()
    ano_var = tk.StringVar()
    uf_var = tk.StringVar()
    carga_horaria_var = tk.StringVar()

    ttk.Label(root, text="Número da Matrícula:").grid(row=0, column=0, padx=10, pady=5)
    ttk.Entry(root, textvariable=numero_matricula_var).grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(root, text="Agrupamento:").grid(row=1, column=0, padx=10, pady=5)
    agrupamento_combobox = ttk.Combobox(root, textvariable=agrupamento_var)
    agrupamento_combobox['values'] = ("AGRUPAMENTO 4", "AGRUPAMENTO 5", "1º ANO", "2º ANO", "3º ANO", "4º ANO", "5º ANO")
    agrupamento_combobox.grid(row=1, column=1, padx=10, pady=5)
    
    ttk.Label(root, text="Nome da Escola:").grid(row=2, column=0, padx=10, pady=5)
    ttk.Entry(root, textvariable=nome_escola_var).grid(row=2, column=1, padx=10, pady=5)
    
    ttk.Label(root, text="Cidade:").grid(row=3, column=0, padx=10, pady=5)
    ttk.Entry(root, textvariable=cidade_var).grid(row=3, column=1, padx=10, pady=5)

    ttk.Label(root, text="Ano:").grid(row=4, column=0, padx=10, pady=5)
    ttk.Entry(root, textvariable=ano_var).grid(row=4, column=1, padx=10, pady=5)
    
    ttk.Label(root, text="UF:").grid(row=5, column=0, padx=10, pady=5)
    ttk.Entry(root, textvariable=uf_var).grid(row=5, column=1, padx=10, pady=5)
    
    ttk.Label(root, text="Carga Horária:").grid(row=6, column=0, padx=10, pady=5)
    ttk.Entry(root, textvariable=carga_horaria_var).grid(row=6, column=1, padx=10, pady=5)
    
    ttk.Button(root, text="OK", command=submit).grid(row=7, column=0, columnspan=2, pady=10)
    ttk.Button(root, text="CANCELAR", command=root.quit).grid(row=7, column=2, columnspan=2, pady=10)
    
    root.mainloop()
    root.destroy()
    return dados

# CÓDIGO ############################################################################################################
dados = obter_matricula()
numero_matricula = dados.get('numero_matricula')

def digita_matricula(driver, numero_matricula):
    # Encontre o campo de digitação pelo xpath e digite o número da matrícula
    campo_matricula = driver.find_element(By.XPATH, '//*[@id="txtMatricula"]')
    campo_matricula.clear()  # Limpa o campo antes de digitar
    campo_matricula.send_keys(numero_matricula)
    campo_matricula.send_keys(Keys.RETURN)

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
    
    agrupamento = dados['agrupamento']
    nome_escola = dados['nome_escola']
    cidade = dados['cidade']
    ano = dados['ano']
    uf = dados['uf']
    carga_horaria = dados['carga_horaria']
    
    print(f"Agrupamento: {agrupamento}")
    print(f"Nome da Escola: {nome_escola}")
    print(f"Cidade: {cidade}")
    print(f"Ano: {ano}")
    print(f"UF: {uf}")
    print(f"Carga Horária: {carga_horaria}")

    if dados['agrupamento'] == "AGRUPAMENTO 4":
        print("executada logica para agrupamento 4")
        seleciona_terceira_janela(driver)  # Seleciona a terceira janela
        incluir_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="panel-8"]/div[2]/div/div[3]/button[1]'))
        )
        incluir_btn.click()
        print(f"Botão para {agrupamento} clicado com sucesso")
        escrever_ano_na_caixa(driver, ano)
        
        combo_cadastramento_dados()


    input("Pressione Enter para fechar o navegador...")

    driver.quit()
else:
    print("Número de matrícula inválido. Certifique-se de que tenha 9 dígitos.")

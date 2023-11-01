
def handle_alert(driver, delay=3):
    """Try to close alert if it's present"""
    try:
        WebDriverWait(driver, delay).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        return True
    except:
        return False
# programa para gerar diários de classe de forma automática



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time as t
import datetime
from datetime import datetime
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import pyautogui as p


# PROVISORIO : APENAS ENQUANTO SE CONFECCIONA O CÓDIGO
print('########################################################################################################################################################################')
# Inicialize o contador de tempo
start_time = t.time()

# Configurações do Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
# Inicializar o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)
# Acessar o site
driver.get("https://www.gemul-aparecida.com.br/login.asp")
# Aguarda a página carregar
wait = WebDriverWait(driver, 10)
# Inserir nome de usuário e senha
username_field = driver.find_element(By.NAME, "txtLogin")
username_field.send_keys("DIEGO.CSF")
password_field = driver.find_element(By.NAME, "txtSenha")
password_field.send_keys("GMLPALADINO")
# Clicar no botão de login
login_button = driver.find_element(By.XPATH, "//a[@class='btn-u pull-right']")

login_button.click()

wait = WebDriverWait(driver, 10)

# Acessar o site
driver.get("https://www.gemul-aparecida.com.br/app/sca_rel_diario_manualCon.asp")
# Aguarda a página carregar


# Obtenha o tempo decorrido
end_time = t.time()


def select_turno(driver, turno="VESPERTINO"):
    select_turno = Select(driver.find_element(By.NAME, "cmbTurno"))
    select_turno.select_by_visible_text(turno)
    print('turno selecionado')

def select_turma(driver, turma):
    select_turma = Select(driver.find_element(By.NAME, "cmbTurma"))
    select_turma.select_by_visible_text(turma)
    print('turma selecionada')

def select_font(driver, font="Fonte Arial 12"):
    select_font = Select(driver.find_element(By.NAME, "cmbTamanhoFonteArial"))
    select_font.select_by_visible_text(font)
    print('fonte selecionada')
    
def click_generate_report(driver):
    # Wait until the body element is clickable
    wait = WebDriverWait(driver, 10)
    body_element = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
    
    # Click on the body element
    body_element.click()

    # Agora, tente clicar no botão "Gerar Relatório"
    button = driver.find_element(By.XPATH, "//button[@onclick='return gerar()']")
    button.click()
    print('botão clicado')


def open_print_window(driver):
    ActionChains(driver).send_keys(Keys.CONTROL + 'p').perform()

def click_print(pyautogui_delay=1):
    t.sleep(pyautogui_delay)
    p.press('enter')
    
def select_save_as_pdf(pyautogui_delay=1):
    t.sleep(pyautogui_delay)
    p.press('tab', presses=3)
    p.press('down')
    p.press('enter')

def go_back_to_main_window(driver):
    driver.back()

# List of all the 'turmas'
turmas = [
    "EF101VA22 - 1º ANO C",
    "EF201VA22 - 2º ANO C",
    "EF301VA22 - 3º ANO B",
    "EF401VA22 - 4º ANO B",
    "EF402VA22 - 4º ANO C",
    "EF501VA22 - 5º ANO B",
    "EI404VA23 - AGRUPAMENTO IV",
    "EI501VA22 - AGRUPAMENTO V",
    "EI502VA22 - AGRUPAMENTO V"
]

# Select 'turno'
select_turno(driver)

# Loop through each turma and execute the steps
for turma in turmas:
    print('eu estou cada segundo mais próximo de ir embora do trabalho em escola')
    select_turma(driver, turma)
    select_font(driver)
    click_generate_report(driver)
    open_print_window(driver)
    click_print()
    select_save_as_pdf()
    go_back_to_main_window(driver)

# Close the driver after all actions
# Imprima o tempo decorrido
print("Tempo decorrido:", end_time - start_time)
# Mantém a janela do navegador aberta até que o usuário decida fechá-la
input("Pressione Enter para fechar o navegador...")
driver.close()

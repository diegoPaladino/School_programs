'''Atualizador_elenco_bot
1º precisa-se limpar os dados antigos na planilha do excel
2º deixa-se selecionada a primeira célula onde vai o numero de matrícula do primeiro aluno, atualmente a B2


'''
# IMPORTAÇÃO DE BIBLIOTECAS
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.common.exceptions import NoAlertPresentException
import time as t
import datetime
from datetime import datetime
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import pyautogui as p





# DECLARAÇÕES
# Função que armazena o local (coordenadas x e y) do navegador Brave na barra de tarefas
def save_position():
    # Inicializa o tkinter
    root = tk.Tk()
    root.withdraw()

    # Mostra uma caixa de diálogo
    simpledialog.messagebox.showinfo("Posição", "Posicione o mouse sobre o local desejado (navegador Brave) e pressione OK.")
    
    # Obtém a posição do mouse
    x, y = p.position()

    # Salva a posição em um arquivo JSON chamado 'coordinates_elenco_bot.json'
    with open('coordinates_elenco_bot.json', 'w') as file:
        json.dump({'x': x, 'y': y}, file)

# função para chamar a localização
def get_saved_position():
    with open('coordinates_elenco_bot.json', 'r') as file:
        position = json.load(file)
        return position['x'], position['y']

def seleciona_turno_vespertino():
    # Encontre o elemento <select> pelo seu atributo 'name' ou 'id'
    select_element = Select(driver.find_element_by_id('cmbTurno'))

    # Selecione a opção pelo seu texto visível
    select_element.select_by_visible_text('VESPERTINO')



# EXECUÇÃO DO CÓDIGO - RUNNING THE CODE
# linha para indicar visualmente no terminal onde se iniciou o programa
print('########################################################################################################################################################################')
# Contagem do tempo:
start_time = t.time()
current_time = datetime.now()
# Inicia o Chrome - UNIVERSAL A TODAS AS OPÇÕES
# Configurações do Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-gpu")
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
# Aguarda a próxima página carregar e clica no ícone desejado
wait.until(EC.presence_of_element_located((By.XPATH, "//img[@src='../assets/img/icones/SCA.png']")))
icon = driver.find_element(By.XPATH, "//img[@src='../assets/img/icones/SCA.png']")
icon.click()
# Acessa diretamente a página
driver.get("https://www.gemul-aparecida.com.br/app/sca_rel_alunoCon.asp")
# Espera o campo de matrícula estar disponível para interação
t.sleep(1)
# seleciona o turno vespertino
seleciona_turno_vespertino()

print('Chrome iniciado')






# Obtenha o tempo decorrido
end_time = t.time()
# Imprima o tempo decorrido
print("Tempo decorrido:", end_time - start_time)
# linha para indicar visualmente no terminal onde se finalizou o programa
print('########################################################################################################################################################################')
# Mantém a janela do navegador aberta até que o usuário decida fechá-la
input("Pressione Enter para fechar o navegador...")
#driver.quit()


#create a program that do
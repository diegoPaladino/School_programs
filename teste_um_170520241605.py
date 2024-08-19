import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

# Localiza o campo de usuário e insere o nome de usuário
username_field = driver.find_element(By.XPATH, '//*[@id="txtLogin"]')
username_field.send_keys("DIEGO.CSF")

# Localiza o campo de senha e insere a senha
password_field = driver.find_element(By.XPATH, '//*[@id="txtSenha"]')
password_field.send_keys("GMLPALADINO")

# Localiza o botão de login e clica nele
login_button = driver.find_element(By.XPATH, '//*[@id="frm"]/div[4]/div[2]/a')
login_button.click()

# Pausa a execução para manter a janela aberta
input("Pressione Enter para fechar o navegador...")

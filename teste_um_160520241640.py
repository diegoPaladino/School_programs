from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Caminho para o executável do ChromeDriver
chrome_driver_path = "C:\\Users\\diego\\Desktop\\001-Desktop\\programas\\ChromeDriver\\chromedriver.exe"

# Opções do Chrome
options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Serviço do ChromeDriver
service = Service(executable_path=chrome_driver_path)

# Inicializa o navegador Chrome
driver = webdriver.Chrome(service=service, options=options)

# Abre uma nova janela do navegador
driver.get("https://www.gemul-aparecida.com.br/login.asp")

# Fecha o navegador após 5 segundos (opcional, apenas para ver o resultado)
import time
time.sleep(5)
#driver.quit()

# Pausa a execução para manter a janela aberta
input("Pressione Enter para fechar o navegador...")

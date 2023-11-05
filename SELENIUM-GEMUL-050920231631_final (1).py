from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time as t
import datetime
from datetime import datetime
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import pyautogui as p



# PROVISORIO : APENAS ENQUANTO SE CONFECCIONA O CÓDIGO
print('########################################################################################################################################################################')

# Declarando função para digitar 0 na carga horária
def preencher_carga_horaria(driver):
    try:
        # Wait until the element is available
        ch_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtCH"))
        )
        ch_element.clear()  # To ensure the field is empty
        ch_element.send_keys("0")
    except Exception as e:
        print(f"Error filling the workload: {e}")

'''
############################################################################################## EM TESTE
def selecionar_situacao(baseado_no_ano, driver):
    ano_atual = datetime.datetime.now().year
    situacao = "Cursando" if baseado_no_ano == ano_atual else "Aprovado"
    
    try:
        # Espera até que o dropdown esteja disponível
        situacao_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cmbSituacaoPromocao"))
        )
        dropdown = Select(situacao_dropdown)
        dropdown.select_by_visible_text(situacao)
    except Exception as e:
        print(f"Erro ao selecionar a situação: {e}")


############################################################################################## EM TESTE
'''



# Contagem do tempo:
start_time = t.time()
current_time = datetime.now()

# Função para coletar os dados do usuário
def collect_data():
    root = tk.Tk()
    root.title("Coleta de Dados")

    # Definir variáveis para armazenar os dados
    matricula = tk.StringVar()
    ano = tk.StringVar()
    ensino = tk.StringVar()
    agrupamento_ano = tk.StringVar()
    data_transferencia = tk.StringVar()

    # Criar widgets
    matricula_label = ttk.Label(root, text="Matrícula do aluno:")
    matricula_entry = ttk.Entry(root, textvariable=matricula)

    ano_label = ttk.Label(root, text="Ano para lançamento:")
    ano_entry = ttk.Entry(root, textvariable=ano)

    ensino_label = ttk.Label(root, text="Ensino:")
    ensino_combobox = ttk.Combobox(root, textvariable=ensino, values=["ENSINO INFANTIL", "ENSINO FUNDAMENTAL"])

    agrupamento_ano_label = ttk.Label(root, text="Agrupamento/Ano:")
    agrupamento_ano_combobox = ttk.Combobox(root, textvariable=agrupamento_ano)
    agrupamento_ano_combobox['values'] = []

    data_transferencia_label = ttk.Label(root, text="Data de transferência (dd/mm):")
    data_transferencia_entry = ttk.Entry(root, textvariable=data_transferencia)

    # Função para atualizar as opções de agrupamento/ano com base na seleção de ensino
    def update_agrupamento_ano_options(event):
        if ensino.get() == "ENSINO INFANTIL":
            agrupamento_ano_combobox['values'] = ["AGRUPAMENTO 4", "AGRUPAMENTO 5"]
        else:
            agrupamento_ano_combobox['values'] = ["1º ANO", "2º ANO", "3º ANO", "4º ANO", "5º ANO"]

    ensino_combobox.bind("<<ComboboxSelected>>", update_agrupamento_ano_options)

    submit_button = ttk.Button(root, text="Submeter", command=root.quit)

    # Organizar widgets na janela
    matricula_label.pack(pady=10)
    matricula_entry.pack(pady=10, padx=20, fill=tk.X)

    ano_label.pack(pady=10)
    ano_entry.pack(pady=10, padx=20, fill=tk.X)

    ensino_label.pack(pady=10)
    ensino_combobox.pack(pady=10, padx=20, fill=tk.X)

    agrupamento_ano_label.pack(pady=10)
    agrupamento_ano_combobox.pack(pady=10, padx=20, fill=tk.X)

    data_transferencia_label.pack(pady=10)
    data_transferencia_entry.pack(pady=10, padx=20, fill=tk.X)

    submit_button.pack(pady=20)

    root.mainloop()

    # Coletar os dados inseridos pelo usuário
    data = {
        "matricula": matricula.get(),
        "ano": ano.get(),
        "ensino": ensino.get(),
        "agrupamento_ano": agrupamento_ano.get(),
        "data_transferencia": data_transferencia.get()
    }

    root.destroy()

    return data

# Coletar os dados do usuário
collected_data = collect_data()



## CALCULADORA DE CARGA HORÁRIA

total_horas = 0

def calcular_carga_horaria(data_transferencia, ensino):
    # Dicionário com os dias letivos por mês
    dias_letivos = {
        1: 6,
        2: 20,
        3: 21,
        4: 19,
        5: 21,
        6: 21,
        7: 0,  # Mês de férias
        8: 22,
        9: 22,
        10: 18,
        11: 19,
        12: 12
    }

    # Dicionário com feriados e recessos por mês
    feriados_recessos = {
        1: 0,
        2: 3,  # 1 feriado + 2 recessos
        3: 0,
        4: 2,  # 2 feriados
        5: 1,  # 1 feriado
        6: 2,  # 1 feriado + 1 recesso
        7: 0,
        8: 0,
        9: 2,  # 1 feriado + 1 recesso
        10: 5,  # 3 feriados + 2 recessos
        11: 3,  # 3 feriados
        12: 0
    }
    
    data_transferencia = datetime.datetime.strptime(data_transferencia, "%d/%m")

    total_horas = 0

    # Iterando pelos meses e calculando a carga horária
    for mes, dias in dias_letivos.items():
        if data_transferencia.month == mes:
            total_horas += (data_transferencia.day - feriados_recessos[mes]) * 5
            break
        else:
            total_horas += (dias - feriados_recessos[mes]) * 5

    # Adjusting the total hours based on the selected option
    if ensino == "ENSINO INFANTIL":
        total_horas = (total_horas / 1000) * 800
    return total_horas

def on_calculate(event=None):  # Adicionado event=None para permitir chamadas diretas e através de eventos
    
    ensino: ensino.get()
    data_transferencia: data_transferencia.get()
    try:
        horas = calcular_carga_horaria(data_transferencia, ensino)
        resultado = f"{int(horas)} horas-aula"
        result_var.set(resultado)
        
        # Copiando o resultado para a área de transferência
        root.clipboard_clear()
        root.clipboard_append(int(horas))
        root.update()  # Isso é necessário para que o resultado permaneça na área de transferência após o programa ser fechado
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira a data no formato dd/mm.")







#acredito que as funções IF entrariam a partir daqui.
# Verificar o agrupamento escolhido pelo usuário e executar o código correspondente
if collected_data["agrupamento_ano"] == "AGRUPAMENTO 4":
    print('agrupamento 4')
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
    driver.get("https://www.gemul-aparecida.com.br/app/sca_historico_escolarCon.asp")
    # Espera o campo de matrícula estar disponível para interação
    #BLOCO responsável por encontrar o campo de ano, que já vem nativamente preenchido com o ano corrente e substituir pelo que foi alimentado no input do tkinter como sendo o ano que se pretende lançar o conteúdo do histórico
    matricula_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "txtMatricula")))
    # Clica no campo de matrícula
    matricula_field.click()
    # Localiza o elemento pelo ID
    # Calcula o número de caracteres no campo
    length = len(matricula_field.get_attribute('value'))
    # Simula a ação de pressionar "backspace" para cada caractere no campo
    for _ in range(length):
        matricula_field.send_keys(Keys.BACKSPACE)
    # Envia o valor da matrícula para o campo
    matricula_field.send_keys(collected_data['matricula'])
    # Selenium pressiona TAB
    elemento = driver.find_element(By.ID, "txtMatricula")
    elemento.send_keys(Keys.TAB)
    # Clica no botão INCLUIR
    botao_incluir = driver.find_element(By.XPATH, '//button[@onclick="salvar(\'I\')"]')
    botao_incluir.click()
    # Aguarda até que o campo de ano histórico esteja visível e pronto para ação
    campo_ano_historico = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "txtAnoHistorico"))
    )
    # Clica no campo para garantir que ele esteja ativo
    # Duplo clique no elemento
    actions = ActionChains(driver)
    actions.double_click(campo_ano_historico).perform()
    # Limpa o campo e insere o novo valor
    # limpando por meio do pyutogui
    p.press('backspace')
    t.sleep(0.3)
    campo_ano_historico.send_keys(collected_data["ano"])    #digita o dado ANO coletado
    campo_ano_historico.send_keys(Keys.TAB)
    
    # Selecionando EDUCAÇÃO INFANTIL
    from selenium.webdriver.common.by import By
    dropdown_element = driver.find_element(By.ID, "cmbCurso")
    # Criar um objeto Select a partir do elemento
    select = Select(dropdown_element)
    # Selecionar a opção pelo texto visível
    select.select_by_visible_text("EI-EDUCAÇÃO INFANTIL")


    # Selecionando AGRUPAMENTO IV
    # Localizar o elemento do menu suspenso
    dropdown_periodo = driver.find_element(By.ID, "cmbPeriodo")
    # Criar um objeto Select a partir do elemento
    select_periodo = Select(dropdown_periodo)
    # Selecionar a opção pelo texto visível
    select_periodo.select_by_visible_text("AGRUPAMENTO IV")
    
    # Supondo que você já tenha o driver configurado e a página carregada
    dropdown = Select(driver.find_element(By.ID, 'cmbDisciplina'))
    dropdown.select_by_visible_text('1º MOMENTO')
    
   
    # Preenche a carga horária com 0
    preencher_carga_horaria(driver)
    
    '''
    ############################################################################################## EM TESTE
    
    selecionar_situacao(2023, driver)
    
    ############################################################################################## EM TESTE
    '''
    
    
    
    
    print("fim da ação AGRUPAMENTO IV em: ")
    
    



# ITEM EM TESTE  #####################################################################################################################################
    
    
    #tentar digitar com pyautogui
    #p.typewrite(total_horas,interval=0.05)


# ITEM EM TESTE  #####################################################################################################################################
    

    



'''
elif collected_data["agrupamento_ano"] == "AGRUPAMENTO 5":
    print('AGRUPAMENTO 5')

elif collected_data["agrupamento_ano"] == "1º ANO":
    print('1º ANO')

elif collected_data["agrupamento_ano"] == "2º ANO":
    print('2º ANO')

elif collected_data["agrupamento_ano"] == "3º ANO":
    print('3º ANO')
    
elif collected_data["agrupamento_ano"] == "4º ANO":
    print('4º ANO')
    
elif collected_data["agrupamento_ano"] == "5º ANO":
    print('5º ANO')
'''








# Obtenha o tempo decorrido
end_time = t.time()

# Imprima o tempo decorrido
print("Tempo decorrido:", end_time - start_time)

# PROVISORIO : APENAS ENQUANTO SE CONFECCIONA O CÓDIGO
print('########################################################################################################################################################################')


# Mantém a janela do navegador aberta até que o usuário decida fechá-la
input("Pressione Enter para fechar o navegador...")
#driver.quit()




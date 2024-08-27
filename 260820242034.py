# Bibliotecas
import time
from datetime import datetime
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException, UnexpectedAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, NoAlertPresentException
import pyautogui as p
import clipboard as c
import pyperclip as pp
import tkinter as tk
from tkinter import simpledialog, ttk
import os
import winsound

# Início da contagem do tempo
start_time = time.time()  # Início do cronômetro
print("Execucao iniciada em:", datetime.now())


class Atalho:
    def alerta_sonoro():
        # Toca um som de notificação do Windows (Beep)
        frequency = 1000  # Frequência do som, em Hertz (1000 Hz = 1 kHz)
        duration = 2000    # Duração do som, em milissegundos
        winsound.Beep(frequency, duration)

        # Outra opção é usar um som do sistema, como uma notificação de 'Exclamation'
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

    # Funções de automação de teclado e mouse
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

    def home():
        p.hotkey('home')
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

class FuncoesDoPrograma:
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

    def fechar_elementos_e_alertas(driver):
        try:
            # Primeiro, verificamos se há um alerta presente
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
            print("Alerta fechado com sucesso.")
        except TimeoutException:
            print("Nenhum alerta presente.")
        except NoAlertPresentException:
            print("Nenhum alerta para ser fechado.")
        except UnexpectedAlertPresentException as e:
            # Captura o texto do alerta inesperado e fecha o alerta
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            print(f"Alerta inesperado fechado. Texto do alerta: {alert_text}")
        
        # Fechar elementos de sobreposição (modais)
        try:
            sobreposicao_elemento = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="fechar_modal"]'))
            )
            sobreposicao_elemento.click()
            print("Elemento de sobreposição fechado com sucesso.")
        except Exception as e:
            print(f"Nenhum elemento de sobreposição encontrado ou erro ao fechar: {e}")


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

    def btn_incluir_start():
        incluir_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="panel-8"]/div[2]/div/div[3]/button[1]'))
        )
        incluir_btn.click()
        print(f"Botao inicial, para incluir registro de historico, clicado com sucesso")

    def incluir_enviar_dados(driver): 
        attempts = 3
        while attempts > 0:
            try:
                # Encontra o botão e rola a página até ele estar visível
                botao = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="panel-8"]/div[2]/div/div[3]/div[3]/button[1]'))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", botao)
                botao.click()

                # Handle any alerts after submitting
                FuncoesDoPrograma.fechar_elementos_e_alertas(driver)  # Close success or error alerts

                break
            except (ElementClickInterceptedException, StaleElementReferenceException) as e:
                attempts -= 1
                if attempts == 0:
                    raise e


    def seleciona_uf():
        try:
            # Encontra o dropdown de UF pelo xpath
            dropdown_uf = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="cmbUFResidencia"]'))
            )

            # Cria uma instância de Select
            select_uf = Select(dropdown_uf)

            # Seleciona a UF de acordo com o valor da variável 'uf'
            select_uf.select_by_visible_text(uf)  # A variável 'uf' deve conter o nome exato como aparece no dropdown
            print(f"UF '{uf}' selecionada com sucesso.")
        except Exception as e:
            print(f"Erro ao selecionar a UF: {e}")

    def situacao_aprovado(driver, ano):
        try:
            # Obter o ano corrente
            ano_corrente = datetime.now().year

            # Aguarda até que o dropdown 'cmbSituacaoPromocao' esteja presente no DOM
            situacao_elemento = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="cmbSituacaoPromocao"]'))
            )

            # Cria uma instância de Select
            select_situacao = Select(situacao_elemento)

            # Verifica se o ano é o ano corrente
            if int(ano) == ano_corrente:
                # Seleciona a opção 'Cursando' pelo texto visível
                select_situacao.select_by_visible_text('Cursando')
                print("Situação 'Cursando' selecionada.")
            else:
                # Seleciona a opção 'Aprovado' pelo texto visível
                select_situacao.select_by_visible_text('Aprovado')
                print("Situação 'Aprovado' selecionada com sucesso.")
        except NoSuchElementException:
            print("Opção 'Cursando' ou 'Aprovado' não encontrada no dropdown.")
        except Exception as e:
            print(f"Erro ao selecionar a situação: {e}")

    def marcar_checkbox_omitir_media(driver, xpath):
        try:
            # Aguarda até que o elemento esteja presente no DOM e seja clicável
            checkbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            
            # Executa um JavaScript para rolar até o elemento, sem precisar estar visível
            driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", checkbox)
            
            # Verifica se o checkbox já está marcado, caso contrário, clica nele
            if not checkbox.is_selected():
                driver.execute_script("arguments[0].click();", checkbox)  # Usa JavaScript para clicar
            print("Checkbox marcado com sucesso.")
        
        except Exception as e:
            print(f"Erro ao marcar o checkbox: {e}")

    def clicar_botao_incluir_final(driver, xpath):
        try:
            # Espera até que o botão esteja presente no DOM e seja clicável
            botao = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            
            # Executa um JavaScript para rolar até o elemento, caso necessário
            driver.execute_script("arguments[0].scrollIntoView(true);", botao)
            
            # Clica no botão via JavaScript para maior compatibilidade
            driver.execute_script("arguments[0].click();", botao)
            print("Botão clicado com sucesso.")
        
        except Exception as e:
            print(f"Erro ao clicar no botão: {e}")
            
    def clicar_item_gerado(driver, xpath):
        try:
            # Aguarda até que o item esteja presente no DOM e seja clicável
            item = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            
            # Rola até o item estar visível na tela
            driver.execute_script("arguments[0].scrollIntoView(true);", item)
            
            # Clica no item via JavaScript para garantir a interação
            driver.execute_script("arguments[0].click();", item)
            print("Item clicado com sucesso.")
        
        except Exception as e:
            print(f"Erro ao clicar no item: {e}")
            
class SelecionarCurso:
    
    def __init__(self, driver):
        self.driver = driver

    # Método para selecionar EI-EDUCAÇÃO INFANTIL
    def curso_EI_EDUCACAO_INFANTIL(self):
        curso_elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cmbCurso"]'))
        )
        select = Select(curso_elemento)
        select.select_by_visible_text('EI-EDUCAÇÃO INFANTIL')

    # Método para selecionar EF-ENSINO FUNDAMENTAL
    def curso_EF_ENSINO_FUNDAMENTAL(self):
        curso_elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cmbCurso"]'))
        )
        select = Select(curso_elemento)
        select.select_by_visible_text('EF-ENSINO FUNDAMENTAL')

    # Método para selecionar os períodos dentro do curso EI-EDUCAÇÃO INFANTIL
    def periodo_EI_EDUCACAO_INFANTIL(self, agrupamento):
        periodo_elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cmbPeriodo"]'))
        )
        select = Select(periodo_elemento)
        
        # Seleciona o agrupamento desejado
        if agrupamento == 4:
            select.select_by_visible_text('AGRUPAMENTO IV')
        elif agrupamento == 5:
            select.select_by_visible_text('AGRUPAMENTO V')

    # Método para selecionar os períodos dentro do curso EF-ENSINO FUNDAMENTAL
    def periodo_EF_ENSINO_FUNDAMENTAL(self, ano):
        periodo_elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cmbPeriodo"]'))
        )
        select = Select(periodo_elemento)
        
        # Seleciona o ano desejado
        if ano == 1:
            select.select_by_visible_text('1º ANO')
        elif ano == 2:
            select.select_by_visible_text('2º ANO')
        elif ano == 3:
            select.select_by_visible_text('3º ANO')
        elif ano == 4:
            select.select_by_visible_text('4º ANO')
        elif ano == 5:
            select.select_by_visible_text('5º ANO')

class SelecionaMateria:

    def __init__(self, driver):
        self.driver = driver

    # Método para selecionar 1º ou 2º MOMENTO para EI - EDUCAÇÃO INFANTIL (Agrupamento 4 ou 5)
    def momento_EI_EDUCACAO_INFANTIL(self, momento):
        if momento in ["1º MOMENTO", "2º MOMENTO"]:
            disciplina_elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="cmbDisciplina"]'))
            )
            select = Select(disciplina_elemento)
            select.select_by_visible_text(momento)

    # Método para selecionar as disciplinas de EF - ENSINO FUNDAMENTAL (1º ANO a 5º ANO)
    def disciplina_EF_ENSINO_FUNDAMENTAL(self, disciplina):
        disciplinas_validas = [
            "ARTES", "CIÊNCIAS", "CULTURA DE INOVAÇÃO E TECNOLOGIAS", "EDUCAÇÃO FÍSICA",
            "ENSINO RELIGIOSO", "GEOGRAFIA", "HISTÓRIA", "LÍNGUA PORTUGUESA", "MATEMÁTICA"
        ]
        if disciplina in disciplinas_validas:
            disciplina_elemento = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="cmbDisciplina"]'))
            )
            select = Select(disciplina_elemento)
            select.select_by_visible_text(disciplina)

    # Método para selecionar os períodos dentro do curso EF-ENSINO FUNDAMENTAL
    def processar_disciplina(self, disciplina, nota):
        # Seleciona a disciplina
        self.disciplina_EF_ENSINO_FUNDAMENTAL(disciplina) or print(f'Disciplina {disciplina} selecionada')

        # Obter o ano corrente
        ano_corrente = datetime.now().year

        # Verifica se o ano é o ano corrente
        if int(ano) == ano_corrente:
            try:
                # Rola até o dropdown usando JavaScript para garantir que esteja visível
                situacao_elemento = self.driver.find_element(By.XPATH, '//*[@id="cmbSituacaoPromocao"]')
                self.driver.execute_script("arguments[0].scrollIntoView(true);", situacao_elemento)

                # Aguarda até que o dropdown esteja presente e clicável
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cmbSituacaoPromocao"]')))

                # Usa a classe Select para interagir com o dropdown
                select_situacao = Select(situacao_elemento)
                
                # Tenta selecionar a opção "Cursando"
                select_situacao.select_by_visible_text('Cursando')
                print("Situação 'Cursando' selecionada.")
            
            except NoSuchElementException:
                print("Opção 'Cursando' não encontrada no dropdown.")
        else:
            # Seleciona a situação "Aprovado"
            FuncoesDoPrograma.situacao_aprovado() or print('Situação APROVADO selecionada')

        # Continuar com o restante do código...
        FuncoesDoPrograma.escrever_texto(self.driver, '//*[@id="txtCHTotal"]', carga_horaria) or print('Carga horária escrita')

        # Se a nota estiver em branco, preenche com "0" e marca o checkbox
        if nota == "":
            nota = "0"
            FuncoesDoPrograma.escrever_texto(self.driver, '//*[@id="txtMedia"]', nota) or print(f'Nota da matéria {disciplina} escrita com 0')
            FuncoesDoPrograma.marcar_checkbox_omitir_media(self.driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input') or print('Checkbox Omitir Média marcado')
        else:
            # Se a nota tiver valor, apenas escreve a nota e não marca o checkbox
            FuncoesDoPrograma.escrever_texto(self.driver, '//*[@id="txtMedia"]', nota) or print(f'Nota da matéria {disciplina} escrita')

        # Finaliza a inclusão da disciplina
        FuncoesDoPrograma.clicar_botao_incluir_final(self.driver, '//*[@id="panel-8"]/div[2]/div/div[3]/div[3]/button[1]') or print('Botão incluir final clicado')
        FuncoesDoPrograma.fechar_elementos_e_alertas(self.driver) or print('Janela de alerta fechada')


# Tkinter capturador de dados
def obter_matricula():
    root = tk.Tk()
    root.title("Entrada de Dados")
    
    dados = {}

    def submit():
        dados['numero_matricula'] = numero_matricula_var.get()
        dados['ano'] = ano_var.get()
        dados['nome_escola'] = nome_escola_var.get()
        dados['cidade'] = cidade_var.get()
        dados['uf'] = uf_var.get()
        dados['serie'] = serie_var.get()
        dados['carga_horaria'] = carga_horaria_var.get()
        dados['ja_estudou'] = 'sim' if ja_estudou_var.get() else 'nao'
        dados['ficha_descritiva'] = 'sim' if ficha_descritiva_var.get() else 'nao'
        dados['observacoes'] = observacoes_var.get()  # Isso vai armazenar True ou False diretamente
        dados['txt_observacoes'] = txt_observacoes_var.get()


        # Coleta dos valores das disciplinas se a checkbox estiver marcada
        if marcar_disciplinas_var.get():
            for disciplina in disciplinas_vars:
                dados[disciplina] = disciplinas_vars[disciplina].get()
                
            # Captura as notas das disciplinas
            nota_arte = disciplinas_vars["ARTES"].get()
            nota_ciencias = disciplinas_vars["CIÊNCIAS"].get()
            nota_cultura = disciplinas_vars["CULTURA DE INOVAÇÃO E TECNOLOGIAS"].get()
            nota_educacao_fisica = disciplinas_vars["EDUCAÇÃO FÍSICA"].get()
            nota_ensino_religioso = disciplinas_vars["ENSINO RELIGIOSO"].get()
            nota_geografia = disciplinas_vars["GEOGRAFIA"].get()
            nota_historia = disciplinas_vars["HISTÓRIA"].get()
            nota_lingua_portuguesa = disciplinas_vars["LÍNGUA PORTUGUESA"].get()
            nota_matematica = disciplinas_vars["MATEMÁTICA"].get()

            # Armazena as notas no dicionário dados
            dados['nota_arte'] = nota_arte
            dados['nota_ciencias'] = nota_ciencias
            dados['nota_cultura'] = nota_cultura
            dados['nota_educacao_fisica'] = nota_educacao_fisica
            dados['nota_ensino_religioso'] = nota_ensino_religioso
            dados['nota_geografia'] = nota_geografia
            dados['nota_historia'] = nota_historia
            dados['nota_lingua_portuguesa'] = nota_lingua_portuguesa
            dados['nota_matematica'] = nota_matematica

        root.quit()  # Termina o mainloop do Tkinter
    
    numero_matricula_var = tk.StringVar()
    ano_var = tk.StringVar()
    nome_escola_var = tk.StringVar(value="ESCOLA MUNICIPAL JARDIM BELA VISTA")
    cidade_var = tk.StringVar(value="APARECIDA DE GOIÂNIA")
    uf_var = tk.StringVar(value="GO")
    serie_var = tk.StringVar()
    carga_horaria_var = tk.StringVar()
    ja_estudou_var = tk.BooleanVar()
    ficha_descritiva_var = tk.BooleanVar()
    observacoes_var = tk.BooleanVar()
    txt_observacoes_var = tk.StringVar()
    marcar_disciplinas_var = tk.BooleanVar()

    ttk.Label(root, text="Número da Matrícula:").grid(row=0, column=0, padx=10, pady=5)
    ttk.Entry(root, textvariable=numero_matricula_var).grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(root, text="Ano:").grid(row=1, column=0, padx=10, pady=5)
    ttk.Entry(root, textvariable=ano_var).grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(root, text="Nome da Escola:").grid(row=2, column=0, padx=10, pady=5)
    ttk.Entry(root, textvariable=nome_escola_var).grid(row=2, column=1, padx=10, pady=5)
    tk.Checkbutton(root, text="Já estudou aqui", variable=ja_estudou_var).grid(row=2, column=2, padx=10, pady=5)

    ttk.Label(root, text="Cidade:").grid(row=3, column=0, padx=10, pady=5)
    ttk.Entry(root, textvariable=cidade_var).grid(row=3, column=1, padx=10, pady=5)

    ttk.Label(root, text="UF:").grid(row=3, column=2, padx=10, pady=5)
    ttk.Entry(root, textvariable=uf_var).grid(row=3, column=3, padx=10, pady=5)

    ttk.Label(root, text="Série:").grid(row=4, column=0, padx=10, pady=5)
    serie_combobox = ttk.Combobox(root, textvariable=serie_var)
    serie_combobox['values'] = ("AGRUPAMENTO 4", "AGRUPAMENTO 5", "1º ANO", "2º ANO", "3º ANO", "4º ANO", "5º ANO")
    serie_combobox.grid(row=4, column=1, padx=10, pady=5)
    tk.Checkbutton(root, text="Ficha Descritiva", variable=ficha_descritiva_var).grid(row=4, column=2, padx=10, pady=5)

    ttk.Label(root, text="Carga Horária:").grid(row=5, column=0, padx=10, pady=5)
    ttk.Entry(root, textvariable=carga_horaria_var).grid(row=5, column=1, padx=10, pady=5)

    tk.Checkbutton(root, text="Observações", variable=observacoes_var).grid(row=6, column=0, padx=10, pady=5)
    ttk.Entry(root, textvariable=txt_observacoes_var).grid(row=6, column=1, padx=10, pady=5)

    # Checkbox para marcar se deseja preencher as disciplinas
    tk.Checkbutton(root, text="Marcar Disciplinas", variable=marcar_disciplinas_var, command=lambda: mostrar_disciplinas()).grid(row=7, column=0, padx=10, pady=5)
    
    # Dicionário para armazenar as variáveis das disciplinas
    disciplinas_vars = {
        "ARTES": tk.StringVar(),
        "CIÊNCIAS": tk.StringVar(),
        "CULTURA DE INOVAÇÃO E TECNOLOGIAS": tk.StringVar(),
        "EDUCAÇÃO FÍSICA": tk.StringVar(),
        "ENSINO RELIGIOSO": tk.StringVar(),
        "GEOGRAFIA": tk.StringVar(),
        "HISTÓRIA": tk.StringVar(),
        "LÍNGUA PORTUGUESA": tk.StringVar(),
        "MATEMÁTICA": tk.StringVar(),
    }

    # Função para mostrar os campos de disciplinas
    def mostrar_disciplinas():
        if marcar_disciplinas_var.get():
            for i, (disciplina, var) in enumerate(disciplinas_vars.items(), start=8):
                ttk.Label(root, text=disciplina + ":").grid(row=i, column=0, padx=10, pady=5)
                ttk.Entry(root, textvariable=var).grid(row=i, column=1, padx=10, pady=5)
        else:
            # Limpar os campos de disciplinas se desmarcado
            for widget in root.grid_slaves():
                if int(widget.grid_info()["row"]) >= 8:
                    widget.grid_forget()

    ttk.Button(root, text="OK", command=submit).grid(row=20, column=0, columnspan=2, pady=10)
    ttk.Button(root, text="CANCELAR", command=root.quit).grid(row=20, column=2, columnspan=2, pady=10)

    root.mainloop()
    root.destroy()
    return dados


class ProcessamentoDeObservacoes:
    
    def decisao_texto(self, ano, escola, cidade, ja_estudou, ficha_descritiva, observacoes, serie):
        ano = int(ano)  # Converte o ano para inteiro
        ano_corrente = datetime.now().year
        
        # Condição para ano menor que 2019
        if ano < 2019:
            return self.processa_ano_menor_2019(escola, cidade, ja_estudou, ficha_descritiva, observacoes)

        # Condição para ano igual a 2020
        elif ano == 2020:
            return self.processa_ano_2020(escola, cidade, ja_estudou, ficha_descritiva, observacoes)

        # Condição para ano igual a 2021
        elif ano == 2021:
            return self.processa_ano_2021(escola, cidade, ja_estudou, ficha_descritiva, observacoes)

        # Condição para o ano corrente
        elif ano == ano_corrente:
            return self.processa_ano_corrente(escola, cidade, ja_estudou, ficha_descritiva, observacoes, serie)

        # Condição para qualquer outro ano
        else:
            return self.processa_ano_padrao(escola, cidade, ja_estudou, ficha_descritiva, observacoes)
    
    def processa_ano_menor_2019(self, escola, cidade, ja_estudou, ficha_descritiva, observacoes):
        # Condição 1: Se 'escola' for 'ESCOLA MUNICIPAL JARDIM BELA VISTA'
        if escola == "ESCOLA MUNICIPAL JARDIM BELA VISTA":
            if ja_estudou == "nao":
                if ficha_descritiva == "sim":
                    return "Aluno(a) avaliado(a) conforme a Resolução Normativa 005/07 CME de Aparecida de Goiânia-GO. Aluno(a) avaliado(a) através de Ficha Descritiva em anexo."
                else:
                    return "Aluno(a) avaliado(a) conforme a Resolução Normativa 005/07 CME de Aparecida de Goiânia-GO."
            else:  # ja_estudou == "sim"
                if ficha_descritiva == "sim":
                    return "Aluno(a) avaliado(a) conforme a Resolução Normativa 005/07 CME. Aluno(a) avaliado(a) através de Ficha Descritiva em anexo."
                else:
                    return "Aluno(a) avaliado(a) conforme a Resolução Normativa 005/07 CME de Aparecida de Goiânia-GO."
        
        else:
            if cidade == "APARECIDA DE GOIÂNIA":
                if ja_estudou == "nao":
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Resolução Normativa 005/07 CME de Aparecida de Goiânia-GO. Aluno(a) avaliado(a) através de Ficha Descritiva em anexo. Histórico transcrito conforme o original."
                    else:
                        return "Aluno(a) avaliado(a) conforme a Resolução Normativa 005/07 CME de Aparecida de Goiânia-GO. Histórico transcrito conforme o original."
                else:  # ja_estudou == "sim"
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Resolução 005/07. Aluno(a) avaliado(a) através de Ficha Descritiva em anexo. Histórico transcrito conforme o original."
                    else:
                        return "Aluno(a) avaliado(a) conforme a Resolução 005/07. Histórico transcrito conforme o original."
            
            elif cidade == "GOIÂNIA":
                if ja_estudou == "nao":
                    if ficha_descritiva == "sim":
                        return ("Aluno(a) avaliado(a) conforme a Proposta pedagógica Ciclos de Formação e Desenvolvimento Humano, regulamentada "
                                "através das resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08. Histórico transcrito conforme o original.")
                    else:
                        return "Aluno(a) avaliado(a) conforme a Proposta pedagógica Ciclos de Formação e Desenvolvimento Humano. Histórico transcrito conforme o original."
                else:  # ja_estudou == "sim"
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Resoluções CEE/GO nº 266. Histórico transcrito conforme o original."
                    else:
                        return "Aluno(a) avaliado(a) conforme a Resoluções CEE/GO nº 266. Histórico transcrito conforme o original."
            
            else:  # cidade != "GOIÂNIA"
                if observacoes:  # Verifica se observacoes é True
                    return f"{observacoes} Histórico rigorosamente transcrito conforme o original."
        
        return "Texto padrão para ano menor que 2019."

    # Métodos placeholders para os outros anos, a serem implementados conforme necessário
    def processa_ano_2020(self, escola, cidade, ja_estudou, ficha_descritiva, observacoes):
        if escola == "ESCOLA MUNICIPAL JARDIM BELA VISTA":
            if ja_estudou == "nao":
                if ficha_descritiva == "sim":
                    return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Aprovado(a) conforme Resolução CME nº 014, de 01 de outubro de 2020, que dispõe sobre a aprovação automática dos alunos devidamente matriculados na Rede Municipal de Ensino de Aparecida de Goiânia. Aluno(a) avaliado(a) através de Ficha Descritiva em anexo."
                else:
                    return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Aprovado(a) conforme Resolução CME nº 014, de 01 de outubro de 2020, que dispõe sobre a aprovação automática dos alunos devidamente matriculados na Rede Municipal de Ensino de Aparecida de Goiânia."
            else:
                if ficha_descritiva == "sim":
                    return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Aprovado(a) conforme Resolução CME nº 014, de 01 de outubro de 2020, que dispõe sobre a aprovação automática dos alunos devidamente matriculados na Rede Municipal de Ensino de Aparecida de Goiânia. Aluno(a) avaliado(a) através de Ficha Descritiva em anexo."
                else:
                    return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Aprovado(a) conforme Resolução CME nº 014, de 01 de outubro de 2020, que dispõe sobre a aprovação automática dos alunos devidamente matriculados na Rede Municipal de Ensino de Aparecida de Goiânia."
        else:
            if cidade == "APARECIDA DE GOIÂNIA":
                if ja_estudou == "nao":
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Aprovado(a) conforme Resolução CME nº 014, de 01 de outubro de 2020, que dispõe sobre a aprovação automática dos alunos devidamente matriculados na Rede Municipal de Ensino de Aparecida de Goiânia. Aluno(a) avaliado(a) através de Ficha Descritiva em anexo. Histórico rigorosamente transcrito conforme o original."
                    else:
                        return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Aprovado(a) conforme Resolução CME nº 014, de 01 de outubro de 2020, que dispõe sobre a aprovação automática dos alunos devidamente matriculados na Rede Municipal de Ensino de Aparecida de Goiânia. Histórico rigorosamente transcrito conforme o original."
                else:
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Aprovado(a) conforme Resolução CME nº 014, de 01 de outubro de 2020, que dispõe sobre a aprovação automática dos alunos devidamente matriculados na Rede Municipal de Ensino de Aparecida de Goiânia. Aluno(a) avaliado(a) através de Ficha Descritiva em anexo. Histórico rigorosamente transcrito conforme o original."
                    else:
                        return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Aprovado(a) conforme Resolução CME nº 014, de 01 de outubro de 2020, que dispõe sobre a aprovação automática dos alunos devidamente matriculados na Rede Municipal de Ensino de Aparecida de Goiânia. Histórico rigorosamente transcrito conforme o original."
            elif cidade == "GOIÂNIA":
                if ja_estudou == "nao":
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Proposta pedagógica Ciclos de Formação e Desenvolvimento Humano, regulamentada através das resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08. Histórico transcrito conforme o original."
                    else:
                        return "Aluno(a) avaliado(a) conforme a Proposta pedagógica Ciclos de Formação e Desenvolvimento Humano, regulamentada através das resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08. Histórico transcrito conforme o original."
                else:
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08. Nos ciclos, a avaliação é descritiva em anexo. Histórico transcrito conforme o original."
                    else:
                        return "Aluno(a) avaliado(a) conforme a Resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08. Nos ciclos, a avaliação é descritiva, no entanto tal documento não se fez presente anexo ao documento recebido. Histórico transcrito conforme o original."
            else:
                if observacoes:
                    return f"{observacoes} Histórico rigorosamente transcrito conforme o original."
        return "Texto padrão para o ano de 2020."

    def processa_ano_2021(self, escola, cidade, ja_estudou, ficha_descritiva, observacoes):
        if escola == "ESCOLA MUNICIPAL JARDIM BELA VISTA":
            if ja_estudou == "nao":
                if ficha_descritiva == "sim":
                    return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Resolução CME nº. 011, de 25 de novembro de 2019, que estabelece diretrizes e normas para as etapas e modalidades da Educação Básica e procedimentos para credenciamento, recredenciamento, autorização e renovação de funcionamento de instituições educacionais do Sistema Municipal de Ensino de Aparecida de Goiânia. Aluno(a) avaliado(a) através de Ficha Descritiva em anexo."
                else:
                    return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Resolução CME nº. 011, de 25 de novembro de 2019, que estabelece diretrizes e normas para as etapas e modalidades da Educação Básica e procedimentos para credenciamento, recredenciamento, autorização e renovação de funcionamento de instituições educacionais do Sistema Municipal de Ensino de Aparecida de Goiânia."
            else:
                if ficha_descritiva == "sim":
                    return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Resolução 011/2019. Aluno(a) avaliado(a) através de Ficha Descritiva em anexo."
                else:
                    return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Resolução 011/2019."
        else:
            if cidade == "APARECIDA DE GOIÂNIA":
                if ja_estudou == "nao":
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Resolução CME nº. 011, de 25 de novembro de 2019, que estabelece diretrizes e normas para as etapas e modalidades da Educação Básica e procedimentos para credenciamento, recredenciamento, autorização e renovação de funcionamento de instituições educacionais do Sistema Municipal de Ensino de Aparecida de Goiânia. Aluno(a) avaliado(a) através de Ficha Descritiva, em anexo. Histórico transcrito conforme o original."
                    else:
                        return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Resolução CME nº. 011, de 25 de novembro de 2019, que estabelece diretrizes e normas para as etapas e modalidades da Educação Básica e procedimentos para credenciamento, recredenciamento, autorização e renovação de funcionamento de instituições educacionais do Sistema Municipal de Ensino de Aparecida de Goiânia. Histórico transcrito conforme o original."
                else:
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Resolução 011/2019. Aluno(a) avaliado(a) através de Ficha Descritiva, em anexo. Histórico transcrito conforme o original."
                    else:
                        return "Aluno(a) avaliado(a) conforme a Resolução nº 004/2020 Dispõe sobre o regime especial de aulas não presenciais (REANP) no Sistema de Ensino do município de Aparecida de Goiânia, como medida preventiva à disseminação do COVID-19. Resolução 011/2019. Histórico transcrito conforme o original."
            elif cidade == "GOIÂNIA":
                if ja_estudou == "nao":
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Proposta pedagógica Ciclos de Formação e Desenvolvimento Humano, regulamentada através das resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08, compreendendo os períodos da infância = Ciclo I / pré-adolescência = Ciclo II / adolescência = Ciclo III. Componentes curriculares: Arte, Ciência, Educação Física, Geografia, História, Língua Estrangeira Moderna Inglês, Língua Portuguesa e Matemática. Carga horária anual: 817 / dias letivos: 200. Nos ciclos, a avaliação é descritiva, em anexo. Histórico transcrito conforme o original."
                    else:
                        return "Aluno(a) avaliado(a) conforme a Proposta pedagógica Ciclos de Formação e Desenvolvimento Humano, regulamentada através das resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08, compreendendo os períodos da infância = Ciclo I / pré-adolescência = Ciclo II / adolescência = Ciclo III. Componentes curriculares: Arte, Ciência, Educação Física, Geografia, História, Língua Estrangeira Moderna Inglês, Língua Portuguesa e Matemática. Carga horária anual: 817 / dias letivos: 200. Nos ciclos, a avaliação é descritiva, no entanto tal documento não se fez presente anexo ao documento recebido. Histórico transcrito conforme o original."
                else:
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08. Nos ciclos, a avaliação é descritiva, em anexo. Histórico transcrito conforme o original."
                    else:
                        return "Aluno(a) avaliado(a) conforme a Resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08. Nos ciclos, a avaliação é descritiva, no entanto tal documento não se fez presente anexo ao documento recebido. Histórico transcrito conforme o original."
            else:
                if observacoes:
                    return f"{observacoes} Histórico rigorosamente transcrito conforme o original."
        return "Texto padrão para o ano de 2021."

    def processa_ano_corrente(self, escola, cidade, ja_estudou, ficha_descritiva, observacoes, serie):
        if escola == "ESCOLA MUNICIPAL JARDIM BELA VISTA":
            if ja_estudou == "nao":
                if ficha_descritiva == "sim":
                    return f"Aluno(a) avaliado(a) conforme a Resolução CME nº. 011, de 25 de novembro de 2019, que estabelece diretrizes e normas para as etapas e modalidades da Educação Básica e procedimentos para credenciamento, recredenciamento, autorização e renovação de funcionamento de instituições educacionais do Sistema Municipal de Ensino de Aparecida de Goiânia. Aluno(a) avaliado(a) através de Ficha Descritiva em anexo. Aluno(a) apto(a) a dar continuidade aos estudos no {serie}."
                else:
                    return f"Aluno(a) avaliado(a) conforme a Resolução CME nº. 011, de 25 de novembro de 2019, que estabelece diretrizes e normas para as etapas e modalidades da Educação Básica e procedimentos para credenciamento, recredenciamento, autorização e renovação de funcionamento de instituições educacionais do Sistema Municipal de Ensino de Aparecida de Goiânia. Aluno(a) apto(a) a dar continuidade aos estudos no {serie}."
            else:
                if ficha_descritiva == "sim":
                    return f"Aluno(a) avaliado(a) conforme a Resolução 011/2019. Aluno(a) avaliado(a) através de Ficha Descritiva, em anexo. Aluno(a) apto(a) a dar continuidade aos estudos no {serie}."
                else:
                    return f"Aluno(a) avaliado(a) conforme a Resolução 011/2019. Aluno(a) apto(a) a dar continuidade aos estudos no {serie}."
        else:
            if cidade == "APARECIDA DE GOIÂNIA":
                if ja_estudou == "nao":
                    if ficha_descritiva == "sim":
                        return f"Aluno(a) avaliado(a) conforme a Resolução CME nº. 011, de 25 de novembro de 2019, que estabelece diretrizes e normas para as etapas e modalidades da Educação Básica e procedimentos para credenciamento, recredenciamento, autorização e renovação de funcionamento de instituições educacionais do Sistema Municipal de Ensino de Aparecida de Goiânia. Aluno(a) avaliado(a) através de Ficha Descritiva, em anexo. Histórico transcrito conforme o original. Aluno(a) apto(a) a dar continuidade aos estudos no {serie}."
                    else:
                        return f"Aluno(a) avaliado(a) conforme a Resolução CME nº. 011, de 25 de novembro de 2019, que estabelece diretrizes e normas para as etapas e modalidades da Educação Básica e procedimentos para credenciamento, recredenciamento, autorização e renovação de funcionamento de instituições educacionais do Sistema Municipal de Ensino de Aparecida de Goiânia. Histórico transcrito conforme o original. Aluno(a) apto(a) a dar continuidade aos estudos no {serie}."
                else:
                    if ficha_descritiva == "sim":
                        return f"Aluno(a) avaliado(a) conforme a Resolução 011/2019. Aluno(a) avaliado(a) através de Ficha Descritiva, em anexo. Histórico transcrito conforme o original. Aluno(a) apto(a) a dar continuidade aos estudos no {serie}."
                    else:
                        return f"Aluno(a) avaliado(a) conforme a Resolução 011/2019. Histórico transcrito conforme o original. Aluno(a) apto(a) a dar continuidade aos estudos no {serie}."
            elif cidade == "GOIÂNIA":
                if ja_estudou == "nao":
                    if ficha_descritiva == "sim":
                        return f"Aluno(a) avaliado(a) conforme a Proposta pedagógica Ciclos de Formação e Desenvolvimento Humano, regulamentada através das resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08, compreendendo os períodos da infância = Ciclo I / pré-adolescência = Ciclo II / adolescência = Ciclo III. Componentes curriculares: Arte, Ciência, Educação Física, Geografia, História, Língua Estrangeira Moderna Inglês, Língua Portuguesa e Matemática. Carga horária anual: 800 / dias letivos: 200. Nos ciclos, a avaliação é descritiva, em anexo. Histórico transcrito conforme o original. Aluno(a) apto(a) a dar continuidade aos estudos no {serie}."
                    else:
                        return f"Aluno(a) avaliado(a) conforme a Proposta pedagógica Ciclos de Formação e Desenvolvimento Humano, regulamentada através das resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08, compreendendo os períodos da infância = Ciclo I / pré-adolescência = Ciclo II / adolescência = Ciclo III. Componentes curriculares: Arte, Ciência, Educação Física, Geografia, História, Língua Estrangeira Moderna Inglês, Língua Portuguesa e Matemática. Carga horária anual: 800 / dias letivos: 200. Nos ciclos, a avaliação é descritiva, no entanto tal documento não se fez presente anexo ao documento recebido. Histórico transcrito conforme o original. Aluno(a) apto(a) a dar continuidade aos estudos no {serie}."
                else:
                    if ficha_descritiva == "sim":
                        return f"Aluno(a) avaliado(a) conforme a Resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08. Nos ciclos, a avaliação é descritiva, em anexo. Histórico transcrito conforme o original. Aluno(a) apto(a) a dar continuidade aos estudos no {serie}."
                    else:
                        return f"Aluno(a) avaliado(a) conforme a Resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08. Nos ciclos, a avaliação é descritiva, no entanto tal documento não se fez presente anexo ao documento recebido. Histórico transcrito conforme o original. Aluno(a) apto(a) a dar continuidade aos estudos no {serie}."
            else:
                if observacoes:
                    return f"{observacoes} Histórico rigorosamente transcrito conforme o original. Aluno(a) apto(a) a dar continuidade aos estudos no {serie}."
        return f"Texto padrão para o ano corrente. Aluno(a) apto(a) a dar continuidade aos estudos no {serie}."

    def processa_ano_padrao(self, escola, cidade, ja_estudou, ficha_descritiva, observacoes):
        if escola == "ESCOLA MUNICIPAL JARDIM BELA VISTA":
            if ja_estudou == "nao":
                if ficha_descritiva == "sim":
                    return "Aluno(a) avaliado(a) conforme a Resolução CME nº. 011, de 25 de novembro de 2019, que estabelece diretrizes e normas para as etapas e modalidades da Educação Básica e procedimentos para credenciamento, recredenciamento, autorização e renovação de funcionamento de instituições educacionais do Sistema Municipal de Ensino de Aparecida de Goiânia. Aluno(a) avaliado(a) através de Ficha Descritiva em anexo."
                else:
                    return "Aluno(a) avaliado(a) conforme a Resolução CME nº. 011, de 25 de novembro de 2019, que estabelece diretrizes e normas para as etapas e modalidades da Educação Básica e procedimentos para credenciamento, recredenciamento, autorização e renovação de funcionamento de instituições educacionais do Sistema Municipal de Ensino de Aparecida de Goiânia."
            else:
                if ficha_descritiva == "sim":
                    return "Aluno(a) avaliado(a) conforme a Resolução 011/2019. Aluno(a) avaliado(a) através de Ficha Descritiva, em anexo."
                else:
                    return "Aluno(a) avaliado(a) conforme a Resolução 011/2019."
        else:
            if cidade == "APARECIDA DE GOIÂNIA":
                if ja_estudou == "nao":
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Resolução CME nº. 011, de 25 de novembro de 2019, que estabelece diretrizes e normas para as etapas e modalidades da Educação Básica e procedimentos para credenciamento, recredenciamento, autorização e renovação de funcionamento de instituições educacionais do Sistema Municipal de Ensino de Aparecida de Goiânia. Aluno(a) avaliado(a) através de Ficha Descritiva, em anexo. Histórico transcrito conforme o original."
                    else:
                        return "Aluno(a) avaliado(a) conforme a Resolução CME nº. 011, de 25 de novembro de 2019, que estabelece diretrizes e normas para as etapas e modalidades da Educação Básica e procedimentos para credenciamento, recredenciamento, autorização e renovação de funcionamento de instituições educacionais do Sistema Municipal de Ensino de Aparecida de Goiânia. Histórico transcrito conforme o original."
                else:
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Resolução 011/2019. Aluno(a) avaliado(a) através de Ficha Descritiva, em anexo. Histórico transcrito conforme o original."
                    else:
                        return "Aluno(a) avaliado(a) conforme a Resolução 011/2019. Histórico transcrito conforme o original."
            elif cidade == "GOIÂNIA":
                if ja_estudou == "nao":
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Proposta pedagógica Ciclos de Formação e Desenvolvimento Humano, regulamentada através das resoluções CEE/GO nº 266, de 29-05-98 e CME/Goiânia nº 1240/08."  # Alterei as barras

                    else:
                        return "DEU BOM" #Aluno(a) avaliado(a) conforme a Proposta pedagógica Ciclos de Formação e Desenvolvimento Humano, regulamentada através das resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08, compreendendo os períodos da infância = Ciclo I / pré-adolescência = Ciclo II / adolescência = Ciclo III. Componentes curriculares: Arte, Ciência, Educação Física, Geografia, História, Língua Estrangeira Moderna Inglês, Língua Portuguesa e Matemática. Carga horária anual: 800 / dias letivos: 200. Nos ciclos, a avaliação é descritiva, no entanto tal documento não se fez presente anexo ao documento recebido. Histórico transcrito conforme o original."
                else:
                    if ficha_descritiva == "sim":
                        return "Aluno(a) avaliado(a) conforme a Resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08. Nos ciclos, a avaliação é descritiva, em anexo. Histórico transcrito conforme o original."
                    else:
                        return "Aluno(a) avaliado(a) conforme a Resoluções CEE/GO nº 266, de 29/05/98 e CME/Goiânia nº 1240/08. Nos ciclos, a avaliação é descritiva, no entanto tal documento não se fez presente anexo ao documento recebido. Histórico transcrito conforme o original."
            else:
                if observacoes:
                    return f"{observacoes} Histórico rigorosamente transcrito conforme o original."
        return "Texto padrão para qualquer outro ano."

def escrever_observacoes(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria):
    # Cria uma instância da classe ProcessamentoDeObservacoes
    processamento = ProcessamentoDeObservacoes()
    
    # Chama a função decisao_texto para gerar o texto baseado nas condições
    observacoes_geradas = processamento.decisao_texto(ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie)
    
    # Adiciona um print para verificar o texto gerado
    print(f"Texto gerado para observações: {observacoes_geradas}")
    
    # Escreve o valor da variável 'carga_horaria' na caixa de texto '//*[@id="txtCHTotal"]'
    FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtCHTotal"]', carga_horaria)
    
    # Verifica se o campo de observações está disponível antes de escrever o texto
    try:
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtObservacao"]', observacoes_geradas)
        print("Texto escrito com sucesso no campo de observações.")
    except Exception as e:
        print(f"Erro ao escrever no campo de observações: {e}")
def definir_media_pela_disciplina(driver, disciplina_selecionada, notas):
    try:
        # Aguarda até que o dropdown 'cmbDisciplina' esteja presente no DOM
        disciplina_elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cmbDisciplina"]'))
        )

        # Cria uma instância de Select
        select_disciplina = Select(disciplina_elemento)

        # Seleciona a disciplina pelo texto visível
        select_disciplina.select_by_visible_text(disciplina_selecionada)
        print(f"Disciplina '{disciplina_selecionada}' selecionada com sucesso.")

        # Aguarda até que o campo de média 'txtMedia' esteja presente no DOM
        media_elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="txtMedia"]'))
        )
        
        # Define o valor da média com base na disciplina selecionada
        if disciplina_selecionada in ["1º MOMENTO", "2º MOMENTO"]:
            media_elemento.clear()
            media_elemento.send_keys("0")
            print("Média '0' definida para '1º MOMENTO' ou '2º MOMENTO'.")
        else:
            # Obtem o valor da disciplina a partir da função 'obter_matricula'
            media = notas.get(disciplina_selecionada, "0")  # Retorna "0" se a nota não for encontrada
            media_elemento.clear()
            media_elemento.send_keys(str(media))
            print(f"Média '{media}' definida para a disciplina '{disciplina_selecionada}'.")

    except Exception as e:
        print(f"Erro ao definir a média para a disciplina '{disciplina_selecionada}': {e}")
        
def combo_cadastramento_dados(driver, ano, nome_escola, cidade, uf, carga_horaria, txt_observacoes, serie, ja_estudou, ficha_descritiva):
    # Chama a função decisao_texto para gerar o texto baseado nas condições
    observacoes_geradas = decisao_texto(ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie)
    
    # Adiciona um print para verificar o texto gerado
    print(f"Texto gerado para observações: {observacoes_geradas}")

    # Escreve o valor da variável 'carga_horaria' na caixa de texto '//*[@id="txtCHTotal"]'
    FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtCHTotal"]', carga_horaria)

    # Verifica se o campo de observações está disponível antes de escrever o texto
    try:
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtObservacao"]', observacoes_geradas)
        print("Texto escrito com sucesso no campo de observações.")
    except Exception as e:
        print(f"Erro ao escrever no campo de observações: {e}")


    # Seleciona a opção no item de xpath '//*[@id="cmbSituacaoPromocao"]'
    situacao_elemento = driver.find_element(By.XPATH, '//*[@id="cmbSituacaoPromocao"]')
    situacao_elemento.click()
    situacao_elemento.find_element(By.XPATH, "//option[text()='Aprovado']").click()


    # Marca o checkbox no item de xpath '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input'
    FuncoesDoPrograma.marcar_checkbox(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input')

    # Escreve zero (0) na caixa de texto '//*[@id="txtMedia"]'
    FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtMedia"]', '0')

    # Chama funções end() e incluir_enviar_dados(driver)
    
    FuncoesDoPrograma.incluir_enviar_dados(driver)
    
    # Segundo bloco de repetição
    
    # Seleciona a opção no item de xpath '//*[@id="cmbCurso"]'
    curso_elemento = driver.find_element(By.XPATH, '//*[@id="cmbCurso"]')
    curso_elemento.click()
    curso_elemento.find_element(By.XPATH, "//option[text()='EI-EDUCAÇÃO INFANTIL']").click()
    
    # Ajusta janela para item estar interável
    Atalho.pagedown()

    # Seleciona a opção no item de xpath '//*[@id="cmbPeriodo"]'
    periodo_elemento = driver.find_element(By.XPATH, '//*[@id="cmbPeriodo"]')
    periodo_elemento.click()
    periodo_elemento.find_element(By.XPATH, "//option[text()='AGRUPAMENTO IV']").click()

    # Seleciona a opção no item de xpath '//*[@id="cmbDisciplina"]'
    disciplina_elemento = driver.find_element(By.XPATH, '//*[@id="cmbDisciplina"]')
    disciplina_elemento.click()
    disciplina_elemento.find_element(By.XPATH, "//option[text()='1º MOMENTO']").click()

    # Seleciona a opção no item de xpath '//*[@id="cmbSituacaoPromocao"]'
    situacao_elemento = driver.find_element(By.XPATH, '//*[@id="cmbSituacaoPromocao"]')
    situacao_elemento.click()
    situacao_elemento.find_element(By.XPATH, "//option[text()='Aprovado']").click()

    FuncoesDoPrograma.marcar_checkbox(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input')
    FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtMedia"]', '0')
    
    FuncoesDoPrograma.incluir_enviar_dados(driver)
    
    # Segundo bloco de repetição
    # Segundo bloco de repetição
    curso_elemento = driver.find_element(By.XPATH, '//*[@id="cmbCurso"]')
    curso_elemento.click()
    curso_elemento.find_element(By.XPATH, "//option[text()='EI-EDUCAÇÃO INFANTIL']").click()

    periodo_elemento = driver.find_element(By.XPATH, '//*[@id="cmbPeriodo"]')
    periodo_elemento.click()
    periodo_elemento.find_element(By.XPATH, "//option[text()='AGRUPAMENTO IV']").click()

    disciplina_elemento = driver.find_element(By.XPATH, '//*[@id="cmbDisciplina"]')
    disciplina_elemento.click()
    disciplina_elemento.find_element(By.XPATH, "//option[text()='2º MOMENTO']").click()

    situacao_elemento = driver.find_element(By.XPATH, '//*[@id="cmbSituacaoPromocao"]')
    situacao_elemento.click()
    situacao_elemento.find_element(By.XPATH, "//option[text()='Aprovado']").click()

    FuncoesDoPrograma.marcar_checkbox(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input')
    FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtMedia"]', '0')
    
    FuncoesDoPrograma.incluir_enviar_dados(driver)



class SerieEscolhida:
    @staticmethod
    def agrupamento4(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria):
        print("executada logica para agrupamento 4")
        FuncoesDoPrograma.seleciona_terceira_janela(driver) or print('terceira janela selecionada')
        FuncoesDoPrograma.btn_incluir_start() or print('botao incluir clicado')
        FuncoesDoPrograma.escrever_ano_na_caixa(driver, ano) or print('ano escrito na caixa')
        seletor.curso_EI_EDUCACAO_INFANTIL() or print('educacao infantil selecionado')
        seletor.periodo_EI_EDUCACAO_INFANTIL(4) or print('agrupamento 4 selecionado')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtEscola"]', nome_escola) or print('nome da escola escrito')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtCidade"]', cidade) or print('nome da cidade escrito') # Escreve o valor da variável 'cidade' na caixa de texto '//*[@id="txtCidade"]'
        FuncoesDoPrograma.seleciona_uf() or print('uf escrito')
        escrever_observacoes(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria) or print('observações escritas')
        seletor_materia = SelecionaMateria(driver) 
        seletor_materia.momento_EI_EDUCACAO_INFANTIL("1º MOMENTO") or print('1º MOMENTO selecionado')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtCHTotal"]', carga_horaria) or print('carga horaria escrita') # Escreve o valor da variável 'carga horaria' na caixa de texto ''//*[@id="txtCHTotal"]'
        FuncoesDoPrograma.situacao_aprovado(driver, ano) or print('Situação selecionada com base no ano.')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtMedia"]', '0') or print('campo (obrigatorio) de media escrito 0')
        FuncoesDoPrograma.marcar_checkbox_omitir_media(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input') or print('checkbox omitir media marcado')
        FuncoesDoPrograma.clicar_botao_incluir_final(driver, '//*[@id="panel-8"]/div[2]/div/div[3]/div[3]/button[1]') or print('botao incluir final clicado')
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('janela de alerta fechada')
        seletor.curso_EI_EDUCACAO_INFANTIL() or print('educacao infantil selecionado')
        seletor.periodo_EI_EDUCACAO_INFANTIL(4) or print('agrupamento 4 selecionado')
        seletor_materia.momento_EI_EDUCACAO_INFANTIL("2º MOMENTO") or print('2º MOMENTO selecionado')
        FuncoesDoPrograma.situacao_aprovado(driver, ano) or print('Situação selecionada com base no ano.')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtMedia"]', '0') or print('campo (obrigatorio) de media escrito 0')
        FuncoesDoPrograma.marcar_checkbox_omitir_media(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input') or print('checkbox omitir media marcado - 2º momento')
        FuncoesDoPrograma.clicar_botao_incluir_final(driver, '//*[@id="panel-8"]/div[2]/div/div[3]/div[3]/button[1]') or print('botao incluir final clicado')
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('janela de alerta fechada')
        FuncoesDoPrograma.clicar_item_gerado(driver, '//*[@id="panel-1"]/div[2]/div/div/table/tbody/tr[1]/td[3]') or print('1º momento clicado para marcar ckeckbox')
        FuncoesDoPrograma.marcar_checkbox_omitir_media(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input') or print('checkbox omitir media marcado - 1º momento')
        FuncoesDoPrograma.clicar_botao_incluir_final(driver, '//*[@id="panel-8"]/div[2]/div/div[3]/div[3]/button[1]') or print('botao incluir final clicado')
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('janela de alerta fechada')
        
    @staticmethod
    def agrupamento5(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria):
        print("executada logica para agrupamento 5")
        FuncoesDoPrograma.seleciona_terceira_janela(driver) or print('terceira janela selecionada')
        FuncoesDoPrograma.btn_incluir_start() or print('botao incluir clicado')
        FuncoesDoPrograma.escrever_ano_na_caixa(driver, ano) or print('ano escrito na caixa')
        seletor.curso_EI_EDUCACAO_INFANTIL() or print('educacao infantil selecionado')
        seletor.periodo_EI_EDUCACAO_INFANTIL(5) or print('agrupamento 5 selecionado')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtEscola"]', nome_escola) or print('nome da escola escrito')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtCidade"]', cidade) or print('nome da cidade escrito') # Escreve o valor da variável 'cidade' na caixa de texto '//*[@id="txtCidade"]'
        FuncoesDoPrograma.seleciona_uf() or print('uf escrito')
        escrever_observacoes(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria) or print('observações escritas')
        seletor_materia = SelecionaMateria(driver) 
        seletor_materia.momento_EI_EDUCACAO_INFANTIL("1º MOMENTO") or print('1º MOMENTO selecionado')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtCHTotal"]', carga_horaria) or print('carga horaria escrita') # Escreve o valor da variável 'carga horaria' na caixa de texto ''//*[@id="txtCHTotal"]'
        FuncoesDoPrograma.situacao_aprovado(driver, ano) or print('Situação selecionada com base no ano.')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtMedia"]', '0') or print('campo (obrigatorio) de media escrito 0')
        FuncoesDoPrograma.marcar_checkbox_omitir_media(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input') or print('checkbox omitir media marcado')
        FuncoesDoPrograma.clicar_botao_incluir_final(driver, '//*[@id="panel-8"]/div[2]/div/div[3]/div[3]/button[1]') or print('botao incluir final clicado')
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('janela de alerta fechada')
        seletor.curso_EI_EDUCACAO_INFANTIL() or print('educacao infantil selecionado')
        seletor.periodo_EI_EDUCACAO_INFANTIL(5) or print('agrupamento 5 selecionado')
        seletor_materia.momento_EI_EDUCACAO_INFANTIL("2º MOMENTO") or print('2º MOMENTO selecionado')
        FuncoesDoPrograma.situacao_aprovado(driver, ano) or print('Situação selecionada com base no ano.')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtMedia"]', '0') or print('campo (obrigatorio) de media escrito 0')
        FuncoesDoPrograma.marcar_checkbox_omitir_media(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input') or print('checkbox omitir media marcado - 2º momento')
        FuncoesDoPrograma.clicar_botao_incluir_final(driver, '//*[@id="panel-8"]/div[2]/div/div[3]/div[3]/button[1]') or print('botao incluir final clicado')
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('janela de alerta fechada')
        FuncoesDoPrograma.clicar_item_gerado(driver, '//*[@id="panel-1"]/div[2]/div/div/table/tbody/tr/td[1]') or print('ARTE clicado para marcar ckeckbox')
        FuncoesDoPrograma.marcar_checkbox_omitir_media(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input') or print('checkbox omitir media marcado - 1º momento')
        FuncoesDoPrograma.clicar_botao_incluir_final(driver, '//*[@id="panel-8"]/div[2]/div/div[3]/div[3]/button[1]') or print('botao incluir final clicado')
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('janela de alerta fechada')

    @staticmethod
    def ano1(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria, dados):
        print("executada logica para 1 ANO")
        FuncoesDoPrograma.seleciona_terceira_janela(driver) or print('terceira janela selecionada')
        FuncoesDoPrograma.btn_incluir_start() or print('botao incluir clicado')
        FuncoesDoPrograma.escrever_ano_na_caixa(driver, ano) or print('ano escrito na caixa')
        seletor.curso_EF_ENSINO_FUNDAMENTAL() or print('Ensino Fundamental selecionado')
        seletor.periodo_EF_ENSINO_FUNDAMENTAL(1) or print('1º ano selecionado')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtEscola"]', nome_escola) or print('nome da escola escrito')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtCidade"]', cidade) or print('nome da cidade escrito') # Escreve o valor da variável 'cidade' na caixa de texto '//*[@id="txtCidade"]'
        FuncoesDoPrograma.seleciona_uf() or print('uf escrito')
        escrever_observacoes(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria) or print('observações escritas')
        
        # Instanciando a classe SelecionaMateria
        seletor_materia = SelecionaMateria(driver)
        
        # Processamento das disciplinas usando os dados coletados
        disciplinas_notas = {
            "ARTES": dados['nota_arte'],
            "CIÊNCIAS": dados['nota_ciencias'],
            "CULTURA DE INOVAÇÃO E TECNOLOGIAS": dados['nota_cultura'],
            "EDUCAÇÃO FÍSICA": dados['nota_educacao_fisica'],
            "ENSINO RELIGIOSO": dados['nota_ensino_religioso'],
            "GEOGRAFIA": dados['nota_geografia'],
            "HISTÓRIA": dados['nota_historia'],
            "LÍNGUA PORTUGUESA": dados['nota_lingua_portuguesa'],
            "MATEMÁTICA": dados['nota_matematica']
        }
        
        for disciplina, nota in disciplinas_notas.items():
            seletor_materia.processar_disciplina(disciplina, nota)

        # Passo final após todas as disciplinas terem sido processadas
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('janela de alerta fechada')
        FuncoesDoPrograma.clicar_item_gerado(driver, '//*[@id="panel-1"]/div[2]/div/div/table/tbody/tr[1]/td[1]') or print('1º momento clicado para marcar checkbox')
        FuncoesDoPrograma.marcar_checkbox_omitir_media(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input') or print('checkbox omitir media marcado - 1º momento')
        FuncoesDoPrograma.clicar_botao_incluir_final(driver, '//*[@id="panel-8"]/div[2]/div/div[3]/div[3]/button[1]') or print('botao incluir final clicado')
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('janela de alerta fechada')

    @staticmethod
    def ano2(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria, dados):
        print("Executada lógica para 2º ANO")
        
        # Seleciona a terceira janela aberta
        FuncoesDoPrograma.seleciona_terceira_janela(driver) or print('Terceira janela selecionada')
        
        # Clica no botão para incluir um novo registro
        FuncoesDoPrograma.btn_incluir_start() or print('Botão incluir clicado')
        
        # Escreve o ano na caixa correspondente
        FuncoesDoPrograma.escrever_ano_na_caixa(driver, ano) or print('Ano escrito na caixa')
        
        # Seleciona o curso e o período para o 2º ano
        seletor.curso_EF_ENSINO_FUNDAMENTAL() or print('Ensino Fundamental selecionado')
        seletor.periodo_EF_ENSINO_FUNDAMENTAL(2) or print('2º ano selecionado')
        
        # Preenche informações da escola, cidade e UF
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtEscola"]', nome_escola) or print('Nome da escola escrito')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtCidade"]', cidade) or print('Nome da cidade escrito')
        FuncoesDoPrograma.seleciona_uf() or print('UF selecionada')
        
        # Escreve as observações
        escrever_observacoes(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria) or print('Observações escritas')
        
        # Instancia a classe SelecionaMateria para processar as disciplinas
        seletor_materia = SelecionaMateria(driver)
        
        # Processamento das disciplinas usando os dados coletados
        disciplinas_notas = {
            "ARTES": dados['nota_arte'],
            "CIÊNCIAS": dados['nota_ciencias'],
            "CULTURA DE INOVAÇÃO E TECNOLOGIAS": dados['nota_cultura'],
            "EDUCAÇÃO FÍSICA": dados['nota_educacao_fisica'],
            "ENSINO RELIGIOSO": dados['nota_ensino_religioso'],
            "GEOGRAFIA": dados['nota_geografia'],
            "HISTÓRIA": dados['nota_historia'],
            "LÍNGUA PORTUGUESA": dados['nota_lingua_portuguesa'],
            "MATEMÁTICA": dados['nota_matematica']
        }
        
        for disciplina, nota in disciplinas_notas.items():
            seletor_materia.processar_disciplina(disciplina, nota)
        
        # Passo final após todas as disciplinas terem sido processadas
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('Janela de alerta fechada')
        FuncoesDoPrograma.clicar_item_gerado(driver, '//*[@id="panel-1"]/div[2]/div/div/table/tbody/tr[1]/td[1]') or print('1º momento clicado para marcar checkbox')
        FuncoesDoPrograma.marcar_checkbox_omitir_media(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input') or print('Checkbox omitir media marcado - 1º momento')
        FuncoesDoPrograma.clicar_botao_incluir_final(driver, '//*[@id="panel-8"]/div[2]/div/div[3]/div[3]/button[1]') or print('Botão incluir final clicado')
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('Janela de alerta fechada')

    @staticmethod
    def ano3(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria, dados):
        print("Executada lógica para 3º ANO")
        
        # Seleciona a terceira janela aberta
        FuncoesDoPrograma.seleciona_terceira_janela(driver) or print('Terceira janela selecionada')
        
        # Clica no botão para incluir um novo registro
        FuncoesDoPrograma.btn_incluir_start() or print('Botão incluir clicado')
        
        # Escreve o ano na caixa correspondente
        FuncoesDoPrograma.escrever_ano_na_caixa(driver, ano) or print('Ano escrito na caixa')
        
        # Seleciona o curso e o período para o 3º ano
        seletor.curso_EF_ENSINO_FUNDAMENTAL() or print('Ensino Fundamental selecionado')
        seletor.periodo_EF_ENSINO_FUNDAMENTAL(3) or print('3º ano selecionado')
        
        # Preenche informações da escola, cidade e UF
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtEscola"]', nome_escola) or print('Nome da escola escrito')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtCidade"]', cidade) or print('Nome da cidade escrito')
        FuncoesDoPrograma.seleciona_uf() or print('UF selecionada')
        
        # Escreve as observações
        escrever_observacoes(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria) or print('Observações escritas')
        
        # Instancia a classe SelecionaMateria para processar as disciplinas
        seletor_materia = SelecionaMateria(driver)
        
        # Processamento das disciplinas usando os dados coletados
        disciplinas_notas = {
            "ARTES": dados['nota_arte'],
            "CIÊNCIAS": dados['nota_ciencias'],
            "CULTURA DE INOVAÇÃO E TECNOLOGIAS": dados['nota_cultura'],
            "EDUCAÇÃO FÍSICA": dados['nota_educacao_fisica'],
            "ENSINO RELIGIOSO": dados['nota_ensino_religioso'],
            "GEOGRAFIA": dados['nota_geografia'],
            "HISTÓRIA": dados['nota_historia'],
            "LÍNGUA PORTUGUESA": dados['nota_lingua_portuguesa'],
            "MATEMÁTICA": dados['nota_matematica']
        }
        
        for disciplina, nota in disciplinas_notas.items():
            seletor_materia.processar_disciplina(disciplina, nota)
        
        # Passo final após todas as disciplinas terem sido processadas
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('Janela de alerta fechada')
        FuncoesDoPrograma.clicar_item_gerado(driver, '//*[@id="panel-1"]/div[2]/div/div/table/tbody/tr[1]/td[1]') or print('1º momento clicado para marcar checkbox')
        FuncoesDoPrograma.marcar_checkbox_omitir_media(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input') or print('Checkbox omitir media marcado - 1º momento')
        FuncoesDoPrograma.clicar_botao_incluir_final(driver, '//*[@id="panel-8"]/div[2]/div/div[3]/div[3]/button[1]') or print('Botão incluir final clicado')
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('Janela de alerta fechada')

    @staticmethod
    def ano4(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria, dados):
        print("Executada lógica para 4º ANO")
        
        # Seleciona a terceira janela aberta
        FuncoesDoPrograma.seleciona_terceira_janela(driver) or print('Terceira janela selecionada')
        
        # Clica no botão para incluir um novo registro
        FuncoesDoPrograma.btn_incluir_start() or print('Botão incluir clicado')
        
        # Escreve o ano na caixa correspondente
        FuncoesDoPrograma.escrever_ano_na_caixa(driver, ano) or print('Ano escrito na caixa')
        
        # Seleciona o curso e o período para o 4º ano
        seletor.curso_EF_ENSINO_FUNDAMENTAL() or print('Ensino Fundamental selecionado')
        seletor.periodo_EF_ENSINO_FUNDAMENTAL(4) or print('4º ano selecionado')
        
        # Preenche informações da escola, cidade e UF
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtEscola"]', nome_escola) or print('Nome da escola escrito')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtCidade"]', cidade) or print('Nome da cidade escrito')
        FuncoesDoPrograma.seleciona_uf() or print('UF selecionada')
        
        # Escreve as observações
        escrever_observacoes(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria) or print('Observações escritas')
        
        # Instancia a classe SelecionaMateria para processar as disciplinas
        seletor_materia = SelecionaMateria(driver)
        
        # Processamento das disciplinas usando os dados coletados
        disciplinas_notas = {
            "ARTES": dados['nota_arte'],
            "CIÊNCIAS": dados['nota_ciencias'],
            "CULTURA DE INOVAÇÃO E TECNOLOGIAS": dados['nota_cultura'],
            "EDUCAÇÃO FÍSICA": dados['nota_educacao_fisica'],
            "ENSINO RELIGIOSO": dados['nota_ensino_religioso'],
            "GEOGRAFIA": dados['nota_geografia'],
            "HISTÓRIA": dados['nota_historia'],
            "LÍNGUA PORTUGUESA": dados['nota_lingua_portuguesa'],
            "MATEMÁTICA": dados['nota_matematica']
        }
        
        for disciplina, nota in disciplinas_notas.items():
            seletor_materia.processar_disciplina(disciplina, nota)
        
        # Passo final após todas as disciplinas terem sido processadas
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('Janela de alerta fechada')
        FuncoesDoPrograma.clicar_item_gerado(driver, '//*[@id="panel-1"]/div[2]/div/div/table/tbody/tr[1]/td[1]') or print('1º momento clicado para marcar checkbox')
        FuncoesDoPrograma.marcar_checkbox_omitir_media(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input') or print('Checkbox omitir media marcado - 1º momento')
        FuncoesDoPrograma.clicar_botao_incluir_final(driver, '//*[@id="panel-8"]/div[2]/div/div[3]/div[3]/button[1]') or print('Botão incluir final clicado')
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('Janela de alerta fechada')

    @staticmethod
    def ano5(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria, dados):
        print("Executada lógica para 5º ANO")
        
        # Seleciona a terceira janela aberta
        FuncoesDoPrograma.seleciona_terceira_janela(driver) or print('Terceira janela selecionada')
        
        # Clica no botão para incluir um novo registro
        FuncoesDoPrograma.btn_incluir_start() or print('Botão incluir clicado')
        
        # Escreve o ano na caixa correspondente
        FuncoesDoPrograma.escrever_ano_na_caixa(driver, ano) or print('Ano escrito na caixa')
        
        # Seleciona o curso e o período para o 5º ano
        seletor.curso_EF_ENSINO_FUNDAMENTAL() or print('Ensino Fundamental selecionado')
        seletor.periodo_EF_ENSINO_FUNDAMENTAL(5) or print('5º ano selecionado')
        
        # Preenche informações da escola, cidade e UF
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtEscola"]', nome_escola) or print('Nome da escola escrito')
        FuncoesDoPrograma.escrever_texto(driver, '//*[@id="txtCidade"]', cidade) or print('Nome da cidade escrito')
        FuncoesDoPrograma.seleciona_uf() or print('UF selecionada')
        
        # Escreve as observações
        escrever_observacoes(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria) or print('Observações escritas')
        
        # Instancia a classe SelecionaMateria para processar as disciplinas
        seletor_materia = SelecionaMateria(driver)
        
        # Processamento das disciplinas usando os dados coletados
        disciplinas_notas = {
            "ARTES": dados['nota_arte'],
            "CIÊNCIAS": dados['nota_ciencias'],
            "CULTURA DE INOVAÇÃO E TECNOLOGIAS": dados['nota_cultura'],
            "EDUCAÇÃO FÍSICA": dados['nota_educacao_fisica'],
            "ENSINO RELIGIOSO": dados['nota_ensino_religioso'],
            "GEOGRAFIA": dados['nota_geografia'],
            "HISTÓRIA": dados['nota_historia'],
            "LÍNGUA PORTUGUESA": dados['nota_lingua_portuguesa'],
            "MATEMÁTICA": dados['nota_matematica']
        }
        
        for disciplina, nota in disciplinas_notas.items():
            seletor_materia.processar_disciplina(disciplina, nota)
        
        # Passo final após todas as disciplinas terem sido processadas
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('Janela de alerta fechada')
        FuncoesDoPrograma.clicar_item_gerado(driver, '//*[@id="panel-1"]/div[2]/div/div/table/tbody/tr[1]/td[1]') or print('1º momento clicado para marcar checkbox')
        FuncoesDoPrograma.marcar_checkbox_omitir_media(driver, '//*[@id="card_dados_familiares"]/div[2]/div/div[2]/div[4]/div/input') or print('Checkbox omitir media marcado - 1º momento')
        FuncoesDoPrograma.clicar_botao_incluir_final(driver, '//*[@id="panel-8"]/div[2]/div/div[3]/div[3]/button[1]') or print('Botão incluir final clicado')
        FuncoesDoPrograma.fechar_elementos_e_alertas(driver) or print('Janela de alerta fechada')


# CÓDIGO
dados = obter_matricula()
#Atalho.alerta_sonoro()
numero_matricula = dados.get('numero_matricula')

def digita_matricula(driver, numero_matricula):
    # Encontre o campo de digitação pelo xpath e digite o número da matrícula
    campo_matricula = driver.find_element(By.XPATH, '//*[@id="txtMatricula"]')
    campo_matricula.clear()  # Limpa o campo antes de digitar
    campo_matricula.send_keys(numero_matricula)
    campo_matricula.send_keys(Keys.RETURN)

if numero_matricula and len(numero_matricula) == 9:
    driver = FuncoesDoPrograma.abrir_chrome()
    seletor = SelecionarCurso(driver)
    
    FuncoesDoPrograma.logar(driver)
    FuncoesDoPrograma.abrir_novas_abas(driver)
    FuncoesDoPrograma.seleciona_segunda_janela(driver)
    digita_matricula(driver, numero_matricula)
    FuncoesDoPrograma.seleciona_terceira_janela(driver)
    digita_matricula(driver, numero_matricula)
    FuncoesDoPrograma.seleciona_quarta_janela(driver)
    digita_matricula(driver, numero_matricula)
    FuncoesDoPrograma.seleciona_quinta_janela(driver)
    digita_matricula(driver, numero_matricula)
    FuncoesDoPrograma.seleciona_setima_janela(driver)
    digita_matricula(driver, numero_matricula)
    FuncoesDoPrograma.seleciona_terceira_janela(driver)
    
    serie = dados['serie']
    nome_escola = dados['nome_escola']
    cidade = dados['cidade']
    ano = dados['ano']
    uf = dados['uf']
    carga_horaria = dados['carga_horaria']
    ja_estudou = dados['ja_estudou']
    ficha_descritiva = dados['ficha_descritiva']
    observacoes = dados['observacoes']
    txt_observacoes = dados['txt_observacoes']
    
    print(f"Serie: {serie}")
    print(f"Nome da Escola: {nome_escola}")
    print(f"Cidade: {cidade}")
    print(f"Ano: {ano}")
    print(f"UF: {uf}")
    print(f"Carga Horaria: {carga_horaria}")

    if dados['serie'] == "AGRUPAMENTO 4":
        SerieEscolhida.agrupamento4(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria)
    if dados['serie'] == "AGRUPAMENTO 5":
        SerieEscolhida.agrupamento5(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria)
    if dados['serie'] == "1º ANO":
        SerieEscolhida.ano1(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria, dados)
    if dados['serie'] == "2º ANO":
        SerieEscolhida.ano2(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria, dados)
    if dados['serie'] == "3º ANO":
        SerieEscolhida.ano3(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria, dados)
    if dados['serie'] == "4º ANO":
        SerieEscolhida.ano4(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria, dados)
    if dados['serie'] == "5º ANO":
        SerieEscolhida.ano5(driver, ano, nome_escola, cidade, ja_estudou, ficha_descritiva, txt_observacoes, serie, carga_horaria, dados)

    
    Atalho.alerta_sonoro()
    input("Pressione Enter para fechar o navegador...")

    driver.quit()
    
    # Término da contagem do tempo
    end_time = time.time()  # Fim do cronômetro
    elapsed_time = end_time - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    milliseconds = (elapsed_time - int(elapsed_time)) * 1000
    print(f"Tempo decorrido: {int(minutes):02}:{int(seconds):02}.{int(milliseconds):03}")
    


else:
    print("Número de matrícula inválido. Certifique-se de que tenha 9 dígitos.")



'''260820242034
1. 1096 - FuncoesDoPrograma.situacao_aprovado(driver, ano) or print('Situação selecionada com base no ano.')
2. 1104


'''
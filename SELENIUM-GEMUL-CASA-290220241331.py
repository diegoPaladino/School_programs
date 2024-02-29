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


# PROVISORIO : APENAS ENQUANTO SE CONFECCIONA O CÓDIGO
print('########################################################################################################################################################################')


# Contagem do tempo:
start_time = t.time()
current_time = datetime.now()

# Função para coletar os dados do usuário
def collect_data():
    root = tk.Tk()
    root.geometry("700x850")  # Define o tamanho da janela para 800x600 pixels
    root.title("Coleta de Dados")

    # Definir variáveis para armazenar os dados
    matricula = tk.StringVar()
    ano = tk.StringVar()
    ensino = tk.StringVar()
    agrupamento_ano = tk.StringVar()
    data_transferencia = tk.StringVar()
    observacoes = tk.StringVar()
    escola = tk.StringVar(value="ESCOLA MUNICIPAL JARDIM BELA VISTA")  # Valor padrão definido
    municipio = tk.StringVar(value="APARECIDA DE GOIÂNIA")  # Valor padrão definido
    uf = tk.StringVar(value="GO")  # Valor padrão definido
    
    
    # Cria um frame principal para conter todos os outros widgets
    main_frame = ttk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Cria uma barra de rolagem
    scrollbar = ttk.Scrollbar(main_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Cria um canvas e associa a barra de rolagem a ele
    canvas = tk.Canvas(main_frame, yscrollcommand=scrollbar.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=canvas.yview)

    # Cria outro frame que será colocado dentro do canvas
    frame_inside_canvas = ttk.Frame(canvas)

    # Adiciona o frame ao canvas
    canvas.create_window((0, 0), window=frame_inside_canvas, anchor="nw")

    # Configura o canvas para ajustar seu tamanho ao frame
    frame_inside_canvas.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    

    # Criar widgets
    matricula_label = ttk.Label(frame_inside_canvas, text="Matrícula do aluno:")
    matricula_entry = ttk.Entry(frame_inside_canvas, textvariable=matricula)

    ano_label = ttk.Label(frame_inside_canvas, text="Ano para lançamento:")
    ano_entry = ttk.Entry(frame_inside_canvas, textvariable=ano)

    ensino_label = ttk.Label(frame_inside_canvas, text="Ensino:")
    ensino_combobox = ttk.Combobox(frame_inside_canvas, textvariable=ensino, values=["ENSINO INFANTIL", "ENSINO FUNDAMENTAL"])
    
    # Variável para armazenar a escolha do usuário sobre a inserção de notas
    inserir_notas = tk.StringVar(value="não")  # Valor padrão definido como 'não'

    agrupamento_ano_label = ttk.Label(frame_inside_canvas, text="Agrupamento/Ano:")
    agrupamento_ano_combobox = ttk.Combobox(frame_inside_canvas, textvariable=agrupamento_ano)
    agrupamento_ano_combobox['values'] = []

    data_transferencia_label = ttk.Label(frame_inside_canvas, text="Data de transferência (dd/mm):")
    data_transferencia_entry = ttk.Entry(frame_inside_canvas, textvariable=data_transferencia)
    
    # Criar widget para Observações
    observacoes_label = ttk.Label(frame_inside_canvas, text="Observações:")
    observacoes_text = tk.Text(frame_inside_canvas, height=4)  # Altura de 4 linhas, largura ajustável
    data_transferencia_entry = ttk.Entry(frame_inside_canvas, textvariable=observacoes)
    
    escola_label = ttk.Label(frame_inside_canvas, text="Escola:")
    escola_entry = ttk.Entry(frame_inside_canvas, textvariable=escola)
    
    municipio_label = ttk.Label(frame_inside_canvas, text="Município:")
    municipio_entry = ttk.Entry(frame_inside_canvas, textvariable=municipio)
    
    uf_label = ttk.Label(frame_inside_canvas, text="UF:")
    uf_entry = ttk.Entry(frame_inside_canvas, textvariable=uf, width=5)  # Largura definida para acomodar siglas de estados


    # Função para atualizar as opções de agrupamento/ano com base na seleção de ensino
    def update_agrupamento_ano_options(event):
        if ensino.get() == "ENSINO INFANTIL":
            agrupamento_ano_combobox['values'] = ["AGRUPAMENTO 4", "AGRUPAMENTO 5"]
        else:
            agrupamento_ano_combobox['values'] = ["1º ANO", "2º ANO", "3º ANO", "4º ANO", "5º ANO"]

    ensino_combobox.bind("<<ComboboxSelected>>", update_agrupamento_ano_options)

    submit_button = ttk.Button(root, text="Submeter", command=root.quit)
    
    # Variável para armazenar o estado do checkbox
    use_max_hours = tk.BooleanVar(value=False) 
    
    # checkbox para marcação de carga horária total
    def on_checkbox_toggle():
        if use_max_hours.get():
            data_transferencia_entry.config(state=tk.DISABLED)  # Desabilitar o campo de entrada
        else:
            data_transferencia_entry.config(state=tk.NORMAL)  # Habilitar o campo de entrada

    
    
    # Organizar widgets na janela
    matricula_label.pack(pady=10)
    matricula_entry.pack(pady=10, padx=20, fill=tk.X)

    ano_label.pack(pady=10)
    ano_entry.pack(pady=10, padx=20, fill=tk.X)

    ensino_label.pack(pady=10)
    ensino_combobox.pack(pady=10, padx=20, fill=tk.X)

    agrupamento_ano_label.pack(pady=10)
    agrupamento_ano_combobox.pack(pady=10, padx=20, fill=tk.X)

    max_hours_checkbox = ttk.Checkbutton(root, text="Usar carga horária máxima", variable=use_max_hours, command=on_checkbox_toggle)
    max_hours_checkbox.pack(pady=10)
    
    data_transferencia_label.pack(pady=10)
    data_transferencia_entry.pack(pady=10, padx=20, fill=tk.X)
    
    # Organizar o novo widget na janela
    observacoes_label.pack(pady=10)
    observacoes_text.pack(pady=10, padx=20, fill=tk.X)  # Permitir que expanda na horizontal
    
    escola_label.pack(pady=10)
    escola_entry.pack(pady=10, padx=20, fill=tk.X)

    municipio_label.pack(pady=10)
    municipio_entry.pack(pady=10, padx=20, fill=tk.X)

    uf_label.pack(pady=10)
    uf_entry.pack(pady=10, padx=20, fill=tk.X)

    submit_button.pack(pady=20)

    root.mainloop()
    
    # Coletar o texto do campo de Observações antes de destruir a janela
    observacoes = observacoes_text.get("1.0", tk.END).strip()  # Coleta o texto
    

    # Coletar os dados inseridos pelo usuário
    data = {
        "matricula": matricula.get(),
        "ano": ano.get(),
        "ensino": ensino.get(),
        "agrupamento_ano": agrupamento_ano.get(),
        "use_max_hours": use_max_hours.get(),
        "data_transferencia": data_transferencia.get(),
        "escola": escola.get(),
        "municipio": municipio.get(),
        "uf": uf.get(),
        "observacoes": observacoes
        
    }
    
    

    # Agora, adicione as observações ao dicionário 'data'
    #data["observacoes"] = observacoes  # Adiciona as observações ao dicionário

    root.destroy()

    return data

# função que marca o checkbox
def mark_checkbox(driver):
    """Marca o checkbox com nome 'txtMostraNota' usando JavaScript.
    :param driver: Instância do driver do Selenium.
    """
    # Definindo o tempo máximo de espera (por exemplo, 30 segundos)
    wait_time = 10

    try:
        # Espera até que o elemento esteja disponível e visível na página
        checkbox = WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.NAME, "txtMostraNota"))
        )
        
        # Verifica se o checkbox já está marcado
        if not checkbox.is_selected():
            # Se não estiver marcado, usa JavaScript para marcar o checkbox
            driver.execute_script("arguments[0].click();", checkbox)
    except Exception as e:
        print(f"Erro ao tentar marcar o checkbox: {str(e)}")

# função que preenche campo de média com valor 0
def insert_value_in_media_field(driver):
    """Insere o valor "0" no campo de média.
    :param driver: Instância do driver do Selenium.
    """
    # Definindo o tempo máximo de espera (por exemplo, 30 segundos)
    wait_time = 30

    try:
        # Espera até que o elemento esteja disponível e visível na página
        media_field = WebDriverWait(driver, wait_time).until(
            EC.visibility_of_element_located((By.ID, "txtMedia"))
        )
        
        # Limpa qualquer valor existente no campo
        media_field.clear()
        
        # Envia o valor "0" para o campo
        media_field.send_keys("0")
    except Exception as e:
        print(f"Erro ao tentar inserir o valor no campo de média: {str(e)}")

# função que determina se aluno estará CURSANDO ou APROVADO
def selecionar_situacao_com_base_no_ano(driver, ano):
    """
    Esta função seleciona 'Cursando' ou 'Aprovado' no dropdown 'Situação'
    com base no ano fornecido.
    
    Parâmetros:
    - driver: O driver do Selenium.
    - ano: O ano para determinar a situação.
    """
    try:
        # Aguarda até que o elemento 'cmbSituacaoPromocao' esteja disponível
        situacao_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cmbSituacaoPromocao"))
        )
        
        select_situacao = Select(situacao_dropdown)

        # Obtém o ano atual
        current_year = datetime.now().year

        # Se o ano fornecido for o ano atual, selecione "Cursando"
        if int(ano) == current_year:
            select_situacao.select_by_value("CR")
        # Se o ano fornecido for diferente do ano atual, selecione "Aprovado"
        else:
            select_situacao.select_by_value("AP")
    except NoSuchElementException:
        print("Elemento 'cmbSituacaoPromocao' não encontrado.")
    except StaleElementReferenceException:
        print("O elemento não está mais presente na página. A página pode ter sido recarregada.")
    except Exception as e:
        print(f"Erro ao selecionar situação: {e}")

# criando a função clicar no ultimo botao da página: Incluir
def clicar_botao_incluir():
    # Aguarde até que o botão "Incluir" esteja visível
    botao_incluir = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Incluir')]"))
    )
    # Clique no botão
    botao_incluir.click()

# criando a função CALCULADORA
def calcular_carga_horaria(data_transferencia, ensino, use_max_hours):
    if use_max_hours:
        if ensino == "ENSINO INFANTIL":
            return 800
        elif ensino == "ENSINO FUNDAMENTAL":
            return 1000
    else:
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
            2: 3,
            3: 0,
            4: 2,
            5: 1,
            6: 2,
            7: 0,
            8: 0,
            9: 2,
            10: 5,
            11: 3,
            12: 0
        }

        data_transferencia = datetime.strptime(data_transferencia, "%d/%m")

        total_horas = 0
        horas_por_dia = 5  # Default for ENSINO FUNDAMENTAL

        if ensino == "ENSINO INFANTIL":
            horas_por_dia = 4

        # Iterando pelos meses e calculando a carga horária
        for mes, dias in dias_letivos.items():
            if mes < data_transferencia.month:
                total_horas += (dias - feriados_recessos[mes]) * horas_por_dia
            elif mes == data_transferencia.month:
                dias_uteis_mes_atual = data_transferencia.day
                # Se a data de transferência for antes de algum feriado ou recesso, não devemos subtrair esse feriado/recesso
                if mes in [2, 4, 5, 6, 9, 10, 11] and data_transferencia.day <= 15:
                    dias_uteis_mes_atual += feriados_recessos[mes]
                total_horas += dias_uteis_mes_atual * horas_por_dia
                break

        return total_horas

# função para digitar o número de matrícula
def digita_matricula():
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

# função para alterar o ANO que será lançado o histórico
def alterar_ano():
    def click_on_year_field(driver):
        try:
            # Localiza o campo de ano do histórico
            campo_ano_historico = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "txtAnoHistorico"))
            )
            
            # Tenta clicar diretamente no elemento
            campo_ano_historico.click()
            print("Clicou no campo do ano do histórico")
        
        except Exception as e:
            print(f"Erro ao tentar clicar no campo do ano do histórico: {str(e)}")
    click_on_year_field(driver)
    
    # Limpa o campo
    def select_all_in_year_field(driver):
        try:
            # Localiza o campo de ano do histórico
            campo_ano_historico = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "txtAnoHistorico"))
            )
            
            # Clica diretamente no elemento
            campo_ano_historico.click()
            print("Clicou no campo do ano do histórico")
            
            # Tenta selecionar todo o conteúdo do campo
            campo_ano_historico.send_keys(Keys.CONTROL, 'a')
            print("Selecionou todo o conteúdo do campo do ano do histórico")
        
        except Exception as e:
            print(f"Erro ao tentar interagir com o campo do ano do histórico: {str(e)}")

    select_all_in_year_field(driver)


    p.hotkey('backspace')
    t.sleep(0.2)

    # Re-localizando o elemento para evitar StaleElementReferenceException
    campo_ano_historico = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "txtAnoHistorico"))
    )
    campo_ano_historico.send_keys(collected_data["ano"])    # Digita o dado ANO coletado

    # Adicione um pequeno atraso antes de enviar a tecla TAB (se necessário)
    # time.sleep(1)
    campo_ano_historico.send_keys(Keys.TAB)

# função para selecionar o item ENSINO INFANTIL no menu suspenso
def seleciona_educacao_infantil():
    # Selecionando EDUCAÇÃO INFANTIL
    from selenium.webdriver.common.by import By
    dropdown_element = driver.find_element(By.ID, "cmbCurso")
    # Criar um objeto Select a partir do elemento
    select = Select(dropdown_element)
    # Selecionar a opção pelo texto visível
    select.select_by_visible_text("EI-EDUCAÇÃO INFANTIL")

# função para digitar o nome da escola
def alterar_escola():
    def click_on_escola_field(driver):
        try:
            # Localiza o campo de escola
            campo_escola = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "txtEscola"))
            )
            
            # Tenta clicar diretamente no elemento
            campo_escola.click()
            print("Clicou no campo de escola")
        
        except Exception as e:
            print(f"Erro ao tentar clicar no campo de escola: {str(e)}")
            
    click_on_escola_field(driver)
    
    def select_all_in_escola_field(driver):
        try:
            # Re-localiza o campo de escola
            campo_escola = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "txtEscola"))
            )
            
            # Clica diretamente no elemento
            campo_escola.click()
            print("Clicou no campo de escola")
            
            # Tenta selecionar todo o conteúdo do campo
            campo_escola.send_keys(Keys.CONTROL, 'a')
            print("Selecionou todo o conteúdo do campo de escola")
        
        except Exception as e:
            print(f"Erro ao tentar interagir com o campo de escola: {str(e)}")
            
    select_all_in_escola_field(driver)

    p.hotkey('backspace')
    t.sleep(0.2)

    # Re-localizando o elemento para evitar StaleElementReferenceException
    campo_escola = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "txtEscola"))
    )
    campo_escola.send_keys(collected_data["escola"])    # Digita o dado ESCOLA coletado

    # Adicione um pequeno atraso antes de enviar a tecla TAB (se necessário)
    # time.sleep(1)
    campo_escola.send_keys(Keys.TAB)

# função para digitar o nome do município
def alterar_municipio():
    def click_on_cidade_field(driver):
        try:
            # Localiza o campo de cidade
            campo_cidade = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "txtCidade"))
            )
            
            # Tenta clicar diretamente no elemento
            campo_cidade.click()
            print("Clicou no campo de cidade")
        
        except Exception as e:
            print(f"Erro ao tentar clicar no campo de cidade: {str(e)}")
            
    click_on_cidade_field(driver)
    
    def select_all_in_cidade_field(driver):
        try:
            # Re-localiza o campo de cidade
            campo_cidade = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "txtCidade"))
            )
            
            # Clica diretamente no elemento
            campo_cidade.click()
            print("Clicou no campo de cidade")
            
            # Tenta selecionar todo o conteúdo do campo
            campo_cidade.send_keys(Keys.CONTROL, 'a')
            print("Selecionou todo o conteúdo do campo de cidade")
        
        except Exception as e:
            print(f"Erro ao tentar interagir com o campo de cidade: {str(e)}")
            
    select_all_in_cidade_field(driver)

    p.hotkey('backspace')
    t.sleep(0.2)

    # Re-localizando o elemento para evitar StaleElementReferenceException
    campo_cidade = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "txtCidade"))
    )
    campo_cidade.send_keys(collected_data["municipio"])    # Digita o dado MUNICÍPIO coletado

    # Adicione um pequeno atraso antes de enviar a tecla TAB (se necessário)
    # time.sleep(1)
    campo_cidade.send_keys(Keys.TAB)

# função para selecionar o item ENSINO FUNDAMENTAL no menu suspenso
def seleciona_ensino_fundamental():
    # Selecionando EDUCAÇÃO INFANTIL
    from selenium.webdriver.common.by import By
    dropdown_element = driver.find_element(By.ID, "cmbCurso")
    # Criar um objeto Select a partir do elemento
    select = Select(dropdown_element)
    # Selecionar a opção pelo texto visível
    select.select_by_visible_text("EF-ENSINO FUNDAMENTAL")



# Função que escreve a observação de acordo com o ano e condições específicas
def observacao(observacoes_text):
    def click_on_observacao_field(driver):
        try:
            # Localiza o campo de observação
            campo_observacao = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "txtObservacao"))
            )
            # Clica no campo de observação para garantir que está focado
            campo_observacao.click()
            print("Clicou no campo de observação")
            
        except Exception as e:
            print(f"Erro ao tentar clicar no campo de observação: {str(e)}")

    def clear_and_type_in_observacao_field(driver, observacoes_text):
        try:
            # Re-localiza o campo de observação para evitar referências obsoletas
            campo_observacao = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "txtObservacao"))
            )
            # Limpa o campo antes de digitar o novo texto
            campo_observacao.clear()
            print("Campo de observação limpo")
            # Digita o texto de observações
            campo_observacao.send_keys(observacoes_text)
            print("Texto digitado no campo de observação")
        
        except Exception as e:
            print(f"Erro ao tentar digitar no campo de observação: {str(e)}")

    # Primeiro, clica no campo para garantir que ele esteja focado
    click_on_observacao_field(driver)
    # Então, limpa qualquer texto existente e digita o novo texto
    clear_and_type_in_observacao_field(driver, observacoes_text)

    
    
    
    

# função que clica no botão INCLUIR, após os lançamentos de dados na página
def btn_incluir():
    # Clicando no botão 'Incluir (AGRUPAMENTO 4)'
    try:
        botao_incluir = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Incluir']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", botao_incluir)  # Rolar até o botão
        botao_incluir.click()
    except ElementClickInterceptedException:
        # Se o elemento não puder ser clicado diretamente, usaremos o JavaScript para forçar o clique.
        driver.execute_script("arguments[0].click();", botao_incluir)
    except TimeoutException:
        print("Não foi possível encontrar ou clicar no botão 'Incluir'.")

# função que clica no 'OK' do popup confirmando que os dados foram lançados
def popup_ok():
    # clicando no botão OK que aparece avisando que as informações foram salvas
    try:
        # Aguarde até que o alerta esteja presente
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        
        # Mude para o alerta e aceite-o (clique em OK)
        alert = driver.switch_to.alert
        alert.accept()
        
    except NoAlertPresentException:
        print("Nenhum alerta foi encontrado.")

# declaração, pois a função que determina o resultado (carga horária) requer 
collected_data = collect_data()

# Depois de chamar a função, você imprime o resultado
ensino_selecionado = 'ENSINO INFANTIL'  # ou 'ENSINO FUNDAMENTAL', dependendo da seleção no seu sistema
resultado = calcular_carga_horaria(collected_data['data_transferencia'], ensino_selecionado, collected_data['use_max_hours'])
print('Horas calculadas:', resultado)
    
# função que escreve a carga horária no local apropriado para tal
def escreve_carga_horaria(carga_horaria):
    # Localizando o elemento para escrever a carga horária
    campo_ch_total = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "txtCHTotal"))
    )
    campo_ch_total.send_keys(str(carga_horaria))

def seleciona_agrupamento_4():
    # Localizar o elemento do menu suspenso
    dropdown_periodo = driver.find_element(By.ID, "cmbPeriodo")
    # Criar um objeto Select a partir do elemento
    select_periodo = Select(dropdown_periodo)
    # Selecionar a opção pelo texto visível
    select_periodo.select_by_visible_text("AGRUPAMENTO IV")

def seleciona_agrupamento_5():
    # Localizar o elemento do menu suspenso
    dropdown_periodo = driver.find_element(By.ID, "cmbPeriodo")
    # Criar um objeto Select a partir do elemento
    select_periodo = Select(dropdown_periodo)
    # Selecionar a opção pelo texto visível
    select_periodo.select_by_visible_text("AGRUPAMENTO V")

def seleciona_1_ano():
    # Localizar o elemento do menu suspenso
    dropdown_periodo = driver.find_element(By.ID, "cmbPeriodo")
    # Criar um objeto Select a partir do elemento
    select_periodo = Select(dropdown_periodo)
    # Selecionar a opção pelo texto visível
    select_periodo.select_by_visible_text("1º ANO")

def seleciona_2_ano():
    # Localizar o elemento do menu suspenso
    dropdown_periodo = driver.find_element(By.ID, "cmbPeriodo")
    # Criar um objeto Select a partir do elemento
    select_periodo = Select(dropdown_periodo)
    # Selecionar a opção pelo texto visível
    select_periodo.select_by_visible_text("2º ANO")

def seleciona_3_ano():
    # Localizar o elemento do menu suspenso
    dropdown_periodo = driver.find_element(By.ID, "cmbPeriodo")
    # Criar um objeto Select a partir do elemento
    select_periodo = Select(dropdown_periodo)
    # Selecionar a opção pelo texto visível
    select_periodo.select_by_visible_text("3º ANO")
    
def seleciona_4_ano():
    # Localizar o elemento do menu suspenso
    dropdown_periodo = driver.find_element(By.ID, "cmbPeriodo")
    # Criar um objeto Select a partir do elemento
    select_periodo = Select(dropdown_periodo)
    # Selecionar a opção pelo texto visível
    select_periodo.select_by_visible_text("4º ANO")

def seleciona_5_ano():
    # Localizar o elemento do menu suspenso
    dropdown_periodo = driver.find_element(By.ID, "cmbPeriodo")
    # Criar um objeto Select a partir do elemento
    select_periodo = Select(dropdown_periodo)
    # Selecionar a opção pelo texto visível
    select_periodo.select_by_visible_text("5º ANO")

def seleciona_materia_1_momento():
    dropdown = Select(driver.find_element(By.ID, 'cmbDisciplina'))
    dropdown.select_by_visible_text('1º MOMENTO')

def seleciona_materia_2_momento():
    dropdown = Select(driver.find_element(By.ID, 'cmbDisciplina'))
    dropdown.select_by_visible_text('2º MOMENTO')

def seleciona_materia_artes():
    dropdown = Select(driver.find_element(By.ID, 'cmbDisciplina'))
    dropdown.select_by_visible_text('ARTES')

def seleciona_materia_ciencias():
    dropdown = Select(driver.find_element(By.ID, 'cmbDisciplina'))
    dropdown.select_by_visible_text('CIÊNCIAS')

def seleciona_materia_cultura_de_inovacao_e_tecnologias():
    dropdown = Select(driver.find_element(By.ID, 'cmbDisciplina'))
    dropdown.select_by_visible_text('CULTURA DE INOVAÇÃO E TECNOLOGIAS')

def seleciona_materia_educacao_fisica():
    dropdown = Select(driver.find_element(By.ID, 'cmbDisciplina'))
    dropdown.select_by_visible_text('EDUCAÇÃO FÍSICA') 

def seleciona_materia_ensino_religioso():
    dropdown = Select(driver.find_element(By.ID, 'cmbDisciplina'))
    dropdown.select_by_visible_text('ENSINO RELIGIOSO')

def seleciona_materia_geografia():
    dropdown = Select(driver.find_element(By.ID, 'cmbDisciplina'))
    dropdown.select_by_visible_text('GEOGRAFIA')

def seleciona_materia_historia():
    dropdown = Select(driver.find_element(By.ID, 'cmbDisciplina'))
    dropdown.select_by_visible_text('HISTÓRIA')

def seleciona_materia_lingua_portuguesa():
    dropdown = Select(driver.find_element(By.ID, 'cmbDisciplina'))
    dropdown.select_by_visible_text('LÍNGUA PORTUGUESA')
 
def seleciona_materia_matematica():
    dropdown = Select(driver.find_element(By.ID, 'cmbDisciplina'))
    dropdown.select_by_visible_text('MATEMÁTICA')

def seleciona_materia_oficinas_interdisciplinares():
    dropdown = Select(driver.find_element(By.ID, 'cmbDisciplina'))
    dropdown.select_by_visible_text('OFICINAS INTERDISCIPLINARES')

def cadastrar_todas_materias_fundamental():
    seleciona_materia_artes()
    #selecionando situação do aluno
    selecionar_situacao_com_base_no_ano(driver, collected_data["ano"])
    # chama a função responsável por digitar "0" no campo de média
    insert_value_in_media_field(driver)
    # chama a função responsável por marcar o checkbox "omitir resultado"
    mark_checkbox(driver)
    # escreve_carga_horaria
    horas_calculadas = calcular_carga_horaria(collected_data['data_transferencia'], ensino_selecionado, collected_data['use_max_hours'])
    print('Horas calculadas:', horas_calculadas)
    escreve_carga_horaria(horas_calculadas)
    # chama a função observação
    #observacao() #retirado após erro: "TypeError: observacao() missing 1 required positional argument: 'observacoes_text'"
    # chama a função para clicar no botão INCLUIR
    btn_incluir()
    # chama a função para clicar no 'OK' do popup de confirmação
    popup_ok()
    
    # Cadastrando a matéria CIENCIAS
    seleciona_materia_ciencias()
    #selecionando situação do aluno
    selecionar_situacao_com_base_no_ano(driver, collected_data["ano"])
    # chama a função responsável por digitar "0" no campo de média
    insert_value_in_media_field(driver)
    # chama a função responsável por marcar o checkbox "omitir resultado"
    mark_checkbox(driver)
    # chama a função para clicar no botão INCLUIR
    btn_incluir()
    # chama a função para clicar no 'OK' do popup de confirmação
    popup_ok()
    
    # Cadastrando a matéria CULTURA DE INOVAÇÃO E TECNOLOGIAS
    seleciona_materia_cultura_de_inovacao_e_tecnologias()
    #selecionando situação do aluno
    selecionar_situacao_com_base_no_ano(driver, collected_data["ano"])
    # chama a função responsável por digitar "0" no campo de média
    insert_value_in_media_field(driver)
    # chama a função responsável por marcar o checkbox "omitir resultado"
    mark_checkbox(driver)
    # chama a função para clicar no botão INCLUIR
    btn_incluir()
    # chama a função para clicar no 'OK' do popup de confirmação
    popup_ok()
    
    # Cadastrando a matéria EDUCAÇÃO FÍSICA
    seleciona_materia_educacao_fisica()
    #selecionando situação do aluno
    selecionar_situacao_com_base_no_ano(driver, collected_data["ano"])
    # chama a função responsável por digitar "0" no campo de média
    insert_value_in_media_field(driver)
    # chama a função responsável por marcar o checkbox "omitir resultado"
    mark_checkbox(driver)
    # chama a função para clicar no botão INCLUIR
    btn_incluir()
    # chama a função para clicar no 'OK' do popup de confirmação
    popup_ok()
    
    # Cadastrando a matéria ENSINO RELIGIOSO
    seleciona_materia_ensino_religioso()
    #selecionando situação do aluno
    selecionar_situacao_com_base_no_ano(driver, collected_data["ano"])
    # chama a função responsável por digitar "0" no campo de média
    insert_value_in_media_field(driver)
    # chama a função responsável por marcar o checkbox "omitir resultado"
    mark_checkbox(driver)
    # chama a função para clicar no botão INCLUIR
    btn_incluir()
    # chama a função para clicar no 'OK' do popup de confirmação
    popup_ok()
    
    # Cadastrando a matéria GEOGRAFIA
    seleciona_materia_geografia()
    #selecionando situação do aluno
    selecionar_situacao_com_base_no_ano(driver, collected_data["ano"])
    # chama a função responsável por digitar "0" no campo de média
    insert_value_in_media_field(driver)
    # chama a função responsável por marcar o checkbox "omitir resultado"
    mark_checkbox(driver)
    # chama a função para clicar no botão INCLUIR
    btn_incluir()
    # chama a função para clicar no 'OK' do popup de confirmação
    popup_ok()
    
    # Cadastrando a matéria HISTÓRIA
    seleciona_materia_historia()
    #selecionando situação do aluno
    selecionar_situacao_com_base_no_ano(driver, collected_data["ano"])
    # chama a função responsável por digitar "0" no campo de média
    insert_value_in_media_field(driver)
    # chama a função responsável por marcar o checkbox "omitir resultado"
    mark_checkbox(driver)
    # chama a função para clicar no botão INCLUIR
    btn_incluir()
    # chama a função para clicar no 'OK' do popup de confirmação
    popup_ok()
    
    # Cadastrando a matéria LÍNGUA PORTUGUESA
    seleciona_materia_lingua_portuguesa()
    #selecionando situação do aluno
    selecionar_situacao_com_base_no_ano(driver, collected_data["ano"])
    # chama a função responsável por digitar "0" no campo de média
    insert_value_in_media_field(driver)
    # chama a função responsável por marcar o checkbox "omitir resultado"
    mark_checkbox(driver)
    # chama a função para clicar no botão INCLUIR
    btn_incluir()
    # chama a função para clicar no 'OK' do popup de confirmação
    popup_ok()
    
    # Cadastrando a matéria MATEMÁTICA
    seleciona_materia_matematica()
    #selecionando situação do aluno
    selecionar_situacao_com_base_no_ano(driver, collected_data["ano"])
    # chama a função responsável por digitar "0" no campo de média
    insert_value_in_media_field(driver)
    # chama a função responsável por marcar o checkbox "omitir resultado"
    mark_checkbox(driver)
    # chama a função para clicar no botão INCLUIR
    btn_incluir()
    # chama a função para clicar no 'OK' do popup de confirmação
    popup_ok()
    
    # Cadastrando a matéria OFICINAS INTERDISCIPLINARES
    seleciona_materia_oficinas_interdisciplinares()
    #selecionando situação do aluno
    selecionar_situacao_com_base_no_ano(driver, collected_data["ano"])
    # chama a função responsável por digitar "0" no campo de média
    insert_value_in_media_field(driver)
    # chama a função responsável por marcar o checkbox "omitir resultado"
    mark_checkbox(driver)
    # chama a função para clicar no botão INCLUIR
    btn_incluir()
    # chama a função para clicar no 'OK' do popup de confirmação
    popup_ok()

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
# Aguarda a próxima página carregar e clica no ícone desejado  (acadêmico)
wait.until(EC.presence_of_element_located((By.XPATH, "//img[@src='../assets/img/icones/SCA.png']")))
icon = driver.find_element(By.XPATH, "//img[@src='../assets/img/icones/SCA.png']")
icon.click()
# Acessa diretamente a página
driver.get("https://www.gemul-aparecida.com.br/app/sca_historico_escolarCon.asp")
# Espera o campo de matrícula estar disponível para interação

print('Chrome iniciado')

# Aqui se inicia a lógica de lançamentos
#acredito que as funções IF entrariam a partir daqui.
# Verificar o agrupamento escolhido pelo usuário e executar o código correspondente
if collected_data["agrupamento_ano"] == "AGRUPAMENTO 4":
    print('agrupamento 4')
    # chama a função para digitar o número de matrícula
    digita_matricula()
    # Altera o campo de ANO para o número que foi alimentado no tkinter
    alterar_ano()
    # chama a função que seleciona ENSINO INFANTIL
    seleciona_educacao_infantil()
    # chama a função que seleciona AGRUPAMENTO IV
    seleciona_agrupamento_4()
    # chama a função que escreve o nome da escola
    alterar_escola()
    # chama a função que escreve o nome do município
    alterar_municipio()
    #escrever as observações
    observacao(collected_data['observacoes'])
    # chama a função que seleciona a matéria 1º MOMENTO
    seleciona_materia_1_momento()
    #selecionando situação do aluno
    selecionar_situacao_com_base_no_ano(driver, collected_data["ano"])
    # chama a função responsável por digitar "0" no campo de média
    insert_value_in_media_field(driver)
    # chama a função responsável por marcar o checkbox "omitir resultado"
    mark_checkbox(driver)
    # escreve_carga_horaria
    horas_calculadas = calcular_carga_horaria(collected_data['data_transferencia'], ensino_selecionado, collected_data['use_max_hours'])
    print('Horas calculadas:', horas_calculadas)
    escreve_carga_horaria(horas_calculadas)
    # chama a função observação
    observacao()
    # chama a função para clicar no botão INCLUIR
    btn_incluir()
    # chama a função para clicar no 'OK' do popup de confirmação
    popup_ok()
    
    # Início do cadastro do 2º MOMENTO ##############################################
    # chama a função que seleciona ENSINO INFANTIL
    seleciona_educacao_infantil()
    # chama a função que seleciona AGRUPAMENTO IV
    seleciona_agrupamento_4()
    # chama a função que seleciona a matéria 2º MOMENTO
    seleciona_materia_2_momento()
    #selecionando situação do aluno
    selecionar_situacao_com_base_no_ano(driver, collected_data["ano"])
    # chama a função responsável por digitar "0" no campo de média
    insert_value_in_media_field(driver)
    # chama a função responsável por marcar o checkbox "omitir resultado"
    mark_checkbox(driver)
    # chama a função para clicar no botão INCLUIR
    btn_incluir()
    # chama a função para clicar no 'OK' do popup de confirmação
    popup_ok()
    
elif collected_data["agrupamento_ano"] == "AGRUPAMENTO 5":
    print('agrupamento 4')
    # chama a função para digitar o número de matrícula
    digita_matricula()
    # Altera o campo de ANO para o número que foi alimentado no tkinter
    alterar_ano()
    # chama a função que seleciona ENSINO INFANTIL
    seleciona_educacao_infantil()
    # chama a função que seleciona AGRUPAMENTO IV
    seleciona_agrupamento_5()
    # chama a função que escreve o nome da escola
    alterar_escola()
    # chama a função que escreve o nome do município
    alterar_municipio()
    #escrever as observações
    observacao(collected_data['observacoes'])
    # chama a função que seleciona a matéria 1º MOMENTO
    seleciona_materia_1_momento()
    #selecionando situação do aluno
    selecionar_situacao_com_base_no_ano(driver, collected_data["ano"])
    # chama a função responsável por digitar "0" no campo de média
    insert_value_in_media_field(driver)
    # chama a função responsável por marcar o checkbox "omitir resultado"
    mark_checkbox(driver)
    # escreve_carga_horaria
    horas_calculadas = calcular_carga_horaria(collected_data['data_transferencia'], ensino_selecionado, collected_data['use_max_hours'])
    print('Horas calculadas:', horas_calculadas)
    escreve_carga_horaria(horas_calculadas)
    # chama a função observação
    observacao()
    # chama a função para clicar no botão INCLUIR
    btn_incluir()
    # chama a função para clicar no 'OK' do popup de confirmação
    popup_ok()
    
    # Início do cadastro do 2º MOMENTO ##############################################
    # chama a função que seleciona ENSINO INFANTIL
    seleciona_educacao_infantil()
    # chama a função que seleciona AGRUPAMENTO IV
    seleciona_agrupamento_5()
    # chama a função que seleciona a matéria 2º MOMENTO
    seleciona_materia_2_momento()
    #selecionando situação do aluno
    selecionar_situacao_com_base_no_ano(driver, collected_data["ano"])
    # chama a função responsável por digitar "0" no campo de média
    insert_value_in_media_field(driver)
    # chama a função responsável por marcar o checkbox "omitir resultado"
    mark_checkbox(driver)
    # chama a função para clicar no botão INCLUIR
    btn_incluir()
    # chama a função para clicar no 'OK' do popup de confirmação
    popup_ok()

elif collected_data["agrupamento_ano"] == "1º ANO":
    print('1º ANO')
    # chama a função para digitar o número de matrícula
    digita_matricula()
    # Altera o campo de ANO para o número que foi alimentado no tkinter
    alterar_ano()
    # chama a função que seleciona ENSINO FUNDAMENTAL
    seleciona_ensino_fundamental()
    # chama a função que seleciona 1º ANO
    seleciona_1_ano()
    # chama a função que escreve o nome da escola
    alterar_escola()
    # chama a função que escreve o nome do município
    alterar_municipio()
    #escrever as observações
    observacao(collected_data['observacoes'])
    # chama a função que cadastra TODAS as matérias do fundamental
    cadastrar_todas_materias_fundamental()
    
elif collected_data["agrupamento_ano"] == "2º ANO":
    print('2º ANO')
    # chama a função para digitar o número de matrícula
    digita_matricula()
    # Altera o campo de ANO para o número que foi alimentado no tkinter
    alterar_ano()
    # chama a função que seleciona ENSINO FUNDAMENTAL
    seleciona_ensino_fundamental()
    # chama a função que seleciona 1º ANO
    seleciona_2_ano()
    # chama a função que escreve o nome da escola
    alterar_escola()
    # chama a função que escreve o nome do município
    alterar_municipio()
    #escrever as observações
    observacao(collected_data['observacoes'])
    # chama a função que cadastra TODAS as matérias do fundamental
    cadastrar_todas_materias_fundamental()
    
elif collected_data["agrupamento_ano"] == "3º ANO":
    print('3º ANO')
    # chama a função para digitar o número de matrícula
    digita_matricula()
    # Altera o campo de ANO para o número que foi alimentado no tkinter
    alterar_ano()
    # chama a função que seleciona ENSINO FUNDAMENTAL
    seleciona_ensino_fundamental()
    # chama a função que seleciona 1º ANO
    seleciona_3_ano()
    # chama a função que escreve o nome da escola
    alterar_escola()
    # chama a função que escreve o nome do município
    alterar_municipio()
    #escrever as observações
    observacao(collected_data['observacoes'])
    # chama a função que cadastra TODAS as matérias do fundamental
    cadastrar_todas_materias_fundamental()

elif collected_data["agrupamento_ano"] == "4º ANO":
    print('4º ANO')
    # chama a função para digitar o número de matrícula
    digita_matricula()
    # Altera o campo de ANO para o número que foi alimentado no tkinter
    alterar_ano()
    # chama a função que seleciona ENSINO FUNDAMENTAL
    seleciona_ensino_fundamental()
    # chama a função que seleciona 1º ANO
    seleciona_4_ano()
    # chama a função que escreve o nome da escola
    alterar_escola()
    # chama a função que escreve o nome do município
    alterar_municipio()
    #escrever as observações
    observacao(collected_data['observacoes'])
    # chama a função que cadastra TODAS as matérias do fundamental
    cadastrar_todas_materias_fundamental()
    
elif collected_data["agrupamento_ano"] == "5º ANO":
    print('5º ANO')
    # chama a função para digitar o número de matrícula
    digita_matricula()
    # Altera o campo de ANO para o número que foi alimentado no tkinter
    alterar_ano()
    # chama a função que seleciona ENSINO FUNDAMENTAL
    seleciona_ensino_fundamental()
    # chama a função que seleciona 1º ANO
    seleciona_5_ano()
    # chama a função que escreve o nome da escola
    alterar_escola()
    # chama a função que escreve o nome do município
    alterar_municipio()
    #escrever as observações
    observacao(collected_data['observacoes'])
    # chama a função que cadastra TODAS as matérias do fundamental
    cadastrar_todas_materias_fundamental()
    









# Obtenha o tempo decorrido
end_time = t.time()

# Imprima o tempo decorrido
print("Tempo decorrido:", end_time - start_time)

# PROVISORIO : APENAS ENQUANTO SE CONFECCIONA O CÓDIGO
print('########################################################################################################################################################################')


# Mantém a janela do navegador aberta até que o usuário decida fechá-la
input("Pressione Enter para fechar o navegador...")
#driver.quit()





'''
############################################################################################## EM TESTE
# ZONA DE TESTE   -   ZONA DE TESTE   -   ZONA DE TESTE   -   ZONA DE TESTE   -   ZONA DE TESTE   -   ZONA DE TESTE 
'''


'''
# ZONA DE TESTE   -   ZONA DE TESTE   -   ZONA DE TESTE   -   ZONA DE TESTE   -   ZONA DE TESTE   -   ZONA DE TESTE
############################################################################################## EM TESTE
'''
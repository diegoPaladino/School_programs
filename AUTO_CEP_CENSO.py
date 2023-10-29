import os
import json
import pyautogui as p
import time as t
import clipboard as c


# Marca o tempo de início
start_time = t.time()


# Tente abrir o arquivo 'coordinates.json' e carregar as coordenadas
try:
    with open('coordinates.json', 'r') as f:
        coordinates = json.load(f)
    excel_x, excel_y = coordinates['excel']
    chrome_x, chrome_y = coordinates['chrome']
    brave_x, brave_y = coordinates['brave']
    matricula_x, matricula_y = coordinates['matricula_x_y']
except (FileNotFoundError, json.JSONDecodeError, KeyError):
    # Se o arquivo não existir, não puder ser lido ou as chaves não estiverem presentes,
    # pedimos ao usuário para fornecer as coordenadas

    p.alert('Posicione o mouse onde desejar capturar o LOCAL do EXCEL e pressione OK')
    excel_x, excel_y = p.position()

    p.alert('Posicione o mouse onde desejar capturar o LOCAL do CHROME e pressione OK')
    chrome_x, chrome_y = p.position()
    
    p.alert('Posicione o mouse onde desejar capturar o BRAVE e pressione OK')
    brave_x, brave_y = p.position()
    
    p.alert('Posicione o mouse onde desejar capturar o matricula_x_y e pressione OK')
    matricula_x, matricula_y = p.position()

    # Salvamos as coordenadas no arquivo 'coordinates.json'
    with open('coordinates.json', 'w') as f:
        json.dump({'excel': (excel_x, excel_y), 'chrome': (chrome_x, chrome_y),  'brave': (brave_x, brave_y)},f)

# Agora você pode usar as variáveis excel_x, excel_y, chrome_x, chrome_y, third_x, third_y em seu código



while True:
    #SELECIONANDO O EXCEL
    p.click(excel_x, excel_y)
    t.sleep(0.2)
    #capturando número de matrícula NO EXCEL
    p.press('esc')
    t.sleep(0.3)
    p.press('home')
    t.sleep(1)
    p.press('right')
    t.sleep(0.2)
    #CAPTANDO O NÚMERO DA MATRÍCULA
    # mover para o início do campo
    p.moveTo(360, 165)
    t.sleep(0.5)  # aguarda meio segundo para evitar problemas de sincronização
    # pressiona e segura o botão esquerdo do mouse
    p.mouseDown()
    # arrasta para o final do campo
    p.moveTo(261, 165)
    # solta o botão esquerdo do mouse
    p.mouseUp()
    #copia o número da matrícula
    p.hotkey('ctrl','c')
    t.sleep(0.3)
    # criando a variável cep
    matricula = c.paste()
    t.sleep(0.1)

    # CAPTANDO O NÚMERO DO CPF
    # movendo para a célula de CPF
    p.hotkey('esc')
    t.sleep(0.3)
    p.press('right',presses=3)
    t.sleep(0.3)
    # mover para o início do campo
    p.moveTo(360, 165)
    t.sleep(0.5)  # aguarda meio segundo para evitar problemas de sincronização
    # pressiona e segura o botão esquerdo do mouse
    p.mouseDown()
    # arrasta para o final do campo
    p.moveTo(261, 165)
    # solta o botão esquerdo do mouse
    p.mouseUp()
    #copia o número do CPF
    p.hotkey('ctrl','c')
    t.sleep(0.3)
    # criando a variável cpf
    cpf = c.paste()
    t.sleep(0.2)
    # reposicionando selecao de celula
    p.press('enter')
    t.sleep(0.2)
    


    #SELECIONANDO O NAVEGADOR BRAVE
    p.click(brave_x, brave_y)
    t.sleep(0.5)
    ########################################################################################################################
    # parte provisória do código apenas para resetar o navegador brave - cadastro de alunos
    p.click(x=834, y=13)
    t.sleep(0.5)
    p.click(x=62, y=578)
    t.sleep(0.5)
    p.hotkey('home')
    t.sleep(0.3)
    p.moveTo(x=454, y=165,duration=0.3)
    t.sleep(0.2)
    p.click(x=447, y=469)
    t.sleep(1.5)
    ########################################################################################################################
    #subindo página para alinhar local do campo de texto
    p.press('home')
    t.sleep(0.5)
    #clicando no campo da matrícula
    p.click(matricula_x,matricula_y)
    t.sleep(0.2)
    #colando o número de matrícula
    p.write(matricula,interval=0.05)
    t.sleep(0.3)
    # teclando tab para carregar as informações
    p.hotkey('tab')
    t.sleep(1)
    # baixando a página para iniciar captura de número de CEP
    p.press('end')
    t.sleep(0.5)
    # capturando o número do CEP
    # clicando no campo de ENDEREÇO para expandir os itens
    p.click(x=143, y=558)
    t.sleep(0.6)
    # selecionando o número de CEP
    p.doubleClick(x=210, y=650)
    t.sleep(0.2)
    # copia o número do CEP
    p.hotkey('ctrl','c')
    t.sleep(0.3)
    # criando a variável cep
    cep = c.paste()
    t.sleep(0.1)



    # SELECIONANDO O CHROME PARA AÇÕES NO CENSOESCOLAR
    p.click(chrome_x, chrome_y)
    t.sleep(0.5)
    p.press('home')
    t.sleep(0.5)
    # clicando na caixa de CPF da página do Censo Escolar
    p.click(x=489, y=637)
    t.sleep(0.5)
    # escrevendo o número do cpf
    p.write(cpf,interval=0.05)
    t.sleep(0.2)
    #desselecionando o campo do CPF
    p.hotkey('tab')
    t.sleep(0.3)
    p.hotkey('pagedown')
    t.sleep(0.5)
    #clicando em PESQUISAR
    p.click(x=1396, y=732)
    t.sleep(0.5)
    p.hotkey('pagedown')
    t.sleep(0.2)
    #clicar no item "Editar dados pessoais"
    p.click(x=353, y=471)
    t.sleep(1)
    # selecionar campo do CEP para apagar e colar novo
    p.click(x=355, y=701)
    t.sleep(0.5)
    # selecionando tudo
    p.keyDown('ctrl')
    p.hotkey('a')
    t.sleep(0.5)
    p.keyUp('ctrl')
    t.sleep(0.5)
    p.hotkey('backspace')
    t.sleep(0.5)
    # escrevendo o CEP
    p.write(cep,interval=0.05)
    t.sleep(0.2)
    # clicando na parte branca
    p.click(x=1531, y=521)
    t.sleep(0.2)
    # baixando página para clicar em enviar
    p.press('end')
    t.sleep(1)
    p.press('end')
    t.sleep(0.5)
    # clicando em enviar
    p.click(x=1441, y=730)
    t.sleep(1)















# Marca o tempo de término
end_time = t.time()
# Calcula o tempo de execução
execution_time = end_time - start_time
# Imprime o tempo de execução
print(f"Tempo de execucao: {execution_time} segundos")
print('matrícula = ',matricula)
print('cpf       = ',cpf)
print('cep       = ',cep)



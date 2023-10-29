import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

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
    data = entry_data.get()
    ensino = ensino_var.get()
    try:
        horas = calcular_carga_horaria(data, ensino)
        resultado = f"{int(horas)} horas-aula"
        result_var.set(resultado)
        
        # Copiando o resultado para a área de transferência
        root.clipboard_clear()
        root.clipboard_append(int(horas))
        root.update()  # Isso é necessário para que o resultado permaneça na área de transferência após o programa ser fechado
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira a data no formato dd/mm.")

# Criando a janela principal
root = tk.Tk()
root.title("Cálculo de Carga Horária")

# Adicionando widgets
label = tk.Label(root, text="Digite a data de transferência (dd/mm):")
label.pack(pady=10)

entry_data = tk.Entry(root)
entry_data.pack(pady=10)
entry_data.bind('<Return>', on_calculate)  # Vinculando a tecla 'Enter' à função on_calculate

# Checkbox for user selection
ensino_var = tk.StringVar()
ensino_var.set("ENSINO FUNDAMENTAL")  # Default value
ttk.Radiobutton(root, text="ENSINO INFANTIL", variable=ensino_var, value="ENSINO INFANTIL").pack(pady=5)
ttk.Radiobutton(root, text="ENSINO FUNDAMENTAL", variable=ensino_var, value="ENSINO FUNDAMENTAL").pack(pady=5)

btn_calcular = tk.Button(root, text="Calcular", command=on_calculate)
btn_calcular.pack(pady=20)

# Variável para exibir o resultado
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack(pady=20)

root.mainloop()

# from openpyxl import load_workbook, Workbook
from datetime import datetime

# Defina as datas de início e fim como strings no formato "mm/yyyy"
data_inicio_str = "01/2023"
data_fim_str = "12/2023"

# Converta as strings para datetime
data_inicio = datetime.strptime(data_inicio_str, "%m/%Y")
data_fim = datetime.strptime(data_fim_str, "%m/%Y")

# Exemplo de uma data atual sendo lida como string ou datetime
data_atual_str = "06/2024"  # Simulando uma leitura
data_atual = datetime.strptime(data_atual_str, "%m/%Y")  # Converte para datetime

# Comparação
if data_inicio <= data_atual <= data_fim:
    print("Data atual está dentro do intervalo.")
else:
    print("Data atual está fora do intervalo.")

print(type(data_inicio))
print(type(data_atual))
print(type(data_fim))

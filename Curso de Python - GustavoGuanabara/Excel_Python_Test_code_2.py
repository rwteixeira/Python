from datetime import datetime

# Suponha que DataRef_ini seja um datetime já existente
DataRef_ini = datetime(2024, 12, 1)  # Exemplo

# Use o objeto datetime diretamente
data_inicio = DataRef_ini  # Correção: já é datetime

# Ou, se necessário como string
data_inicio_str = DataRef_ini.strftime("%m/%Y")

print(f"Data início como datetime: {data_inicio}")
print(f"Data início como string: {data_inicio_str}")

print("DataRef_ini: ", type(DataRef_ini))
print("data_inicio: ", type(data_inicio))
print("data_inicio_str: ", type(data_inicio_str))
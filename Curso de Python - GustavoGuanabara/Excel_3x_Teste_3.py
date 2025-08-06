import pandas as pd

# Ler a planilha Excel (ajuste o nome do arquivo e a folha conforme necessário)
df = pd.read_excel("meses_ordenados.xlsx", sheet_name="Planilha1")

# Supondo que a coluna "Meses" contenha os números dos meses
meses_numeros = df["Mês"]

# Obter os valores únicos e ordenar
meses_numeros_unicos = sorted(meses_numeros.unique())

# Criar um DataFrame com os números dos meses ordenados únicos
df_ordenado_unico = pd.DataFrame({"Meses Ordenados Únicos": meses_numeros_unicos})
#df_ordenado_unico = pd.DataFrame(meses_numeros_unicos)

# Salvar em um novo arquivo Excel
df_ordenado_unico.to_excel("meses_ordenados_unicos.xlsx", index=False)

print("Meses únicos ordenados e salvos em 'meses_ordenados_unicos.xlsx'.")

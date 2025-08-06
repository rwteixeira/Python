import pandas as pd

# Ler a planilha Excel (ajuste o nome do arquivo e a folha conforme necessário)
df = pd.read_excel("meses_ordenados.xlsx", sheet_name="Planilha1")

# Supondo que a coluna "Meses" contenha os números dos meses
meses_numeros = df["Mês"]

# Ordenar os números dos meses
meses_numeros_unicos = sorted(meses_numeros.unique())

# Dicionário para mapear números aos nomes dos meses
nomes_meses = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
    7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

# Converter os números para os nomes dos meses
meses_ordenados_unicos = [nomes_meses[mes] for mes in meses_numeros_unicos]

# Criar um DataFrame com os meses ordenados
df_ordenado_unico = pd.DataFrame({"Meses Ordenados Unicos": meses_ordenados_unicos})

# Salvar em um novo arquivo Excel
df_ordenado_unico.to_excel("meses_ordenados_unicos.xlsx", index=False)

print("Meses ordenados e salvos em 'meses_ordenados_unicos.xlsx'.")
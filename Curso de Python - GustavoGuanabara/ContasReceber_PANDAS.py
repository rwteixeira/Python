import pandas as pd

tabela = pd.read_excel("ContasReceber1.xlsx")
# ATUALIZAR O MULTIPLICADOR
# tabela.loc[tabela["SITUAÇÃO"]=="Atrasado", "TAXA"] = 1.2

# CALCULAR O VALOR TOTAL COM BASE NA TAXA
tabela["TOTAL"] = tabela["TAXA"] * tabela["VALOR"]
tabela.to_excel("CONTAS_RECEBER_PANDAS.xlsx", index=False)

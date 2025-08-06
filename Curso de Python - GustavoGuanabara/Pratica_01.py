print('-'* 43)
texto = 'R4 DATA CENTER'
print(f'{texto:^43}')
print('-'* 43)
# -------------------------------
pessoas = {
    'chico': {'nome': 'Chico', 'idade': 33, 'profissão': 'Professor'},
    'bras': {'nome': 'Brás Cubas', 'idade': 64, 'profissão': 'Defunto-autor'},
    'machado': {'nome': 'Machado de Assis', 'idade': 69, 'profissão': 'Escritor'},
}

print(f"{'Nome':^16} | {'Idade':^6} | {'Profissão':^15}")
print(f"{'-'*16} | {'-'*6} | {'-'*15}")

for pessoa in pessoas:
    d = pessoas[pessoa]
    print(f"{d['nome']:<16} | {d['idade']:^6} | {d['profissão']:>15}")
print()
print('-'* 43)
print(f"{'FORMATAÇÃO DE DATA':^43}")
from datetime import datetime
print('{:%d-%m-%Y }'.format(datetime(1964, 10, 13, 22, 56)))
print('-'* 43)
print(len(texto))
print(texto[len(texto)-6:])

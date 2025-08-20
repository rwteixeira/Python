import json
# Converter de JSON para Python
json_string = '{"nome": "João", "idade": 30}'
dados = json.loads(json_string)
print(dados['nome'])

# Converter de Python para JSON
dados = {"nome": "Maria", "idade": 25}
json_string = json.dumps(dados)
print(json_string)

# Ler e escrever arquivos JSON
# Escrever
with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo)

# Ler
with open("dados.json", "r") as arquivo:
    dados_lidos = json.load(arquivo)
    print(dados_lidos)
    
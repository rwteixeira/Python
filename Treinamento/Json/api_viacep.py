import requests

cep = int(input("CEP: "))

req = requests.get(f"https://https://viacep.com.br/ws/{cep}/json/")
dados = req.json()



# for chave, valor in dados.items():
#     print(f"{chave}: {valor}")
# print("-"*15)

# cep = dados['cep']
# endereco = dados['address']
# estado = dados['state']
# bairro = dados['district']
# cidade = dados['city']
# cidade_ibge = dados['city_ibge']
# latitude = dados['lat']
# longitude = dados['lng']
# ddd = dados['ddd']
# print()
# print(f"Endereço: {endereco}")
# print(f"Cidade: {cidade}")
# print(f"Estado: {estado}")
# print(f"Bairro: {bairro}")
# print(f"Cidade IBGE: {cidade_ibge}")
# print(f"Latitude: {latitude}")
# print(f"Longitude: {longitude}")
# print(f"DDD: {ddd}")
# print()

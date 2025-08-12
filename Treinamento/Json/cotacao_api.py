import requests
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
# print(requisicao)
# print(requisicao.json())
dic_requisicao = requisicao.json()
# print(f"R$ {float(dic_requisicao['USDBRL']['bid']):.2f}")

valor = float(dic_requisicao['USDBRL']['bid'])
print(f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))



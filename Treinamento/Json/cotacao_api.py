import requests
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
# print(requisicao)
# print(requisicao.json())
dic_requisicao = requisicao.json()
print(f"R$ {float(dic_requisicao['USDBRL']['bid']):.2f}")
moeda = f"{str(dic_requisicao['USDBRL']['name'])}"

# -----------------------------------------------------------------

while True:
    print()
    print("Escolha uma opção:")
    print("-"*18)
    print("1 - Dólar para Real")
    print("2 - Euro para Real")
    print("3 - Bitcoin para Real")
    print("4 - Dolar-Euro-Bitcoin")
    print("5 - Sair")
    print()
    opcao = int(input("Opção: "))
    print()

    if opcao == 1:
        valor = float(dic_requisicao['USDBRL']['bid'])
        # print(f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        cotacao = f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        moeda = f"{str(dic_requisicao['USDBRL']['name'])}"
    elif opcao == 2:
        valor = float(dic_requisicao['EURBRL']['bid'])
        # print(f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        cotacao = f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        moeda = f"{str(dic_requisicao['EURBRL']['name'])}"
    elif opcao == 3:
        valor = float(dic_requisicao['BTCBRL']['bid'])
        # print(f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        cotacao = f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        moeda = f"{str(dic_requisicao['BTCBRL']['name'])}"
    elif opcao == 4:
        valor1 = float(dic_requisicao['USDBRL']['bid'])
        valor2 = float(dic_requisicao['EURBRL']['bid'])
        valor3 = float(dic_requisicao['BTCBRL']['bid'])
        
        cotacao1 = f"R$ {valor1:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        cotacao2 = f"R$ {valor2:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        cotacao3 = f"R$ {valor3:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        cotacao = f"dolar: {cotacao1}, euro: {cotacao2}, bitcoin: {cotacao3}"
    else:
        print("Saindo da cotação...")
        break

    print(f"Cotação de hoje é: {cotacao}")
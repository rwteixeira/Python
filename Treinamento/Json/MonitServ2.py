import requests
import json

cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m'}

def mostrar_status():
    req = requests.get("http://177.84.130.204:5000/status?token=221193t") # Criação de endpoint
    dados = req.json()
    print("\n--- STATUS DO SERVIDOR ---")
    for chave, valor in dados.items():
        print(f"{chave:<20}: {valor}")
    with open("status_servidor.json", "w") as f:
        json.dump(dados, f, indent=4)

def mostrar_usuarios():
    req = requests.get("http://177.84.130.204:5000/usuarios_linux?token=221193t") # Criação de endpoint
    usuarios = req.json()
    print("\n--- CONTAS DE USUÁRIOS ---")
    for usuario in usuarios:
        print(f"{cores['verde']}Usuário:{cores['limpa']} {usuario.get('usuario')}, {cores['amarelo']}Grupos: {cores['limpa']}{usuario.get('grupos')}")

while True:
    # Menu simples
    print("--- ESCOLHA UMA OPÇÃO ---")
    print("1 - Ver status do servidor")
    print("2 - Ver contas de usuários")
    print("3 - Sair")
    print()
    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        mostrar_status()
    elif opcao == "2":
        mostrar_usuarios()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print(f"{cores['vermelho']}Opção inválida.{cores['limpa']}")
        continue

import requests
import json
import time

req = requests.get(f"http://177.84.130.204:5000/status")
dados = req.json()
# print(dados)

for chave, valor in dados.items():
    print(f"{chave:<20}: {valor}")

with open("status_servidor.json", "w") as f:
    json.dump(dados, f, indent=4)

# while True:
#     req = requests.get("http://177.84.130.204:5000/status")
#     dados = req.json()
#     print(f"\n--- Status às {time.strftime('%H:%M:%S')} ---")
#     for chave, valor in dados.items():
#         print(f"{chave:<20}: {valor}")
#     time.sleep(10)  # atualiza a cada 10 segundos


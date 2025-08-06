import math
import os

x = 16

raiz = math.sqrt(x)
print(f"A raiz de {x} é {raiz}")

angulo = 45
seno = math.sin(angulo)
print(f"O seno de {angulo} é {seno:.4f}")

print("-=-"*50)

diretorio = os.getcwd()
print(f"Meu diretório de trabalho é: {diretorio}")

os.system("dir")

# Desafio_68: Faça um programa que jogue PAR ou ÍMPAR com
# o computador. O jogo será interrompido quando o jogador
# perder, mostrando o total de vitórias consecutivas que
# ele conquistou no final do jogo.
# DESAFIO RESOLVIDO POR RWT EM 17/10/2023
import random
vitorias = 0
while True:
   comp = random.randint(0, 9)
   user = int(input('Diga um número: '))
   res_jogo = (comp + user) % 2
   op = str(input('Par ou Ímpar? [P/I]: '))
   if op in 'Pp':
      if res_jogo == 0:
         print(f'Você jogou {user} e o computador jogou {comp}. A soma deu {comp + user}')
         print('Deu PAR, você venceu!')
         vitorias = vitorias + 1
      else:
         print(f'Você jogou {user} e o computador jogou {comp}. A soma deu {comp + user}')
         print('Deu ÍMPAR, você perdeu!')
         break
   if op in 'Ii':
      if res_jogo == 1:
         print(f'Você jogou {user} e o computador jogou {comp}. A soma deu {comp + user}')
         print('Deu ÍMPAR, você venceu!')
         vitorias = vitorias + 1
      else:
         print(f'Você jogou {user} e o computador jogou {comp}. A soma deu {comp + user}')
         print('Deu PAR, você perdeu!')
         break
print(f'GAME OVER!! você venceu {vitorias} vezes')

# Melhore o jogo do DESAFIO_028 onde o computador
# vai "pensar" em um número entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando
# no final quantos palpites foram necessários para vencer.
# Ref: https://www.youtube.com/watch?v=-QkOIHJ1Chw&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=60
# ESSE DESAFIO FOI DESENVOLVIDO POR RWT EM 10/10/2023
import random
palpite = 0
comp = random.randint(0,5)
print('\033[32m* * * * \033[m\033[33mJOGO DE ADIVINHAR\033[m\033[32m * * * * \033[m')
num = 1
palpite = 0
while num != comp:
    num = int(input('{} - Digite um número entre 0 e 5: '.format(palpite+1)))
    palpite += 1
print('\033[32m* \033[m'*18)
print('      Você tentou \033[1;36m{}\033[m vezes.'.format(palpite))
print('\033[32m* \033[m'*18)

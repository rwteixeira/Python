# CRIAR O JOGO JOKEMPÔ
import random
import emoji
print('\033[1;34mPara jogar, escolha uma opção\033[m')
print(emoji.emojize('\033[1;32m[1]\033[m Pedra - :raised_fist:'))
print(emoji.emojize('\033[1;32m[2]\033[m Papel - :hand_with_fingers_splayed:'))
print(emoji.emojize('\033[1;32m[3]\033[m Tesoura - :victory_hand:'))
print('-'*40)
j = random.randint(1,3)
c = int(input('Para jogar, escolha uma opção: '))
print(' ')
if c == 1:
    if j == 1:
        print('Você: \033[35mPEDRA\033[m.\nComputador: \033[35mPEDRA\033[m')
        print('-' * 40)
        print('\033[1;35mDEU EMPATE! - TENTE NOVAMENTE!\033[m')
    elif j == 2:
        print('Você: \033[35mPEDRA\033[m.\nComputador: \033[33mPAPEL\033[m')
        print('-' * 40)
        print('\033[1;30;46mO COMPUTADOR GANHOU!\033[m')
    else:
        print('Você: \033[35mPEDRA\033[m.\nComputador: \033[36mTESOURA\033[m')
        print('-' * 40)
        print('\033[1;30;41mVOCÊ GANHOU GANHOU!\033[m')
elif c == 2:
    if j == 1:
        print('Você: \033[33mPAPEL\033[m.\nComputador: \033[35mPEDRA\033[m')
        print('-' * 40)
        print('\033[1;30;41mVOCÊ GANHOU GANHOU!\033[m')
    elif j == 2:
        print('Você: \033[33mPAPEL\033[m.\nComputador: \033[33mPAPEL\033[m')
        print('-' * 40)
        print('\033[1;35mDEU EMPATE! - TENTE NOVAMENTE!\033[m')
    else:
        print('Você: \033[33mPAPEL\033[m.\nComputador: \033[36mTESOURA\033[m')
        print('-' * 40)
        print('\033[1;30;46mO COMPUTADOR GANHOU!\033[m')
elif c == 3:
    if j == 1:
        print('Você: \033[36mTESOURA\033[m.\nComputador: \033[35mPEDRA\033[m')
        print('-' * 40)
        print('\033[1;30;46mO COMPUTADOR GANHOU!\033[m')
    elif j == 2:
        print('Você: \033[36mTESOURA\033[m.\nComputador: \033[33mPAPEL\033[m')
        print('-' * 40)
        print('\033[1;30;41mVOCÊ GANHOU GANHOU!\033[m')
    else:
        print('Você: \033[36mTESOURA\033[m.\nComputador: \033[36mTESOURA\033[m')
        print('-' * 40)
        print('\033[1;35mDEU EMPATE! - TENTE NOVAMENTE!\033[m')
else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')

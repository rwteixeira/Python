# Desafio_97: Faça um programa que tenha uma função chamada escreva(),
# que receba  um  texto  qualquer como parâmetro e mostre uma mensagem
# com tamanho adaptável. Ex: escreva('Olá, Mundo!') Saída: Olá, Mundo!
# Ref: https://www.youtube.com/watch?v=Q6basnSo7r0

def escreva(msg):
    tam  =len((msg)) + 4
    print('~' * tam)
    print(f'  {msg:^}')
    print('~' * tam)


# PROGRAMA PRINCIPAL
escreva('Ricardo Wagner Teixeira')
escreva('R4')
escreva('Curso de Python em vídeo no YouTube')
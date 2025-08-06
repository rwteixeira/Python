# Calcular o IMC: IMC = peso / (altura)²
altura = float(input('Digite a sua altura: '))
peso = float(input('Entre com seu peso: '))
imc = peso / (altura ** 2)
print('-'*45)
if imc < 18.5:
    print('Seu IMC é de {:.2f}. Isso indica que você está ABAIXO DO PESO!'.format(imc))
elif imc <= 18.5 and imc < 25:
    print('Seu IMC é de {:.2f}. Isso indica que você está com o PESO IDEAL!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f}. Isso indica que você está na faixa de SOBREPESO!'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu IMC é {:.2f}. Isso indica OBESIDADE.'.format(imc))
else:
    print('Seu IMC é {:.2f}. Isso indica que você tem OBESIDADE MÓRBIDA!'.format(imc))
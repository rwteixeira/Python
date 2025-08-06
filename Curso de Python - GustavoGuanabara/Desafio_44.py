# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento.
# À vista [dinheiro] 10% desconto; à vista [no cartão] 5% desconto
# Em até 2x no cartão, preço normal; 3x ou mais no cartão, 20% de juros.
vl_total = float(input('Valor total da compra: '))
print(' ')
print('Escolha uma das opção de Pagamento:')
print('-'*55)
print('''[1] - À vista, em dinheiro - Desconto de 10%
[2] - À vista, no Cartão de Crédito - Desconto de 5%
[3] - Em até 2 vezes no Cartão, sem juros
[4] - Em três vezes no Cartão, com 20% de juros''')
print('-'*55)
opcao = int(input('Como vai pagar: '))
print('-'*55)
if opcao == 1:
    print('À Vista, no dinheiro. Desconto de 10%, \nTotal R${:.2f}'.format(vl_total-(vl_total*0.1)))
elif opcao == 2:
    print('À vista, no Cartão. Desconto de 5%, \nTotal R${:.2f}'.format(vl_total-(vl_total*0.05)))
elif opcao == 3:
    print('Duas parcelas no cartão. Sem juros. \n2 x de R${:.2f}, Total: {:.2f}'.format(vl_total-(vl_total/2),vl_total))
elif opcao == 4:
    print('Parcelado no Cartão. Com 20% de juros.\n3 x de R${:.2f}, Total: R${:.2f}'.format((vl_total+(vl_total*0.2))/3,vl_total+(vl_total*0.2)))
else:
    print('Você digitou uma opçãp inválida, tente novamente!')

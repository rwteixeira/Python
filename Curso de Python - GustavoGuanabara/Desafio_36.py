# SOLICITAÇÃO DE FINANCIAMENTO PARA CASA-PRÓPRIA
cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'magenta':'\033[35',
         'ciano':'\033[36'}
vl_finan = float(input('Informe o valor desejado do financiamento: '))
vl_salario = float(input('Informe o rendimento mensal: '))
t = int(input('Informe quantos em anos deseja pagar: '))
tempo = 12 * t
parcela = vl_finan / tempo
verificador = (vl_finan / tempo) / vl_salario
print('-'*40)
if verificador >= 0.3:
    print('O valor do financiamento é de R${:.2f}'.format(vl_finan))
    print('com parcelas de R${:.2f} por {} meses: ...'.format(parcela,tempo))
    print('Seu pedido de financiamento foi {}NEGADO!{}'.format(cores['vermelho'],cores['limpa']))
else:
    print('O valor do financiamento é de R${:.2f}'.format(vl_finan),end=' ')
    print('com parcelas de R${:.2f} por {} meses: ...'.format(parcela,tempo))
    print('Seu pedido de financiamento foi {}APROVADO!{}'.format(cores['azul'],cores['limpa']))

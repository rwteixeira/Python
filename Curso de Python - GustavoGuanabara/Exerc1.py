import openpyxl

# Criar uma planilha (book)
book = openpyxl.Workbook()

# Como criar uma página
book.create_sheet('Computadores')

# Como selecionar uma página
guia = book['Computadores']
# Nome das colunas:
guia.append(['Eletrônica', 'Memória', 'Preço'])

# Dados
guia.append(['Computador 1', '8 Gb', 'R$ 2500,00'])
guia.append(['Computador 2', '16 Gb', 'R$ 5500,00'])
guia.append(['Computador 3', '32 Gb', 'R$ 8500,00'])

# Salvar a planilha
book.save('Meus Computadores.xlsx')

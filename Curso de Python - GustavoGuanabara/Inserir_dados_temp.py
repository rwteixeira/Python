import mysql.connector
from mysql.connector import Error

# INSERIR REGISTROS EM UM BANCO DE DADOS MYSQL.
print('Rotina para cadastro de produtos no Banco de dados.')
print('Entre com os dados conforme solicitado:')

idProd = input('Id: ')
nomeProd = input('Nome do Produto: ')
precoProd = input('Preço: ')
qtdeProd = input('Quantidade: ')

dados = idProd + ',\'' + nomeProd + '\',' + precoProd + ',' + qtdeProd + ')'
declaracao = inserir_produtos = """INSERT INTO Produtos
                            (idProdutos, nome_produto, preco_unitario, quantidade)
VALUES ("""
sql = declaracao + dados

try:
    with open("login_us.txt", "r") as user:
        login = user.read()
    with open("login_ip.txt", "r") as ip:
        endereco = ip.read()
    with open("login_pw.txt", "r") as chave:
        passwd = chave.read()
    with open("login_db.txt", "r") as db:
        database = db.read()
    con = mysql.connector.connect(
        host=endereco,
        database=database,
        user=login,
        password=passwd)

    inserir_produtos = sql
    cursor = con.cursor()
    cursor.execute(inserir_produtos)
    con.commit()
    print(cursor.rowcount,'\033[33mRegistros inseridos na tabela!\033[m')
    cursor.close()

except Error as erro:
    print(f'\033[31mFalha ao inserir dados no MySQL: {erro}\033[m')
finally:
    if con.is_connected():
        cursor.close()
        print('\033[33mConexão ao MySQL foi encerrada!\033[m')

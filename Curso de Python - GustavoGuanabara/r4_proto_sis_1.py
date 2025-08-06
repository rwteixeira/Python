# -*- coding: utf-8 -*-

import easygui
import openpyxl

# Seleciona o arquivo .xlsx
arquivo = easygui.fileopenbox(title="Selecione uma pasta Excel", default="*.xlsx", filetypes=["*.xlsx"])

# Verifica se o usuário selecionou um arquivo
if arquivo:
    # Abre o arquivo no openpyxl
    wb = openpyxl.load_workbook(arquivo)

    # Obtendo apenas o nome do arquivo sem o caminho completo
    import os
    nome_arquivo = os.path.basename(arquivo)

    # Exibe o nome do arquivo no console
    print(f"Arquivo selecionado: {nome_arquivo}")

    # Mensagem visual para o usuário
    easygui.msgbox(f"Você abriu o arquivo:\n{nome_arquivo}", title="Arquivo Selecionado")
else:
    easygui.msgbox("Nenhum arquivo foi selecionado.", title="Aviso")
print(nome_arquivo)
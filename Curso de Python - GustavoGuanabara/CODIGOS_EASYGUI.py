# -*- coding: utf-8 -*-
# PROJETO INICIADO EM 29/01/2025
# by: RWT
# EXEMPLOS DE CÓDIGOS PARA EASYGUI


import easygui

easygui.msgbox("""Olá! Bem-vindo ao nosso sistema de controle de Custos!
\nAqui, você vai parametrizar as entradas de dados
para que o custo dos serviços possa ser calculado.
Quanto mais precisas forem as informações, mais precisos
serão os valores calculados.""", title="Saudação")

'''arquivo = easygui.fileopenbox(title="Selecione um Arquivo")
pasta = load_workbook(arquivo)

easygui.msgbox(f"Você escolheu: {arquivo}", title="Arquivo Selecionado")

texto = "Este é um exemplo de texto longo.\n" * 20  # Simulando um texto longo
easygui.textbox(msg="Visualizando um texto:", title="Exemplo de Textbox", text=texto)

texto_original = "Digite ou edite o texto aqui..."
texto_editado = easygui.textbox("Edite o texto abaixo:", "Editor de Texto", texto_original)

if texto_editado:
    easygui.msgbox(f"Você editou o texto para:\n\n{texto_editado}", title="Texto Final")
else:
    easygui.msgbox("Nenhuma alteração feita.", title="Aviso")
'''

opcao = easygui.buttonbox("Escolha uma opção:", title="Menu",
                          choices=["Arquivo", "Arquivo Novo"])

if opcao == "Arquivo Novo":
    easygui.msgbox("Arquivo Novo", title="Aviso")
else:
    easygui.msgbox("Arquivo.", title="Aviso")


# CAIXAS (ESCOLHA E MULTIPLA-ESCOLHA:

opcoes = ["Python", "Java", "C++", "JavaScript"]
# CAIXA DE MÚLTIPLA ESCOLHA
selecionados = easygui.multchoicebox("Quais linguagens você gosta?", title="Escolha", choices=opcoes)
easygui.msgbox(f"Você selecionou: {selecionados}", title="Resultado")

# CAIXA DE ESCOLHA SIMPLES
selecionado = easygui.choicebox("Quais linguagens você gosta?", title="Escolha", choices=opcoes)
easygui.msgbox(f"Você selecionou: {selecionado}", title="Resultado")


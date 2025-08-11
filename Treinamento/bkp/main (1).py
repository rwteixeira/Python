from sistema_usuarios import SistemaUsuarios

# Criando o sistema de usuários
sistema = SistemaUsuarios()

# Adicionando usuários
sistema.adicionar_usuario("Ricardo Teixeira", "ricardo@email.com")
sistema.adicionar_usuario("João Silva", "joao@email.com")

# Listando usuários
sistema.listar_usuarios()

# Ativando um usuário
usuario = sistema.buscar_usuario_por_email("ricardo@email.com")
if usuario:
    usuario.ativar()

# Listando novamente para ver o status atualizado
sistema.listar_usuarios()

# Removendo um usuário
sistema.remover_usuario("joao@email.com")

# Listando usuários após remoção
sistema.listar_usuarios()

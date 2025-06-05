import networkx as nx
import matplotlib.pyplot as plt

# Criando o grafo
G = nx.Graph()

# Nós principais
G.add_edges_from([
    ("Sistema", "GUI"),
    ("Sistema", "cliente.py"),
    ("Sistema", "produto.py"),
    ("Sistema", "funcionario.py"),
    ("Sistema", "compra.py"),
    ("Sistema", "db.py"),
    
    ("GUI", "Adicionar Cliente"),
    ("GUI", "Adicionar Produto"),
    ("GUI", "Adicionar Funcionário"),
    ("GUI", "Registrar Compra"),
    ("GUI", "Atualizar/Excluir Cliente"),
    ("GUI", "Atualizar/Excluir Produto"),
    ("GUI", "Atualizar/Excluir Funcionário"),

    ("Registrar Compra", "Classe Compra"),
    ("Classe Compra", "Cliente (via CPF)"),
    ("Classe Compra", "Produto (via código de barras)"),
    ("Classe Compra", "Funcionário (via ID)"),

    ("db.py", "Funções de Conexão"),
    ("db.py", "Funções CRUD"),
    ("db.py", "Funções de Leitura"),
])

# Desenhando o grafo
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G, seed=42)  
nx.draw_networkx(G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=10, font_weight='bold', edge_color="gray")
plt.title("Grafo do Sistema de Cadastro e Compras", fontsize=16)
plt.axis("off")
plt.tight_layout()
plt.show()

import mysql.connector
import random
import string
from compra import Compra

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Substitua pela sua senha
        database="cadastro_clientes"
    )

def gerar_nota_fiscal():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
 
 
 #Atualizar Clientes 
def atualizar_cliente(cliente):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
    UPDATE clientes SET nome=%s, email=%s, telefone=%s, cidade=%s WHERE cpf=%s
    """
    cursor.execute(sql, (cliente.nome, cliente.email, cliente.telefone, cliente.cidade, cliente.cpf))
    conn.commit()
    cursor.close()
    conn.close()
#Deletar Cliente
def excluir_cliente(cpf: str):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM clientes WHERE cpf=%s"
    cursor.execute(sql, (cpf,))
    conn.commit()
    cursor.close()
    conn.close()

#Atualizar Funcionario
def atualizar_funcionario(funcionario):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
    UPDATE funcionarios SET nome=%s, email=%s, telefone=%s, cargo=%s, salario=%s WHERE id_funcionario=%s
    """
    cursor.execute(sql, (funcionario.nome, funcionario.email, funcionario.telefone, funcionario.cargo, funcionario.salario, funcionario.id_funcionario))
    conn.commit()
    cursor.close()
    conn.close()

#Deletar Funcionario 
def excluir_funcionario(id_funcionario: str):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM funcionarios WHERE id_funcionario=%s"
    cursor.execute(sql, (id_funcionario,))
    conn.commit()
    cursor.close()
    conn.close()

#Atualizar Produto
def atualizar_produto(produto):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
    UPDATE produtos SET nome=%s, valor_unitario=%s, quantidade=%s WHERE codigo_barras=%s
    """
    cursor.execute(sql,  (produto.nome, produto.valor_unitario, produto.quantidade, produto.codigo_barras))
    conn.commit()
    cursor.close()
    conn.close()

#Deletar Produto 
def excluir_produto(codigo_barras: str):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM produtos WHERE codigo_barras=%s"
    cursor.execute(sql, (codigo_barras,))
    conn.commit()
    cursor.close()
    conn.close()

#Puxar informções do Banco de Dados para tela de resumo
def obter_clientes():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def obter_produtos():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def obter_funcionarios():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    conn.close()
    return funcionarios

def obter_compras():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM compras")
    compras = cursor.fetchall()
    conn.close()
    return compras

#Insere as informções no Banco
def inserir_cliente(cliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO clientes (cpf, nome, email, telefone, cidade)
        VALUES (%s, %s, %s, %s, %s)
    """, (cliente.cpf, cliente.nome, cliente.email, cliente.telefone, cliente.cidade))
    conn.commit()
    cursor.close()
    conn.close()

def inserir_produto(produto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO produtos (codigo_barras, nome, valor_unitario, quantidade)
        VALUES (%s, %s, %s, %s)
    """, (produto.codigo_barras, produto.nome, produto.valor_unitario, produto.quantidade))
    conn.commit()
    cursor.close()
    conn.close()

def inserir_funcionario(funcionario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO funcionarios (id_funcionario, nome, email, telefone, cargo, salario)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (funcionario.id_funcionario, funcionario.nome, funcionario.email, funcionario.telefone, funcionario.cargo, funcionario.salario))
    conn.commit()
    cursor.close()
    conn.close()

def registrar_compra(compra):
    conn = conectar()
    cursor = conn.cursor()

    if not compra.nota_fiscal:
        compra.nota_fiscal = gerar_nota_fiscal()

    cursor.execute('''
        INSERT INTO compras (cpf_cliente, codigo_barras_produto, id_funcionario, quantidade, valor_total, nota_fiscal)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (
        compra.cpf_cliente,
        compra.codigo_barras_produto,
        compra.id_funcionario,
        compra.quantidade,
        compra.valor_total,
        compra.nota_fiscal
    ))

    conn.commit()
    cursor.close()
    conn.close()

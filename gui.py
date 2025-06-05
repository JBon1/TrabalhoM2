import customtkinter as ctk
import random
import string
from chatbot_04 import abrir_chatbot
from tkinter import messagebox
from cliente import Cliente
from produto import Produto
from funcionario import Funcionario
from compra import Compra
from db import inserir_cliente, inserir_produto, inserir_funcionario, registrar_compra
from db import obter_clientes, obter_compras, obter_funcionarios, obter_produtos
from db import atualizar_cliente, excluir_cliente
from db import atualizar_produto, excluir_produto
from db import atualizar_funcionario, excluir_funcionario
import tkinter as tk



cliente = {}
produto = {}
funcionario = {}




# Função para adicionar cliente
def adicionar_cliente():
    global cliente
    cpf = entry_cpf.get()
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    cidade = entry_cidade.get()
    cliente = Cliente(cpf, nome, email, telefone, cidade)
    inserir_cliente(cliente)

    messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado com sucesso!")

   
# Função para adicionar produto
def adicionar_produto():
    global produto
    codigo = entry_codigo_barras.get()
    nome = entry_produto_nome.get()
    preco = float(entry_produto_preco.get())
    quantidade = int(entry_produto_quantidade.get())
    produto = Produto(codigo, nome, preco, quantidade)
    inserir_produto(produto)
    messagebox.showinfo("Sucesso", f"Produto {nome} cadastrado com sucesso!")

# Função para adicionar funcionário
def adicionar_funcionario():
    global funcionario
    id_funcionario = int(entry_funcionario_id.get())
    nome = entry_funcionario_nome.get()
    email = entry_funcionario_email.get()
    telefone = entry_funcionario_telefone.get()
    cargo = entry_funcionario_cargo.get()
    salario = float(entry_funcionario_salario.get())
    funcionario = Funcionario(id_funcionario, nome, email, telefone, cargo, salario)
    inserir_funcionario(funcionario)
    messagebox.showinfo("Sucesso", f"Funcionário {nome} cadastrado com sucesso!")

# Função para registrar compra
def gerar_nota_fiscal():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))  # Ex: "A9X2T5D8QW"

def registrar_compra_bd():
    cpf_cliente = entry_cpf_cliente.get()
    codigo_barras = entry_codigo_barras.get()
    id_funcionario = entry_id_funcionario.get()
    quantidade = int(entry_quantidade.get())
    produtos = obter_produtos()
    produto = next((p for p in produtos if p['codigo_barras'] == codigo_barras), None)

    if not produto:
        messagebox.showerror("Erro", "Produto não encontrado.")
        return

    valor_unitario = float(produto['valor_unitario'])

    valor_total = valor_unitario * quantidade

    nota_fiscal = gerar_nota_fiscal()

    compra = Compra(cpf_cliente, codigo_barras, id_funcionario, quantidade, valor_total, nota_fiscal)
    registrar_compra(compra)
    
    messagebox.showinfo("Sucesso", f"Compra registrada com sucesso!\nNota Fiscal: {nota_fiscal}")

def atualizar_cliente_func():
    global cliente
    try:
        cpf = entry_cpf.get()
        nome = entry_nome.get()
        email = entry_email.get()
        telefone = entry_telefone.get()
        cidade = entry_cidade.get()
        cliente = Cliente(cpf, nome, email, telefone, cidade)
        atualizar_cliente(cliente)
        messagebox.showinfo("Sucesso", f"Cliente {nome} atualizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def excluir_cliente_func():
    cpf = entry_cpf.get()
    if messagebox.askyesno("Confirmação", f"Quer mesmo excluir o cliente {cpf}?"):
        try:
            excluir_cliente(cpf)
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

def atualizar_produto_func():
    global produto
    try:
        codigo = entry_codigo_barras.get()
        nome = entry_produto_nome.get()
        preco = float(entry_produto_preco.get())
        quantidade = int(entry_produto_quantidade.get())
        produto = Produto(codigo, nome, preco, quantidade)
        atualizar_produto(produto)
        messagebox.showinfo("Sucesso", f"Produto {nome} atualizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def excluir_produto_func():
    codigo = entry_codigo_barras.get()
    if messagebox.askyesno("Confirmação", f"Quer mesmo excluir o produto {codigo}?"):
        try:
            excluir_produto(codigo)
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

def atualizar_funcionario_func():
    global funcionario
    try:
        id_funcionario = int(entry_funcionario_id.get())
        nome = entry_funcionario_nome.get()
        email = entry_funcionario_email.get()
        telefone = entry_funcionario_telefone.get()
        cargo = entry_funcionario_cargo.get()
        salario = float(entry_funcionario_salario.get())
        funcionario = Funcionario(id_funcionario, nome, email, telefone, cargo, salario)
        atualizar_funcionario(funcionario)
        messagebox.showinfo("Sucesso", f"Funcionário {nome} atualizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def excluir_funcionario_func():
    id_funcionario = entry_funcionario_id.get()
    if messagebox.askyesno("Confirmação", f"Quer mesmo excluir o funcionário {id_funcionario}?"):
        try:
            excluir_funcionario(id_funcionario)
            messagebox.showinfo("Sucesso", "Funcionário excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

# Telas

    
def abrir_tela_cliente():
    tela = ctk.CTkToplevel()
    tela.title("Cadastro de Cliente")

    global entry_cpf, entry_nome, entry_email, entry_telefone, entry_cidade

    ctk.CTkLabel(tela, text="CPF:").grid(row=0, column=0, pady=5)
    entry_cpf = ctk.CTkEntry(tela)
    entry_cpf.grid(row=0, column=1, pady=5)

    ctk.CTkLabel(tela, text="Nome:").grid(row=1, column=0, pady=5)
    entry_nome = ctk.CTkEntry(tela)
    entry_nome.grid(row=1, column=1, pady=5)

    ctk.CTkLabel(tela, text="Email:").grid(row=2, column=0, pady=5)
    entry_email = ctk.CTkEntry(tela)
    entry_email.grid(row=2, column=1, pady=5)

    ctk.CTkLabel(tela, text="Telefone:").grid(row=3, column=0, pady=5)
    entry_telefone = ctk.CTkEntry(tela)
    entry_telefone.grid(row=3, column=1, pady=5)

    ctk.CTkLabel(tela, text="Cidade:").grid(row=4, column=0, pady=5)
    entry_cidade = ctk.CTkEntry(tela)
    entry_cidade.grid(row=4, column=1, pady=5)

    ctk.CTkButton(tela, text="Adicionar Cliente", command=adicionar_cliente).grid(row=5, columnspan=2, pady=10)
    ctk.CTkButton(tela, text="Atualizar Cliente", command=atualizar_cliente_func).grid(row=6, columnspan=2, pady=10)
    ctk.CTkButton(tela, text="Excluir Cliente", command=excluir_cliente_func).grid(row=7, columnspan=2, pady=10)

def abrir_tela_produto():
    tela = ctk.CTkToplevel()
    tela.title("Cadastro de Produto")

    global entry_codigo_barras, entry_produto_nome, entry_produto_preco, entry_produto_quantidade

    ctk.CTkLabel(tela, text="Código de Barras:").grid(row=0, column=0, pady=5)
    entry_codigo_barras = ctk.CTkEntry(tela)
    entry_codigo_barras.grid(row=0, column=1, pady=5)

    ctk.CTkLabel(tela, text="Nome:").grid(row=1, column=0, pady=5)
    entry_produto_nome = ctk.CTkEntry(tela)
    entry_produto_nome.grid(row=1, column=1, pady=5)

    ctk.CTkLabel(tela, text="Valor Unitário:").grid(row=2, column=0, pady=5)
    entry_produto_preco = ctk.CTkEntry(tela)
    entry_produto_preco.grid(row=2, column=1, pady=5)

    ctk.CTkLabel(tela, text="Quantidade:").grid(row=3, column=0, pady=5)
    entry_produto_quantidade = ctk.CTkEntry(tela)
    entry_produto_quantidade.grid(row=3, column=1, pady=5)

    ctk.CTkButton(tela, text="Adicionar Produto", command=adicionar_produto).grid(row=4, columnspan=2, pady=10)
    ctk.CTkButton(tela, text="Atualizar Produto", command=atualizar_produto_func).grid(row=5, columnspan=2, pady=10)
    ctk.CTkButton(tela, text="Excluir Produto", command=excluir_produto_func).grid(row=6, columnspan=2, pady=10)

def abrir_tela_funcionario():
    tela = ctk.CTkToplevel()
    tela.title("Cadastro de Funcionário")

    global entry_funcionario_id, entry_funcionario_nome, entry_funcionario_email, entry_funcionario_telefone, entry_funcionario_cargo, entry_funcionario_salario

    ctk.CTkLabel(tela, text="ID:").grid(row=0, column=0, pady=5)
    entry_funcionario_id = ctk.CTkEntry(tela)
    entry_funcionario_id.grid(row=0, column=1, pady=5)

    ctk.CTkLabel(tela, text="Nome:").grid(row=1, column=0, pady=5)
    entry_funcionario_nome = ctk.CTkEntry(tela)
    entry_funcionario_nome.grid(row=1, column=1, pady=5)

    ctk.CTkLabel(tela, text="Email:").grid(row=2, column=0, pady=5)
    entry_funcionario_email = ctk.CTkEntry(tela)
    entry_funcionario_email.grid(row=2, column=1, pady=5)

    ctk.CTkLabel(tela, text="Telefone:").grid(row=3, column=0, pady=5)
    entry_funcionario_telefone = ctk.CTkEntry(tela)
    entry_funcionario_telefone.grid(row=3, column=1, pady=5)

    ctk.CTkLabel(tela, text="Cargo:").grid(row=4, column=0, pady=5)
    entry_funcionario_cargo = ctk.CTkEntry(tela)
    entry_funcionario_cargo.grid(row=4, column=1, pady=5)

    ctk.CTkLabel(tela, text="Salário:").grid(row=5, column=0, pady=5)
    entry_funcionario_salario = ctk.CTkEntry(tela)
    entry_funcionario_salario.grid(row=5, column=1, pady=5)

    ctk.CTkButton(tela, text="Adicionar Funcionário", command=adicionar_funcionario).grid(row=6, columnspan=2, pady=10)
    ctk.CTkButton(tela, text="Atualizar Funcionário", command=atualizar_funcionario_func).grid(row=7, columnspan=2, pady=10)
    ctk.CTkButton(tela, text="Excluir Funcionário", command=excluir_funcionario_func).grid(row=8, columnspan=2, pady=10)

def abrir_tela_compra():
    tela = ctk.CTkToplevel()
    tela.title("Registrar Compra")

    carrinho = []
    total_compra = ctk.StringVar(value="0.00")

    def adicionar_item():
        codigo = entry_codigo_barras.get()
        try:
            quantidade = int(entry_quantidade.get())
        except ValueError:
            messagebox.showerror("Erro", "Quantidade inválida.")
            return

        produtos = obter_produtos()
        produto = next((p for p in produtos if p['codigo_barras'] == codigo), None)

        if not produto:
            messagebox.showerror("Erro", "Produto não encontrado.")
            return

        preco_unitario = float(produto['valor_unitario'])
        subtotal = preco_unitario * quantidade
        carrinho.append({
            "codigo_barras": codigo,
            "nome": produto['nome'],
            "quantidade": quantidade,
            "preco_unitario": preco_unitario,
            "subtotal": subtotal
        })

        atualizar_lista_itens()
        atualizar_total()

    def remover_item():
        selecionado = listbox_carrinho.curselection()
        if not selecionado:
            return
        index = selecionado[0]
        del carrinho[index]
        atualizar_lista_itens()
        atualizar_total()

    def atualizar_lista_itens():
        listbox_carrinho.configure(state="normal")
        listbox_carrinho.delete("1.0", "end")
        for item in carrinho:
            listbox_carrinho.insert("end", f"{item['nome']} x{item['quantidade']} - R${item['subtotal']:.2f}\n")
        listbox_carrinho.configure(state="disabled")

    def atualizar_total():
        total = sum(item['subtotal'] for item in carrinho)
        total_compra.set(f"{total:.2f}")

    def registrar_compra_carrinho():
            if not carrinho:
                messagebox.showwarning("Aviso", "Carrinho vazio.")
                return

            cpf_cliente = entry_cpf_cliente.get()
            id_funcionario = entry_id_funcionario.get()
            nota = gerar_nota_fiscal()

            for item in carrinho:
                compra = Compra(
                    cpf_cliente=cpf_cliente,
                    codigo_barras_produto=item['codigo_barras'],
                    id_funcionario=id_funcionario,
                    quantidade=item['quantidade'],
                    valor_total=item['subtotal'],
                    nota_fiscal=nota
                )
                registrar_compra(compra)

            messagebox.showinfo("Sucesso", f"Compra registrada com sucesso!\nNota Fiscal: {nota}")
            tela.destroy()


    # Campos de entrada
    global entry_cpf_cliente, entry_codigo_barras, entry_id_funcionario, entry_quantidade

    ctk.CTkLabel(tela, text="CPF do Cliente:").grid(row=0, column=0, pady=5)
    entry_cpf_cliente = ctk.CTkEntry(tela)
    entry_cpf_cliente.grid(row=0, column=1, pady=5)

    ctk.CTkLabel(tela, text="Código de Barras:").grid(row=1, column=0, pady=5)
    entry_codigo_barras = ctk.CTkEntry(tela)
    entry_codigo_barras.grid(row=1, column=1, pady=5)

    ctk.CTkLabel(tela, text="Quantidade:").grid(row=2, column=0, pady=5)
    entry_quantidade = ctk.CTkEntry(tela)
    entry_quantidade.grid(row=2, column=1, pady=5)

    ctk.CTkLabel(tela, text="ID do Funcionário:").grid(row=3, column=0, pady=5)
    entry_id_funcionario = ctk.CTkEntry(tela)
    entry_id_funcionario.grid(row=3, column=1, pady=5)

    ctk.CTkButton(tela, text="Adicionar Item", command=adicionar_item).grid(row=4, column=0, pady=5)
    ctk.CTkButton(tela, text="Remover Item", command=remover_item).grid(row=4, column=1, pady=5)

    listbox_carrinho = ctk.CTkTextbox(tela, height=100, width=300)
    listbox_carrinho.grid(row=5, column=0, columnspan=2, pady=5)
    listbox_carrinho.configure(state="disabled")  # Bloqueia edição manual

    ctk.CTkLabel(tela, text="Total da Compra:").grid(row=6, column=0)
    ctk.CTkLabel(tela, textvariable=total_compra).grid(row=6, column=1)

    ctk.CTkButton(tela, text="Registrar Compra", command=registrar_compra_carrinho).grid(row=7, columnspan=2, pady=10)
#Tela de Resumo Geral 

def mostrar_resumo_geral():
    clientes = obter_clientes()
    produtos = obter_produtos()
    funcionarios = obter_funcionarios()
    compras = obter_compras()

    texto = "=== CLIENTES ===\n"
    for c in clientes:
        texto += f"CPF: {c['cpf']} | Nome: {c['nome']} | Email: {c['email']} | Telefone: {c['telefone']} | Cidade: {c['cidade']}\n"

    texto += "\n=== PRODUTOS ===\n"
    for p in produtos:
        texto += f"Código de Barras: {p['codigo_barras']} | Nome: {p['nome']} | Valor Unitário: {p['valor_unitario']} | Quantidade: {p['quantidade']}\n"

    texto += "\n=== FUNCIONÁRIOS ===\n"
    for f in funcionarios:
        texto += f"ID: {f['id_funcionario']} | Nome: {f['nome']} | Email: {f['email']} | Telefone: {f['telefone']} | Cargo: {f['cargo']} | Salário: {f['salario']}\n"

    texto += "\n=== COMPRAS ===\n"
    for c in compras:
        texto += f"Nota Fiscal: {c['nota_fiscal']} | CPF Cliente: {c['cpf_cliente']} | Código Produto: {c['codigo_barras_produto']} | ID Funcionário: {c['id_funcionario']} | Quantidade: {c['quantidade']} | Valor Total: {c['valor_total']}\n"

    janela_resumo = ctk.CTkToplevel()
    janela_resumo.title("Resumo Geral")
    text_box = ctk.CTkTextbox(janela_resumo, width=800, height=600)
    text_box.pack(padx=20, pady=20)
    text_box.insert("1.0", texto)

# Função para sair da aplicação
def sair():
    app.destroy()

# Tela principal
app = ctk.CTk()
app.title("Sistema de Cadastro")
app.geometry("230x380")

ctk.CTkButton(app, text="Cadastrar Cliente", command=abrir_tela_cliente).grid(row=0, column=0, padx=40, pady=10)
ctk.CTkButton(app, text="Cadastrar Produto", command=abrir_tela_produto).grid(row=1, column=0, padx=20, pady=10)
ctk.CTkButton(app, text="Cadastrar Funcionário", command=abrir_tela_funcionario).grid(row=2, column=0, padx=20, pady=10)
ctk.CTkButton(app, text="Registrar Compra", command=abrir_tela_compra).grid(row=3, column=0, padx=20, pady=10)
ctk.CTkButton(app, text="Falar com Suporte", command=abrir_chatbot).grid(row=5, column=0, padx=20, pady=10)
ctk.CTkButton(app, text="Resumo do Geral", command=mostrar_resumo_geral).grid(row=6, column=0, columnspan=2, pady=5)

# ✅ Botão Sair
ctk.CTkButton(app, text="Sair", command=sair).grid(row=7, column=0, padx=20, pady=15)

app.mainloop()
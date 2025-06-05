import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from db import obter_funcionarios

def gerar_grafico_salarios():
    funcionarios = obter_funcionarios()
    
    nomes = [f['nome'] for f in funcionarios]
    salarios = [f['salario'] for f in funcionarios]
    
    plt.figure(figsize=(10, 6))
    plt.bar(nomes, salarios, color='green')
    plt.xlabel('Nome do Funcionário')
    plt.ylabel('Salário')
    plt.title('Salários dos Funcionários')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def criar_interface():
    root = tk.Tk()
    root.title("Escolha o gráfico a ser gerado")
    root.geometry("300x150")
    
    # Fundo preto da janela
    root.configure(bg='black')
    
    # Configurar estilo ttk para botão azul e fundo preto
    style = ttk.Style(root)
    style.theme_use('clam')  # tema que permite customização melhor
    style.configure('TButton', background='#0078D7', foreground='white', font=('Arial', 10, 'bold'))
    style.map('TButton',
        background=[('active', '#005A9E')],
        foreground=[('active', 'white')]
    )
    style.configure('TLabel', background='black', foreground='white', font=('Arial', 14))
    
    label = ttk.Label(root, text="Escolha o gráfico a ser gerado", style='TLabel')
    label.pack(pady=20)
    
    btn_funcionarios = ttk.Button(root, text="Funcionários e cargos", style='TButton', command=gerar_grafico_salarios)
    btn_funcionarios.pack()
    
    root.mainloop()

if __name__ == "__main__":
    criar_interface()

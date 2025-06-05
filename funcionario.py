class Funcionario:
    def __init__(self, id_funcionario, nome, email, telefone, cargo, salario=0):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cargo = cargo
        self.salario = salario

class Compra:
    def __init__(self, cpf_cliente, codigo_barras_produto, id_funcionario, quantidade, valor_total, nota_fiscal):
        self.cpf_cliente = cpf_cliente
        self.codigo_barras_produto = codigo_barras_produto
        self.id_funcionario = id_funcionario
        self.quantidade = quantidade
        self.valor_total = valor_total
        self.nota_fiscal = nota_fiscal

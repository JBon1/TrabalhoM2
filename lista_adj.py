from db import obter_compras

def construir_lista_adjacencia():
    compras = obter_compras()
    grafo = {}

    for compra in compras:
        cpf = compra['cpf_cliente']
        produto = compra['codigo_barras_produto']

        if cpf not in grafo:
            grafo[cpf] = []

        grafo[cpf].append(produto)

    return grafo

grafo = construir_lista_adjacencia()
for cliente, produtos in grafo.items():
    print(f"Cliente CPF {cliente} comprou os produtos: {produtos}")

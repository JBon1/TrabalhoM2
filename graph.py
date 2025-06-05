# graph.py

class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def adicionar_aresta(self, cliente1, cliente2):
        if cliente1 not in self.grafo:
            self.grafo[cliente1] = []
        if cliente2 not in self.grafo:
            self.grafo[cliente2] = []
        self.grafo[cliente1].append(cliente2)
        self.grafo[cliente2].append(cliente1)
    
    def exibir_grafo(self):
        for cliente, relacionados in self.grafo.items():
            print(f'{cliente}: {[relacionado for relacionado in relacionados]}')
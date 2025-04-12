class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []

    def adicionar_vizinho(self, vizinho_nome):
        if vizinho_nome not in self.vizinhos:
            self.vizinhos.append(vizinho_nome)

class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, nome):
        if nome not in self.vertices:
            self.vertices[nome] = Vertice(nome)

    def adicionar_aresta(self, origem, destino):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.vertices[origem].adicionar_vizinho(destino)

    def construir_de_dict(self, grafo_dict):
        for origem, destinos in grafo_dict.items():
            for destino in destinos:
                self.adicionar_aresta(origem, destino)

    def encontrar_menor_caminho(self, origem, destino):
        if origem not in self.vertices or destino not in self.vertices:
            return None

        visitados, caminho_atual, menor_caminho = set(), [], []

        def dfs_recursiva(vertice_nome):
            visitados.add(vertice_nome)
            caminho_atual.append(vertice_nome)

            if vertice_nome == destino:
                if not menor_caminho or len(caminho_atual) < len(menor_caminho):
                    menor_caminho[:] = caminho_atual.copy()
            else:
                for vizinho_nome in self.vertices[vertice_nome].vizinhos:
                    if vizinho_nome not in visitados:
                        dfs_recursiva(vizinho_nome)

            visitados.remove(vertice_nome)
            caminho_atual.pop()

        dfs_recursiva(origem)
        return menor_caminho

exemplo_grafo = {
    'a': ['b', 'd', 'i'],
    'b': ['a', 'h'],
    'c': ['d', 'f', 'h'],
    'd': ['a', 'c', 'e'],
    'e': ['d', 'i'],
    'f': ['c', 'g'],
    'g': ['f'],
    'h': ['b', 'c'],
    'i': ['a', 'e']
}

grafo = Grafo()
grafo.construir_de_dict(exemplo_grafo)

origem, destino = 'a', 'g'
caminho = grafo.encontrar_menor_caminho(origem, destino)

if caminho:
    print(f"\nCaminho encontrado de {origem} para {destino}: {' -> '.join(caminho)}")
else:
    print(f"\nNão existe caminho de {origem} para {destino}")
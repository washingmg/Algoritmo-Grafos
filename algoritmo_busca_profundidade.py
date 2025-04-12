def busca_em_profundidade(grafo, origem, destino):

    if origem not in grafo:
        raise ValueError(f"Vértice de origem '{origem}' não existe no grafo.")
    if destino not in grafo:
        raise ValueError(f"Vértice de destino '{destino}' não existe no grafo.")

    visitados = set()       
    caminho_atual = []      
    caminho_encontrado = [] 

    def explorar(vertice):
        visitados.add(vertice)
        caminho_atual.append(vertice)

        if vertice == destino:
            if not caminho_encontrado or len(caminho_atual) < len(caminho_encontrado):
                caminho_encontrado[:] = caminho_atual.copy()
        else:
            for vizinho in grafo.get(vertice, []):
                if vizinho not in visitados:
                    explorar(vizinho)

        visitados.remove(vertice)
        caminho_atual.pop()

    explorar(origem)
    return caminho_encontrado

grafo = {
    'a': ['b', 'd', 'i'],
    'b': ['a', 'h'],
    'c': ['d', 'f', 'h'],
    'd': ['a', 'c', 'e'],
    'e': ['d', 'i'],
    'f': ['c', 'g'],
    'g': ['f'],
    'h': ['b', 'c'],
    'i': ['a', 'e'],
}

origem, destino = 'a', 'g'

try:
    caminho = busca_em_profundidade(grafo, origem, destino)
    print("\nResultado da Busca em Profundidade:")
    if caminho:
        print(f"Caminho encontrado de {origem} para {destino}: {' -> '.join(caminho)}")
        print(f"Tamanho do caminho: {len(caminho)-1} arestas")
    else:
        print(f"Não existe caminho de {origem} para {destino}")
        
except ValueError as e:
    print(f"Erro: {e}")
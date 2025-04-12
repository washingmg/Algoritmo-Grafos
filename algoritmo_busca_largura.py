def busca_em_largura(grafo, inicio):
    if inicio not in grafo:
        raise ValueError(f"O vértice inicial '{inicio}' não existe no grafo.")
    
    visitados = set()
    fila = []
    ordem_visita = []
    distancia = {}
    
    fila.append(inicio)
    visitados.add(inicio)
    distancia[inicio] = 0
    
    while fila:
        atual = fila.pop(0)
        ordem_visita.append(atual)
        
        for vizinho in grafo.get(atual, []):  
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                distancia[vizinho] = distancia[atual] + 1
    
    nao_visitados = set(grafo.keys()) - visitados
    
    if nao_visitados:
        print(f"Aviso: Vértices inalcançáveis a partir de '{inicio}': {', '.join(nao_visitados)}")
    
    return ordem_visita, distancia

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

inicio = 'a'
try:
    ordem_visita, distancias = busca_em_largura(grafo, inicio)
    print(f"Ordem de visita a partir de '{inicio}': {' -> '.join(ordem_visita)}")
    print(f"Distâncias a partir de '{inicio}': {distancias}")
    
except ValueError as e:
    print(e)
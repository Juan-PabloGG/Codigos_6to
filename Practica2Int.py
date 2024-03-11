from collections import deque

def busca_ancho(ni, grafo):
    visitados = set()
    visitados_ordenados = []

    queue = deque([ni])

    while queue:
        nodo = queue.popleft()
        if nodo not in visitados:
            visitados.add(nodo)
            visitados_ordenados.append(nodo)

            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    queue.append(vecino)

    return visitados_ordenados

def bus_ancho(E, ni):
    grafo = {}
    
    for u, v in E:
        if u not in grafo:
            grafo[u] = []
        if v not in grafo:
            grafo[v] = []
        grafo[u].append(v)
        grafo[v].append(u)

    vertices_visitados = busca_ancho(ni, grafo)

    return vertices_visitados

E = [('a', 'b'), ('a', 'c'), ('a', 'g'), ('b', 'a'), ('b', 'd'), ('c', 'a'),
     ('c', 'd'), ('c', 'e'), ('d', 'b'), ('d', 'c'), ('d', 'f'), ('e', 'c'),
     ('e', 'f'), ('e', 'g'), ('f', 'd'), ('f', 'e'), ('f', 'h'), ('g', 'a'),
     ('g', 'e'), ('h', 'f')]

vertices_visitados = bus_ancho(E, 'a')
print(vertices_visitados)
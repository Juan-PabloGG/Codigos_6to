
def busca_profundidad(nodo, grafo, visitados):
    visitados.add(nodo)
    visitados_ordenados = [nodo]

    for vecino in grafo[nodo]:
        if vecino not in visitados:
            visitados_ordenados.extend(busca_profundidad(vecino, grafo, visitados))

    return visitados_ordenados

def bus_profundidad(E, ni):
    grafo = {}
    
    for u, v in E:
        if u not in grafo:
            grafo[u] = []
        if v not in grafo:
            grafo[v] = []
        grafo[u].append(v)
        grafo[v].append(u)

    visitados = set()
    vertices_visitados = busca_profundidad(ni, grafo, visitados)

    return vertices_visitados

E = [('a', 'b'), ('a', 'c'), ('a', 'g'), ('b', 'a'), ('b', 'd'), ('c', 'a'),
     ('c', 'd'), ('c', 'e'), ('d', 'b'), ('d', 'c'), ('d', 'f'), ('e', 'c'),
     ('e', 'f'), ('e', 'g'), ('f', 'd'), ('f', 'e'), ('f', 'h'), ('g', 'a'),
     ('g', 'e'), ('h', 'f')]

vertices_visitados = bus_profundidad(E, 'a')
print(vertices_visitados)

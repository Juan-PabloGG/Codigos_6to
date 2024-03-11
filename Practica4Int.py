def dijkstra(w, a, z, L):
    L = {vertex: float('inf') for vertex in w}
    L[a] = 0

    T = set(w)

    while T:
        v = min(T, key=lambda vertex: L[vertex])
        T.remove(v)

        for x in w[v]:
            if L[x] > L[v] + w[v][x]:
                L[x] = L[v] + w[v][x]

    return L[z]

w = {
    'a': {'b': 2, 'f': 1},
    'b': {'a': 2, 'c': 2, 'd': 2, 'e': 4},
    'c': {'b': 2, 'e': 3, 'z': 1},
    'd': {'b': 2, 'e': 4, 'f': 3},
    'e': {'b': 4, 'c': 3, 'd': 4, 'g': 7},
    'f': {'a': 1, 'd': 3, 'g': 5},
    'g': {'e': 7, 'f': 5, 'z': 6},
    'z': {'c': 1, 'g': 6}
}

a = 'a'
z = 'z'
L = 0
corto = dijkstra(w, a, z, L)

print(f"La longitud de la ruta más corta de '{a}' a '{z}' es: {corto}")

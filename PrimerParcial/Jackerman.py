from collections import deque


def getBestItem(distances, visited):
    minDistance = float("inf")
    best = -1
    for i in range(len(distances)):
        if not visited[i] and distances[i] < minDistance:
            best = i
            minDistance = distances[i]
    return best


def dijkstra(g, origen):
    n = len(g)
    distances = [float("inf")] * n
    visited = [False] * n
    parents = [-1] * n
    distances[origen] = 0

    for _ in range(n):
        nextNode = getBestItem(distances, visited)
        if nextNode == -1:
            break  # Si no hay más nodos accesibles, terminamos.

        visited[nextNode] = True

        for _, neighbor, weight in g[nextNode]:
            newDistance = distances[nextNode] + weight
            if not visited[neighbor] and newDistance < distances[neighbor]:
                parents[neighbor] = nextNode
                distances[neighbor] = newDistance

    return distances, parents


def reconstruct_path(parents, end):
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parents[current]
    return path[::-1]  # Invertimos el camino para obtenerlo desde el origen.


# Entrada de datos
n, m = map(int, input().strip().split())
g = [[] for _ in range(n)]
for _ in range(m):
    o, d, s = map(int, input().strip().split())
    g[o].append((o, d, s))
    g[d].append((d, o, s))

p = int(input().strip())
ids_nodes = set()
for _ in range(p):
    ids = int(input().strip())
    ids_nodes.add(ids)

# Solución
soluciones = []

for i in range(n):
    sol, camino = dijkstra(g, i)  # Distancias y padres desde el nodo i
    total_latencia = sum(sol)  # Latencia total acumulada desde el nodo i
    soluciones.append((total_latencia, i, camino, sol))

# Ordenamos por latencia total (descendente), y en caso de empate, por índice del nodo (ascendente).
soluciones.sort(key=lambda x: (-x[0], x[1]))

# Nodo inicial óptimo
mejor_solucion = soluciones[0]
latencia_total, nodo_inicial, parents, distancias = mejor_solucion

print(nodo_inicial, latencia_total)

# Encontrar el camino óptimo con menos IDS y más nodos visitados
camino_optimo = []
menos_ids = float('inf')
for destino in range(n):
    if destino == nodo_inicial:
        continue
    camino = reconstruct_path(parents, destino)
    ids_en_camino = sum(1 for nodo in camino if nodo in ids_nodes)

    # Actualizamos el mejor camino si:
    # 1. Tiene menos IDS, o
    # 2. Tiene la misma cantidad de IDS pero más nodos, o
    # 3. Tiene la misma cantidad de IDS y nodos pero termina en un nodo con menor ID.
    if (
        ids_en_camino < menos_ids or
        (ids_en_camino == menos_ids and len(camino) > len(camino_optimo)) or
        (ids_en_camino == menos_ids and len(camino) == len(camino_optimo) and camino[-1] < camino_optimo[-1])
    ):
        camino_optimo = camino
        menos_ids = ids_en_camino

print(" ".join(map(str, camino_optimo)))
print(menos_ids)

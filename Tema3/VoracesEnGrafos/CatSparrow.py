# Algorithmic definition

def selectMinDistance(distancias,visited):
    minDistance = float('inf')
    bestItem = 0
    for i in range(len(distancias)):
        if not visited[i] and distancias[i] < minDistance:
            minDistance = distancias[i]
            bestItem = i
    return bestItem


def dijkstra(g,origen,destino):
    n= len(g)
    distancias =[float("inf")] * n
    visited=[False] * n
    camas=[-1] * n
    distancias[origen] = 0

    for _ in range(n):
        nextNode = selectMinDistance(distancias,visited)
        if nextNode == -1:
            break
        visited[nextNode] = True
        if nextNode == destino:
            break
        for start,end,weight in g[nextNode]:
            if not visited[end]:
                nuevaDistancia = distancias[nextNode] + weight
                if nuevaDistancia < distancias[end]:
                    distancias[end] = nuevaDistancia
                    camas[end] = nextNode
    camino = []
    actual = destino
    while actual != -1:
        camino.append(actual)
        actual = camas[actual]
    camino.reverse()

    return distancias[destino],camino

# Data definition
n,m=map(int,input().strip().split())
g = []
for _ in range(n):
    g.append([])
for _ in range(m):
    a,b,c=map(int,input().strip().split())
    g[a].append((a,b,c))
    g[b].append((b,a,c))


camaOrigen,camaDestino = map(int,input().strip().split())

distancia,camino=dijkstra(g,camaOrigen,camaDestino)
print(distancia)
print(" ".join(map(str,camino)))
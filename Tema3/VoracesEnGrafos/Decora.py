# Algorithmic definition
def getBestItem(distances,visited):
    minDistance = float('inf')
    bestItem = 0
    for i in range(len(distances)):
        if not visited[i] and distances[i] < minDistance:
            minDistance = distances[i]
            bestItem = i
    return bestItem

def dijkstra(g,origen):
    n= len(g)
    distances = [float('inf')] * n
    visited = [False] * n
    visited[origen] = True
    distances[origen] = 0

    for start,end,weight in g[origen]:
        distances[end] = weight
    for _ in range(n-1):
        nextNode = getBestItem(distances,visited)
        visited[nextNode] = True
        for start,end,weight in g[nextNode]:
            distances[end] = min(distances[end],distances[start] + weight)
    contandor = 0
    for k in range(n):
        contandor += distances[k]
    return contandor




# Data definition
n,m,tiempoMax = map(int,input().strip().split())
g=[]
for _ in range(n):
    g.append([])
for _ in range(m):
    h1,h2,d= map(int,input().strip().split())
    g[h1].append((h1,h2,d))
    g[h2].append((h2,h1,d))
nodo = 0

tiempoTotal= dijkstra(g,nodo)
if tiempoTotal > tiempoMax:
    print("Aleg, ¡a decorar!")
else:
    print(tiempoTotal)

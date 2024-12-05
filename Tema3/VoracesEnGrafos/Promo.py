# Dijkstra definition
def getItem(distances,visited):
    minDistance = float('inf')
    bestItem = 0
    for i in range(len(distances)):
        if not visited[i] and distances[i] < minDistance:
            minDistance = distances[i]
            bestItem = i
    return bestItem
def dijkstra(g,origen):
    n = len(g)-1

    visited =[False] * (n+1)
    distances = [float('inf')] * (n+1)
    visited[origen] = True
    distances[origen] = 0
    for start,end,weight in g[origen]:
        distances[end] = weight
    for _ in range(1,len(g)):
        nextNode = getItem(distances,visited)
        visited[nextNode] = True
        for start,end,weight in g[nextNode]:
            distances[end] = min(distances[end],distances[start] + weight)
    return distances



# Data definition
n,m = map(int,input().strip().split())
g = []
solucion =[]
for _ in range(n):
    g.append([])
listaActividades= list(map(int,input().strip().split()))
actividades = set(listaActividades)
for z in range(len(actividades)):
    solucion.append(float('inf'))
for i in range(m):
    c,d,l = map(int,input().strip().split())
    g[c].append((c,d,l))
    g[d].append((d,c,l))
for j in range(n):
    sol = dijkstra(g,j)
    for l in range(n):
        miN = float('inf')
        if listaActividades[l] == listaActividades[j] and sol[l] != 0 and sol[l] < miN :
            miN = sol[l]
            if solucion[listaActividades[j]] > miN:
                solucion[listaActividades[j]] = miN
print(*solucion)






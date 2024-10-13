import heapq
from collections import deque


#bfs algoritm definition

def bfs_aux(g,v,visited,lista):
    q= []
    visited[v] = True
    heapq.heappush(q,v)
    while q:
        aux = heapq.heappop(q) # Sacar el nodo con el menor valor
        lista.append(aux)
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                heapq.heappush(q,adj) # Add los vecinos a la cola de prioridad
    return lista
def bfs(g):
    n = len(g)
    lista=[]
    visited= [False] * n
    for v in range(n):
        if not visited[v]:
            bfs_aux(g,v,visited,lista)
    return lista




#Data definition

n,m=map(int,input().strip().split())
g=[]
for i in range(n):
    g.append([])
for i in range(m):
    a,b=map(int,input().strip().split())
    g[a].append(b)

listaOrdenados=bfs(g)
print(listaOrdenados)
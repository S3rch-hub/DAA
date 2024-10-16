from collections import deque

#BFS algorithimic (Busqueda en anchura)
def bfsAux(g, visited, v,distancia,turno):
    q = deque()
    visited[v] = True
    q.append(v)
    distancia += 1
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True


def bfs(g):
    n = len(g)
    visited = [False] * n
    turno = 1
    distancia_min = 0
    for v in range(n):
        if not visited[v]:
            bfsAux(g, visited, v,distancia_min,turno)
    return distancia_min

#Data definition

n,m = map(int,input().strip().split())
g=[]
for i in range(n):
    a = list(map(int,input().strip().split()))
    g.append(a)
print(g)


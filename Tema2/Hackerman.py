from collections import deque


#BFS algorithm definition

def bfs_aux(g,v,visited):
    q= deque()
    visited[v]= True
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True



def bfs(g):
    n=len(g)
    visited=[False]*(n)
    for v in range(n):
        if not visited[v]:
            bfs_aux(g,v,visited)






#Data definition
n,m = map(int,input().strip().split())
g=[]
costeReparacion=[]
for i in range(n):
    coste=int(input("Introduce el coste de reparar el nodo {i}:"))
    costeReparacion.append(coste)
    g.append([])
for j in range(m):
    a,b = map(int,input().strip().split())
    g[a].append(b)
    g[b].append(a)

from collections import deque


#BFS


def bfs_aux(g,v,visited):
    q = deque()
    visited[v] = True
    q.append(v)
    while q:
        aux = q.popleft()
        for w in g[aux]:
            if not visited[w]:
                q.append(w)
                visited[w]= True





def bfs(g):
    n = len(g)
    visited= [False] * n
    bfs_aux(g,0,visited)
    return all(visited)


def sol(n,m,grafo,grafo_inv):
    if not bfs(grafo):
        return "CAMBIA EL ITINERARIO"
    if not bfs(grafo_inv):
        return "CAMBIA DE ITINERARIO"
    return "PERFECTO"









#Data Definition

n,m=map(int,input().strip().split())
grafo=[]
grafo_inv=[]
for i in range(0,n):
    grafo.append([])
    grafo_inv.append([])
for i in range(0,m):
    a,b=map(int,input().strip().split())
    grafo[a].append(b)
    grafo_inv[b].append(a)


print(sol(n,m,grafo,grafo_inv))

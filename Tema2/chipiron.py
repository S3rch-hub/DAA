from collections import deque

#BFS algorithimic (Busqueda en anchura)
def bfsAux(g, visited, v):
    q = deque()
    visited[v] = True
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True


def bfs(g):
    n = len(g)
    visited = [False] * n
    ncc= 0
    for v in range(0, n):
        if not visited[v]:
            bfsAux(g, visited, v)
            ncc += 1
    return ncc

#Data definition

n,m = map(int,input().strip().split())
g=[]
for i in range (n):
    g.append([])


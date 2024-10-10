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
                q.appendleft(w)
                visited[w]= True





def bfs(g):
    n = len(g)
    visited = set()
    visited= [False] * n

    for v in range(0,n):
        ciudadDestino = n
        if not visited[v]:
            bfs_aux(g,v,visited)












#Data Definition

n,m=map(int,input().strip().split())
g=[]
for i in range(n):
    g.append([])
for i in range(m):
    a,b=map(int,input().strip().split())
    g[a].append(b)


print(g)
bfs(g)
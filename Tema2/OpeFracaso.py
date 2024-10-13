from collections import deque


#BFS
def bfs_aux(g,v,visited,m):
    q= deque()
    visited[v] = True
    fans=1
    q.append([v,0])
    while q:
        aux,nivel= q.popleft()
        if nivel >= m-1:
            continue
        for adj in g[aux]:
            if not visited[adj]:
                fans += 1
                q.append((adj,nivel +1))
                visited[adj] = True
    return fans

def bfs(g,m):
    n = len(g);
    visited = [False] * n
    if m==1:
        return 1
    return bfs_aux(g,0,visited,m)

#Data definition

n=int(input())
for i in range(n):
    m,k,c=map(int,input().strip().split())
    g=[]
    for j in range(k):
        g.append([])
    for j in range(c):
        a,b=map(int,input().strip().split())
        if a<k and b<k :
            g[a].append(b)
            g[b].append(a)
    print(bfs(g,m))





# Dijkstra algorithmic definition

def selectMinDistance(distances,visited):
    minDis = float('inf')
    bestItem = 0
    for i in range(len(distances)):
        if not visited[i] and distances[i] < minDis:
            minDis = distances[i]
            bestItem = i
    return bestItem
def dijkstra(g,origen):
    n = len(g)
    distances = [float("inf")] * n
    visited = [False] * n

    visited[origen] = True
    distances[origen] = 0

    for start,end,weight in g[origen]:
        distances[end] = weight

    for _ in range(n-1):
        nextNode = selectMinDistance(distances,visited)
        visited[nextNode] = True
        for start,end,weight in g[nextNode]:
            distances[end] = min(distances[end],distances[start]+weight)
    return max(distances)








# Data definition


n,m = map(int,input().strip().split())
g = []
sol= []

for _ in range(n):
    g.append([])
    sol.append([])
for _ in range(m):
    h1,h2,d = map(int,input().strip().split())
    g[h1].append((h1,h2,d))
    g[h2].append((h2,h1,d))
for i in range(n):
    sol[i] = dijkstra(g,i)
print(max(sol))

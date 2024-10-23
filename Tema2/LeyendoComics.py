import heapq
from collections import deque


def topSort(g,grados):
    sol =[]
    heap=[]

    for k in range(len(grados)):
        if grados[k] ==0:
            heapq.heappush(heap,k)

    while heap:
        aux = heapq.heappop(heap)
        sol.append(aux)
        for adj in g[aux]:
            grados[adj] -=1
            if grados[adj] == 0:
                heapq.heappush(heap,adj)
    return sol



#Data definition

n,m=map(int,input().strip().split())
g=dict()
grados=[0] * n
for i in range(n):
    g[i] = []
for i in range(m):
    a,b=map(int,input().strip().split())
    g[a].append(b)
    grados[b] += 1

listaOrdenados = topSort(g,grados)

print(*listaOrdenados)
import copy
from collections import deque


#BFS algorithm definition

""" def eliminar_nodo(g,v):
    grafo_copia = copy.deepcopy(g)
    grafo_copia[v]= []
    n= len(g)
    for j in range(n):
        if v in grafo_copia[j]:
            grafo_copia[j].remove(v)
    return grafo_copia
"""

def eliminar_nodo(g,v):
    n=len(g)
    grafo_copia=[]
    for i in range(n):
        grafo_copia.append([])
    for z in range(n):
        for j in g[z]:
            grafo_copia[z].append(j)
    grafo_copia[v]=[]
    for k in range(n):
        if v in grafo_copia[k]:
            grafo_copia[k].remove(v)
    return grafo_copia

def bfs_aux(g,start,visited):
    q= deque()
    visited[start]= True
    q.append(start)
    while q:
        auxN = q.popleft()
        for adj in g[auxN]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True



def bfs(g,costeReparacion):
    n=len(g)
    costeTotal =0
    for v in range(n):
        grafoCopia= eliminar_nodo(g,v)
        if v!= 0:
            start = 0
        else:
            start = 1
        visited = [False] * n
        bfs_aux(grafoCopia,start,visited)
        if not all(visited[i] or i==v for i in range(n)): # Si la red esta desconectada, sumamos el precio de reparacion
            costeTotal += costeReparacion[v]
    return costeTotal



#Data definition
n,m = map(int,input().strip().split())
g=[]
costeReparacion=[]
for i in range(n):
    coste=int(input())
    costeReparacion.append(coste)
    g.append([])
for j in range(m):
    a,b = map(int,input().strip().split())
    g[a].append(b)
    g[b].append(a)

costeSistema= bfs(g,costeReparacion)
print(costeSistema)

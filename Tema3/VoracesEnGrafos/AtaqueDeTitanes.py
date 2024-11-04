# Kruskal definition
import math


def updateComponents(components,newID,oldID):
    for i in range(len(components)):
        if components[i] ==oldID:
            components[i]= newID

def sortCandidates(g):
    candidates=[]
    for node in g:
        for (start,end,weight) in node:
            candidates.append((weight,start,end))
    candidates.sort()
    return candidates
def greedyKruskal(g):
    coste = 0
    candidates= sortCandidates(g)
    components = list(range(len(g)))
    i=0
    numComponentes = len(components)
    while i<len(candidates) and numComponentes > 1:
        (weight,start,end) = candidates[i]
        if components[start] != components[end]: # Si el destino y el origen no estan en la misma componente conexa
            coste += weight
            numComponentes -= 1
            updateComponents(components,components[start],components[end])
        i += 1
    dinero=coste/5
    if coste%5 != 0:
        dinero =math.trunc(dinero)
        dinero +=1
        print(dinero)
    else:
        print(dinero)








# Data definition
n,m=map(int,input().strip().split())
g=[]


for _ in range(n):
    g.append([])
for _ in range(m):
    n1,n2,d=map(int,input().strip().split())
    n1=int(n1)
    n2=int(n2)
    d=int(d)
    g[n1].append([n1,n2,d])
    g[n2].append([n2,n1,d])
solucion =greedyKruskal(g)


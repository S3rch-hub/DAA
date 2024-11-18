# Kruskal  algorithmic defintion

'''def sortCandidates(g):
    candidates =[]
    for adjs in g:
        for start,end,weight in adjs:
            candidates.append((weight,start,end))
    candidates.sort()
    return candidates

def updateComponents(components,new_id,old_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def greedyKruskal(g):
    candidates = sortCandidates(g)
    components=list(range(len(g)))
    count = len(candidates)
    sol = 0

    costes = [0] * n
    i = 0

    while count > 1 and len(candidates) > i:
        (weight,start,end) = candidates[i]
        if components[start] != components[end]:
            sol += weight
            costes[start] += weight
            costes[end] += weight
            updateComponents(components,components[start],components[end])
        i += 1
    return sol,costes'''
from random import randint
# Prim algorithmic definition
def getBestItem(candidates,visited):
    bestCandidate = -1
    minCost = float('inf')
    for i in range(len(candidates)):
        if not visited[i] and candidates[i] < minCost:
            minCost = candidates[i]
            bestCandidate = i
    return bestCandidate,minCost

def greedyPrim(g):
    n = len(g)
    costeTotal = 0
    inicial = randint(0,n-1)
    visited = [False] * n
    candidates = [float('inf')] * n
    visited[inicial] = True
    habitaciones = [0] * n
    padre = [-1] * n

    for strart,end,weight in g[inicial]:
        candidates[end] = weight
        padre[end] = inicial
    for _ in range(n-1):
        nextNode,coste = getBestItem(candidates, visited)
        if coste==float('inf'):
            break

        costeTotal += coste
        visited[nextNode] = True
        if padre[nextNode] != -1:
            habitaciones[nextNode] += coste
            habitaciones[padre[nextNode]] += coste
        for start,end,weight in g[nextNode]:
            if not visited[end] and weight < candidates[end]:
                candidates[end] = weight
                padre[end] = nextNode

    return costeTotal,habitaciones






# Data definition
n,m = map(int,input().strip().split())
g=[]
for _ in range(n):
    g.append([])
for _ in range(m):
    a,b,c = map(int,input().strip().split())
    g[a].append((a,b,c))
    g[b].append((b,a,c))

precio,costeHabitacion = greedyPrim(g)
print(f"Coste total: {precio}")
for i in range(n):
    print(f"H{i}: {costeHabitacion[i]}")
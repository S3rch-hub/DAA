# Kruskal  algorithmic defintion

def sortCandidates(g):
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
    return sol,costes



# Data definition
n,m = map(int,input().strip().split())
g=[]
for _ in range(n):
    g.append([])
for _ in range(m):
    a,b,c = map(int,input().strip().split())
    g[a].append((a,b,c))
    g[b].append((b,a,c))

costeTotal,costes = greedyKruskal(g)
print("Coste total: "+ str(costeTotal))
for i in range(n):
    print("H"+ str(i) + ": " + str(costes[i]))
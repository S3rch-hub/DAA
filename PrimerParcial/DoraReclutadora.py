
def getBestItem(candidates,personas):
    bestRatio = -1
    bestItem = -1
    for c in candidates:
        ratio = personas[c][1] / personas[c][2]
        if ratio > bestRatio:
            bestRatio = ratio
            bestItem = c
    return bestItem
def esFactible(bestCandidate,personas,presupuesto):
    return personas[bestCandidate][2] <= presupuesto

def knapsack(personas,presupuesto):
    n = len(personas)
    sueldoTotal = 0
    solucion = [0] * n
    candidates = set()
    for q in range(n):
        candidates.add(q)
    isSol = False
    while not isSol and candidates:
        bestCandidate = getBestItem(candidates,personas)
        candidates.remove(bestCandidate)
        if esFactible(bestCandidate,personas,presupuesto):
            solucion[bestCandidate] += 1
            presupuesto -= personas[bestCandidate][2]

        else:
            solucion[bestCandidate] = presupuesto / personas[bestCandidate][2]
            isSol = True
    for q in range(n):
        if solucion[q] != 0:
            sueldoTotal += personas[q][2]
    return solucion,sueldoTotal







# Data definition
n = int(input().strip())
habilidadesPentester=[]
habilidadesCryontester=[]
habilidadesPenciltester = []

for o in range(n):
    nombre,a,s,i,g = input().strip().split()
    a= int(a)
    s = int(s)
    i = int(i)
    g = int(g)
    habilidadesPentester.append((nombre,a,g))
    habilidadesCryontester.append((nombre,s,g))
    habilidadesPenciltester.append((nombre,i,g))



p = int(input().strip())
habilidades =[]
habilidades.append(habilidadesPentester)
habilidades.append(habilidadesCryontester)
habilidades.append(habilidadesPenciltester)


presupuestosMax =[]

for r in range(p):
    x,m = map(int,input().strip().split())
    presupuestosMax.append(m)

for j in range(p):
    sol,cantidad = knapsack(habilidades[j],presupuestosMax[j])
    print(cantidad)
    for d in range(len(sol)):
        if sol[d] != 0:
            print(habilidades[j][d][0])
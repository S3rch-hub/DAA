

def getBestItem(candidates,data):
    bestItem = None
    bestRatio = -1
    for c in candidates:
        ratio = data[c][1] / data[c][2]
        if ratio > bestRatio:
            bestItem = c
            bestRatio = ratio
    return bestItem

def esFactible(bestItem,salarioMax,data):
    return data[bestItem][2] <= salarioMax

def greedyKnackpack(data,salarioMax):
    habilidad = 0
    personas =[]
    n = len (data)
    candidates = set()
    for q in range(n):
        candidates.add(q)
    isSol = False
    while candidates and not isSol:
        bestItem = getBestItem(candidates,data)
        candidates.remove(bestItem)
        if esFactible(bestItem,salarioMax,data):
            habilidad += data[bestItem][1]
            personas.append(data[bestItem][0])
            salarioMax -= data[bestItem][2]
        else:
            habilidad += data[bestItem][1]*(salarioMax/data[bestItem][2])
            personas.append(data[bestItem][0])
            isSol = True
    return habilidad,personas


# Data definition

pentester=[]
crayontester=[]
penciltester=[]
n = input().strip()
n = int(n)

for _ in range(n):
    nombre,a,s,i,g= input().strip().split()
    a =int(a)
    s =int(s)
    i =int(i)
    g =int(g)
    pentester.append((nombre,a,g))
    crayontester.append((nombre,s,g))
    penciltester.append((nombre,i,g))

p = int(input().strip())
equipos=[]
for _ in range(p):
    x,m = map(int,input().strip().split())
    equipos.append((x,m))

for j in range(p):
    habilidadTotal = 0
    contratados= []
    if equipos[j][0] == 0: # Si el perfil es pentester
        habilidadTotal,contratados = greedyKnackpack(pentester,equipos[j][1])
    elif equipos[j][0] == 1:
        habilidadTotal,contratados= greedyKnackpack(crayontester,equipos[j][1])
    else:
        habilidadTotal,contratados= greedyKnackpack(penciltester,equipos[j][1])
    print(habilidadTotal)
    print(*contratados)



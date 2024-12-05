
# Algorithmic definition

def rec_bs(lista,nivel,low,high):
    if low > high:
        return -low -1

    mid = (low + high ) // 2
    if lista[mid] == nivel:
        return mid
    elif lista[mid] > nivel:
        return rec_bs(lista,nivel,low,mid-1)
    else:
        return rec_bs(lista,nivel,mid+1,high)


def binSearchRec(lista,nivel):
    return rec_bs(lista,nivel,0,len(lista)-1)



# Data definiton

n = int(input().strip())
enemigos = list(map(int, input().strip().split()))
casos = int(input().strip())

poder = [0] * (n+1)
for i in range(n):
    poder[i+1] = poder[i] + enemigos[i]

sol =[]


for k in range(casos):

    nivelCaballero = int(input().strip())
    indice = binSearchRec(enemigos, nivelCaballero)
    i = 0
    if indice < 0:
        indice = -indice -1
        numEnemigos = indice
        poderObtenido= poder[indice]
    else:
        numEnemigos = indice + 1
        poderObtenido = poder[indice+1]
    sol.append((numEnemigos,poderObtenido))

for j in range(len(sol)):
    print(sol[j][0],sol[j][1])


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
sol =[]


for k in range(casos):
    numEnemigos = 0
    poder = 0
    nivelCaballero = int(input().strip())
    indice = binSearchRec(enemigos, nivelCaballero)
    i = 0
    if indice < 0:
        indice = -indice-1
        while i < indice:
            numEnemigos += 1
            poder += enemigos[i]
            i+=1
    else:
        while i <= indice:
            numEnemigos += 1
            poder += enemigos[i]
            i +=1
    sol.append((numEnemigos,poder))

for j in range(len(sol)):
    print(sol[j][0],sol[j][1])


# Algorithmic definition
def rec_bs(lista,numero,low,high):

    if low > high:
        return -low -1

    mid = (low + high)//2
    if lista[mid] == numero:
        return mid
    elif lista[mid] < numero:
        return rec_bs(lista,numero,mid +1, high)
    else:
        return rec_bs(lista,numero,low,mid-1)

def binarySearch(lista,numero):
    return rec_bs(lista,numero,0,len(lista)-1)




# Data definition

n = int(input().strip())

tablero=[]
sol =[]


for _ in range(n):
    filas = list(map(int,input().strip().split()))
    tablero.extend(filas)
sol = tablero.copy()
ataques = list(map(int,input().strip().split()))

ocupados = set()


for i in range(len(ataques)):
    indice = binarySearch(tablero,ataques[i])
    if indice >= 0:
        while indice < len(sol) and indice in ocupados:
            indice +=1
    else:
        indice = -indice -1
        while indice < len(sol) and indice in ocupados:
            indice += 1
    if indice < len(sol):
        sol[indice] = "X"
        ocupados.add(indice)

for i in range(n):
    print(*(sol[i * n:(i + 1) * n]))




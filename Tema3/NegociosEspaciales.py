
# GreedyCoins definition

def isSol(coste):
    return coste ==0

def isFactible(cantidad,monedas):
    return monedas <= cantidad
def greedyCoins(cantidad,monedas,solucion):
    indice = 0
    numMonedas=0
    while not isSol(cantidad):
        if isFactible(cantidad,monedas[indice]):
            solucion[indice]+= 1
            numMonedas += 1
            cantidad -= monedas[indice]
        else:
            indice +=1
    monedasCambio=[]
    for i in range(len(monedas)):
        if solucion[i] !=0:
            print()
    print(f"Numero de monedas totales: ",numMonedas)

    return solucion







#Data definition

cantidad = input()
cantidad=int(cantidad)
monedas=list(map(int,input().strip().split()))
monedas.sort(reverse=True) #Monedas estará odenado de mayor a menor
print(monedas)
solucion= [0] * len(monedas)
sol= greedyCoins(cantidad,monedas,solucion)
print(sol)
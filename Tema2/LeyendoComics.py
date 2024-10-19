
from collections import deque


def topSortVisited(data,k):
    data["estado"][k] = "VISITADO"
    data["tiempo"] += 1
    data["d"][k] = data["tiempo"]
    for adj in data["grafo"][k]: # Para cada adyacente, vemos si esta visitado
        if data["estado"][adj] == "NO VISITADO":
            topSortVisited(data,adj)
    data["estado"][k]= "TERMINADO" # Cuando nos hayamos recorrido la lista de adyacencia del nodo k, este ya lo podemos dar por terminado y lo metemos en la sol
    data["tiempo"] += 1
    data["f"][k] = data["tiempo"]
    data["sol"].appendleft(k)

def topSort(g):
    data = {
        "grafo" : g,
        "estado" : dict(),
        "d" : dict(), # Tiempo en el que se descubre por primera vez el nodo
        "f" : dict(), # Tiempo en el que se terminan de explorar todas las dependencias de un nodo
        "tiempo" : 0, # Contandor que se incrementa cada vez que se descubre o finaliza un nodo
        "sol" : deque()

    }

    for k in g.keys(): # Inicializamos los estados a NO VISITADO
        data["estado"][k] = "NO VISITADO"
        data["d"][k] = 0
        data["f"][k] = 0
    for k in g.keys(): # Para cada nodo, verificamos si no lo hemos visitado
        if data["estado"][k] == "NO VISITADO":
            topSortVisited(data,k)
    return sorted(list(data["sol"]))



#Data definition

n,m=map(int,input().strip().split())
g=dict()
for i in range(n):
    g[i] = []
for i in range(m):
    a,b=map(int,input().strip().split())
    g[a].append(b)

listaOrdenados = topSort(g)

print(listaOrdenados)
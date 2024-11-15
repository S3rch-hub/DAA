# Algorithmic definition


def greedyAlgorithmic(actividades):
    n =len(actividades)
    actividades.sort(key=lambda x:(x[1])) # Lo ordeno por hora de fin
    ultimaActividad= None
    sol=[]
    for ini,fin in actividades:
        if ultimaActividad is None or ini >=ultimaActividad:
            sol.append((ini,fin))
            ultimaActividad = fin
    totalActividades = len(sol)
    return totalActividades




# Data definition

casos = int(input().strip())
resultados=[]
for _ in range(casos):
    numActividades=int(input().strip())
    actividades = []
    listaHoras=list(map(int,input().strip().split()))
    for i in range(numActividades):
        inicio = listaHoras[2*i]
        fin = listaHoras[2*i+1]
        actividades.append([inicio,fin])
    resultados.append(greedyAlgorithmic(actividades))
for resultado in resultados:
    print(resultado)


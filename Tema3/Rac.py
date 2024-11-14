# Algorithmic definition


def greedyAlgorithmic(actividades):
    n =len(actividades)
    actividades.sort(key=lambda x:(x[0], x[1]- x[0])) # Lo ordeno por hora de inicio y en caso de que sea la misma, por duracion
    ultimaActividad= None
    sol=[]
    for ini,fin in actividades:
        if  ultimaActividad is None or ini >=ultimaActividad:
            sol.append((ini,fin))
            ultimaActividad = fin
    totalActividades = len(sol)
    return totalActividades




# Data definition

casos = int(input().strip())
for _ in range(casos):
    numActividades=int(input().strip())
    actividades=[]

    listaHoras=list(map(int,input().strip().split()))
    for i in range(numActividades):
        inicio = listaHoras[2*i]
        fin = listaHoras[2*i+1]
        actividades.append([inicio,fin])
    print(greedyAlgorithmic(actividades))




def greedy(g):
    ultima_actividad=-1
    aux= 0
    for i in g:
        fin,inicio=i[0],i[2]
        if inicio >= ultima_actividad:
            aux +=1
            ultima_actividad=fin
    return aux



# Data definition
numActividades=input()
numActividades =int(numActividades)
actividades=[]
for _ in range(numActividades):
    n,i,f=input().strip().split()
    i= int(i)
    f= int(f)
    actividades.append((f,n,i))

listaOrdenados=sorted(actividades)
activities=greedy(listaOrdenados)
print(activities)
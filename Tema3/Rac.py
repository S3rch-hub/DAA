

# Data definition

casos = int(input().strip())
for _ in range(casos):
    numActividades=int(input().strip())
    actividades=[]
    listaHoras=list(map(int,input().strip().split()))
    for i in range(numActividades):
        inicio=listaHoras[2*i]
        fin = listaHoras[2*i+1]
        actividades.append([inicio,fin])

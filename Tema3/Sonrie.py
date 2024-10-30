
def greedy(ordenados):
    listaNombre=sorted(ordenados, key=lambda x: x[1])
    numHoras=0
    persona=listaNombre[0]
    for i in ordenados:
        if i[1] == persona[1]:
            return numHoras
        numHoras+=i[4]




# Data definition


n=input()
n=int(n)
candidatos=[]
for _ in range(n):
    nombre,paciencia,urgencia,tiempo = input().strip().split()
    paciencia=int(paciencia)
    urgencia=int(urgencia)
    tiempo=int(tiempo)
    nivel = paciencia/urgencia
    candidatos.append((nivel,nombre,paciencia,urgencia,tiempo))

ordenados=sorted(candidatos)
for d, nombre, paciencia, urgencia, tiempo in ordenados:
    print(nombre)
sol=greedy(ordenados)
print(sol)
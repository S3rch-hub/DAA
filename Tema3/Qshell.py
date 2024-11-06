
# Objetivo: Maximizar las veces que se encienden las luces de la tentación

def bestItem(tentadores,candidatos,nivelAtraccion):
    best_ratio = -1
    best_candidate = -1
    for i in candidatos:
        ratio=tentadores[i][nivelAtraccion]/tentadores[i][4]
        if ratio > best_ratio:
            best_ratio = ratio
            best_candidate = i
    return best_candidate

def greedy(concursantes):
    caracteristica=concursantes[0]
    candidatos = set()
    n=concursantes[2]
    tiempo = concursantes[1]

    if caracteristica == 'beauty':
        nivelAtraccion = 1
    elif caracteristica == 'intelligence':
        nivelAtraccion = 2
    else:
        nivelAtraccion = 3

    beneficio = 0
    sol =[]

    for i in range(n):
        candidatos.add(i)



    while candidatos and tiempo >0:

        bestCandidato=bestItem(concursantes[3],candidatos,nivelAtraccion)
        tentador = concursantes[3][bestCandidato]


        if tiempo >=tentador[4]:
            tiempo -= tentador[4]
            beneficio += tentador[nivelAtraccion]
        else:
            ratio= tiempo / tentador[4]
            tiempo = 0
            beneficio += ratio * tentador[nivelAtraccion]

        sol.append(tentador[0])
        candidatos.remove(bestCandidato)
    return sol,beneficio






# Data definition
n = int(input().strip())
concursantes = []
sol=[]

for i in range(n):
    caracteristica = input().strip()
    tiempoMax = int(input().strip())
    parejas = int(input().strip())
    tentadores = []

    for _ in range(parejas):
        datos = input().strip().split()
        nombre = datos[0]
        belleza = int(datos[1])
        inteligencia = int(datos[2])
        amabilidad = int(datos[3])
        tiempoSed = int(datos[4])
        tentadores.append([nombre, belleza, inteligencia, amabilidad, tiempoSed])

    concursantes.append([caracteristica, tiempoMax, parejas, tentadores])
    parejas,beneficio = greedy(concursantes[i])
    sol.append([parejas,beneficio])
for resultado in range(len(sol)):
    for pareja in sol[resultado][0]:
        print(pareja,end="")
    print()
    print(f"{sol[resultado][1]:.2f}")





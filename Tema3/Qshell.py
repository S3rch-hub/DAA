
# Objetivo: Maximizar las veces que se encienden las luces de la tentación

def bestItem(candidatos,caracteristica,nivelAtraccion,tiempo):
    best_candidate= None
    valorMax = -1
    tiempoMin =float('inf')

    for i in candidatos:
        nombre,belleza,inteligencia,amabilidade,tiempoSed = i
        valor =i[nivelAtraccion]
        if (valor > valorMax)or (valor == valorMax and tiempoMin < tiempoMin):
            if tiempoMin <= tiempo:
                valorMax = valor
                tiempoMin =tiempoSed
                best_candidate = i
    return best_candidate

def greedy(concursantes):
    caracteristica=concursantes[0]
    candidatos = concursantes[3]
    numParejas = concursantes[2]
    tiempo = concursantes[1]

    if caracteristica == 'kindness':
        nivelAtraccion = 1
    elif caracteristica == 'intelligence':
        nivelAtraccion = 2
    else:
        nivelAtraccion = 3

    beneficio = 0
    sol =[]


    while candidatos and tiempo > 0:
        best_item= bestItem(candidatos,caracteristica,nivelAtraccion,tiempo)
        if best_item is None:
            break
        nombre,belleza,inteligencia,amabilidad,tiempoSed = best_item
        valor=best_item[nivelAtraccion]

        if tiempoSed<tiempo:
            beneficio += valor
            tiempo -=tiempoSed
            sol.append(nombre)
        else:
            beneficio += valor * (tiempo/tiempoSed)
            sol.append(nombre)
            tiempo = 0
        candidatos.remove(best_item)
    return sol, round(beneficio,2)






# Data definition
n = int(input().strip())
concursantes = []

for _ in range(n):
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

for concursante in concursantes:
    pareja,beneficio=greedy(concursante)
    print(" ".join(pareja))
    print(f"{beneficio:.2f}")



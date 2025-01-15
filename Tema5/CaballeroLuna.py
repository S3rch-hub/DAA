
def esFactible(g,x,y):
    return g[x][y] != -1

def backtracking(g,distancia,x,y,derrotados,count):
    if g[x][y] == 1:
        derrotados +=1
    movimientos = [(0,1),(1,0),(-1,0),(0,-1)]
    while count < distancia:
        for nx,ny in movimientos:
            nuevaCasillaX = x+nx
            nuevaCasillaY = y+ny
            if 0 <= nuevaCasillaX < len(g) and 0<= nuevaCasillaY < len(g[0]):
                if esFactible(g,nuevaCasillaX,nuevaCasillaY):
                    if g[nuevaCasillaX][nuevaCasillaY] == 1:
                        backtracking(g,distancia,nuevaCasillaX,nuevaCasillaY,derrotados,count+1)
                    count +=1

    return derrotados




# Data definition

n,m,e = map(int,input().strip().split())
g =[]

for i in range(n):
    filas = list(map(int,input().strip().split()))
    g.append(filas)


x,y,d = map(int,input().strip().split())

posicionInicialX = x
posicionInicialY = y
distancia = d
derrotados = 0
count = 0


enemigos = backtracking(g,distancia,posicionInicialX,posicionInicialY,derrotados,count)
print(enemigos)
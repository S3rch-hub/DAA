
movimientos = [(0,1),(1,0),(-1,0),(0,-1)]

def esFactible(newPos, visited, matrix, n, m):
    newX, newY = newPos
    return 0 <= newX < n and 0 <= newY < m and (newX,newY) not in visited and matrix[newX][newY] != -1




def vueltaAtras(n, m, matrix, e, x, y, d,visited, pos, index = 0,enemigos=0):
    actX, actY = pos

    if index == d: # El boomerang ya no puede recorrer mas casillas
        return enemigos==e

    for dx,dy in movimientos:
        newPos = (dx+actX,dy+actY)

        if esFactible(newPos,visited,matrix,n,m):
            visited.add(newPos)

            if matrix[dx+actX][dy+actY] == 1:
                enemigos +=1

            if vueltaAtras(n,m, matrix, e, x, y, d, visited, newPos, index+1, enemigos):
                return True

            if matrix[dx+actX][dy+actY] == 1: # Si no puedo ir a esa posicion, no me cargo al enemigo
                enemigos -=1
            visited.remove(newPos)


# Data definition

n,m,e = map(int,input().strip().split())
matrix =[]
visited = set()

for i in range(n):
    filas = list(map(int,input().strip().split()))
    matrix.append(filas)


x,y,d = map(int,input().strip().split())
visited.add((x,y))

if vueltaAtras(n,m,matrix,e,x,y,d,visited,(x,y)):
    print('ATACA')
else:
    print('CORRE')
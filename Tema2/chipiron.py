from collections import deque

#BFS algorithimic (Busqueda en anchura)

def bfs(g,x,y,turno,distancia_min):
    if g[x][y]== 2:
        return distancia_min
    q =deque()
    q.append((x,y,turno,distancia_min))
    visited = set()
    visited.add((x,y))
    while q:
        x,y,turno,distancia_min = q.popleft()
        if g[x][y] == 2:
            return distancia_min
        direcciones= [(1,0),(0,1),(-1,0),(0,-1)]

        if turno %2 == 1: # En los turnos impares
            for auxX,auxY in direcciones:
                nx,ny= x+auxX,y+auxY
                if 0<=nx<n and 0<=ny<m and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    q.append((nx,ny,turno + 1,distancia_min + 1))
        else: # En los turnos pares
            for auxX,auxY in direcciones:
                nx,ny= x + auxX,y + auxY
                if 0<=nx<n and 0<=ny<m and (nx,ny) not in visited:
                    if g[nx][ny] ==0 or g[nx][ny] == 2:
                        visited.add((nx,ny))
                        q.append((nx,ny,turno +1, distancia_min + 1))










#Data definition

n,m = map(int,input().strip().split())
g=[]
for i in range(n):
    a = list(map(int,input().strip().split()))
    g.append(a)
distancia_min = 0
origenX = 0
origenY = 0
turno =1
sol = bfs(g,origenX,origenY,turno,distancia_min)
print(sol)


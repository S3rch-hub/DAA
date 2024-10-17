from collections import deque

#BFS algorithimic (Busqueda en anchura)

def bfs(g,x,y,turno):
    n = len(g)
    distancia_min = 0
    if g[x][y]== 2:
        return distancia_min
    encontrado=0
    q =deque()
    while not encontrado:
        if turno %2 ==1:

            q.append((x+1,y))
            q.append((x,y+1))
            while q:
                x,y =q.popleft()
                distancia_min += 1
                if g[x][y] == 2:
                    encontrado =1








#Data definition

n,m = map(int,input().strip().split())
g=[]
for i in range(n):
    a = list(map(int,input().strip().split()))
    g.append(a)
x= 0
y = 0
turno =1
bfs(g,x,y,turno)
print(g)


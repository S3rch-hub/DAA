
#Greedy definition

def greedy(participantes,k):
    size_young=min(k,len(participantes)-k)
    for i in range(size_young):
        print(participantes[i][1],end= " ")
    print()
    for j in range(size_young,len(participantes)):
        print(participantes[j][1],end =" ")


#Data definition

n,k =map(int,input().strip().split())
participantes=[]
for _ in range(n):
    nombre,edad= input().strip().split()
    edad= int(edad)
    participantes.append((edad,nombre)) # Para que luego se ordene por edad
participantes.sort()



greedy(participantes,k)
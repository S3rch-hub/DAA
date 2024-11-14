
# Algorithmic definition
def rec_bs(id,persona,primero,ultimo):
    if primero > ultimo: # Caso base
        return -1
    else:
        mid = (primero + ultimo) // 2
        if id[mid]== persona:
            return mid
        elif persona < id[mid]:
            return rec_bs(id,persona,primero,mid-1)
        else:
            return rec_bs(id,persona,mid+1,ultimo)

def binarySearch(id,persona):
    return rec_bs(id,persona,0,len(id)-1)



# Data definition

n=int(input().strip())
id1 = list(map(int,input().strip().split()))

m = int(input().strip())

id2 = list(map(int,input().strip().split()))

p = int(input().strip())
grupo1 = []
grupo2 =[]
for _ in range(p):
    persona1,persona2 = map(int,input().strip().split())
    grupo1.append(persona1)
    grupo2.append(persona2)
for i in range(p):
    indice1 =binarySearch(id1,grupo1[i])
    indice2 = binarySearch(id2,grupo2[i])
    if indice1 >= 0 and indice2 >= 0:
        print(indice1, indice2)
    else:
        print("SIN DESTINO")



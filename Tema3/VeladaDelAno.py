

# Data definition
numActividades=input()
numActividades =int(numActividades)
actividades=[]
for _ in range(numActividades):
    n,i,f=input().strip().split()
    i= int(i)
    f= int(f)
    actividades[_] = n

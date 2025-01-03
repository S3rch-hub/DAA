

def bs_aux(array,number,low,high):
    if low > high:
        return 0
    mid = (low+high)//2
    if array[mid] == number:
        return 1
    elif array[mid] > number:
        return bs_aux(array,number,0,mid-1)
    else:
        return bs_aux(array,number,mid+1,high)

def bs_rec(array,number):
    return bs_aux(array,number,0,len(array)-1)


# Data definition

array =[]
sol =[]
n = int(input().strip())

for _ in range(n):
    a = list(map(int,input().strip().split()))
    array.append(a)


array.sort()
m = int(input().strip())

for _ in range(m):
    number = int(input().strip())
    nivel = 0
    for i in range(len(array)):
        esta = bs_rec(array[i],number)
        if esta == 1:
            nivel += 1

        while esta == 1 and i<=len(array)-1:
            number = array[i][0]
            esta = bs_rec(array[i+1], number)
            if esta == 1:
                nivel += 1
            i += 1
    sol.append(nivel)
print(sol)
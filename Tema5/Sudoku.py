
def colValida(i,k,sudoku):
    for n in range(9):
        if sudoku[i][n] == k:
            return False
    return True


def filValida(j,k,sudoku):
    for n in range(9):
        if sudoku[n][j] == k:
            return False
    return True


def cuadValido(i,j,k,sudoku):
    for x in range((i // 3) * 3, (i // 3) * 3 + 3):
        for y in range((j // 3) * 3, (j // 3) * 3 + 3):
            if sudoku[x][y] == k:
                return False
    return True


def posValida(i, j, k,sudoku):
    return colValida(i,k,sudoku) and filValida(j,k,sudoku) and cuadValido(i,j,k,sudoku)

def solve(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for k in range(1,10):
                    if posValida(i,j,k,sudoku):
                        sudoku[i][j] = k
                        if solve(sudoku): # Si lo he rellenado entero, he terminado
                            return True
                        sudoku[i][j] = 0
                return False
    return True

# Data definition

sudoku = []
for i in range(9):
    lista = list(map(int, input().split()))
    sudoku.append(lista)
if solve(sudoku):
    for fila in sudoku:
        print(*fila)
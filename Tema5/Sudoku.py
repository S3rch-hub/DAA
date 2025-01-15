
def solve(sudoku):





# Data definition

sudoku = []
for i in range(9):
    lista = list(map(int, input().split()))
    sudoku.append(lista)
if solve(sudoku):
    for fila in sudoku:
        print(*fila)
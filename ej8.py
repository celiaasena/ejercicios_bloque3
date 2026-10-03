matriz: list[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in range(3):
    for columna in range(3):
        if fila == columna:
            print(matriz[fila][columna])

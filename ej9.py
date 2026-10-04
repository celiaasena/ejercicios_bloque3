matriz: list[list[int]] = [
    [1, 2, 3, 4], 
    [2, 4, 6, 8], 
    [1, 3, 5, 7], 
    [1, 2, 3, 4]
]
suma_fila: int = 0
for numero in matriz[0]:
    suma_fila += numero 
suma_columna: int = 0
for fila in matriz:
    suma_columna += fila[0]

print("la suma de la fila 0 es:", suma_fila)
print("la suma de la columna 0 es:", suma_columna)
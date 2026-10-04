# no lo he hecho yo
matriz: list[list[str]]= [   #creo una lista que va a tener dentro otra lista de tipo str
    ["."] * 8   #creo una fila de 8 .
    for i in range(8)   #un bucle que se repita 8 veces de la fila creada anterior
]
for fila in matriz[0:4]:   #recorre las 4 primeras filas (slicing)
    print(" ".join(fila))   #imprime los elementos de la lista separados por espacios
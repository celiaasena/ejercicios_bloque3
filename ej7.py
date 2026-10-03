#DIFICIL, no lo he hecho yo
matriz = []  #creo una matriz vacia
for i in range(4):  #el bucle que voy a hacer se ejecuta 4 veces
    fila = []  #se crea una fila vacia
    for j in range(4):  #el bucle de 0 se ejecuta 4 veces
        fila.append(0)  #en la primera vuelta añade un 0, y despues ya lo hace 4 veces, y queda asi : [0, 0, 0, 0]
    matriz.append(fila)  #añade la fila a la matriz, y vuleve al bucle de las filas, es decir, para hacer otras 3 filas que le quedan

for fila in matriz:  #coge cada fila de la matriz
        for elemento in fila:  #recoore cada elemento
            print(elemento, end="")  #imprime cada elemento, pegados gracias al end=""
        print()  #este prin solo hace el salto de linea
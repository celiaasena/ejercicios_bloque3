TAMANYO_TABLERO: int = 8                           #están en letras mayúsculas porque son constantes, es decir, no van a cambiar
LETRAS_VALIDAS: str = "abcdefgh"
NUMEROS_VALIDOS: str = "12345678"

tablero_simbolos: list[list[str]] = [                                                     #con una lista de listas creo una matriz (el tablero de ajedrez), donde cada fila es una lista
    ["\u265C", "\u265E", "\u265D", "\u265B", "\u265A", "\u265D", "\u265E", "\u265C"],     # en la fila 8 pongo las 8 piezas negras
    ["\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F"],     # en la fila 7 pongo los 8 peones negros
    ["", "", "", "", "", "", "", ""],                                                     # la fila 6 está vacía
    ["", "", "", "", "", "", "", ""],                                                     # la fila 5 está vacía
    ["", "", "", "", "", "", "", ""],                                                     # la fila 4 está vacía
    ["", "", "", "", "", "", "", ""],                                                     # la fila 3 está vacía
    ["\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659"],     # en la fila 2 pongo los 8 peones blancos
    ["\u2656", "\u2658", "\u2657", "\u2655", "\u2654", "\u2657", "\u2658", "\u2656"],     # en la fila 1 pongo las 8 piezas blancas
] 


tablero_nombres: list[list[str]] = [                    #con una lista de listas creo una matriz que le pone nombre a cada uno de las piezas de la matriz anterior
    ["Torre negra", "Caballo negro", "Alfil negro", "Rey negro", "Reina negra", "Alfil negro", "Caballo negro", "Torre negra"],
    ["Peon negro", "Peon negro", "Peon negro", "Peon negro", "Peon negro", "Peon negro", "Peon negro", "Peon negro"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""], 
    ["", "", "", "", "", "", "", ""],
    ["Peon blanco", "Peon blanco", "Peon blanco", "Peon blanco", "Peon blanco", "Peon blanco", "Peon blanco"],
    ["Torre blanca", "Caballo blanco", "Alfil blanco", "Rey blanco", "Reina blanco", "Alfil blanco", "Caballo blanco", "Torre blanca"]
]

#básicamente crea un bucle que recorra 8 veces (TAMANYO_TABLERO), donde en cada vuelta le corresponde una letra, y finalmente modifica la estética del bucle para que las letras estén separadas

for indice_fila in range(TAMANYO_TABLERO):                                 #creo un bucle con una nueva variable que es numero_fila, con tamaño TAMANYO_TABLERO, es decir, 8
    numero_fila: int = TAMANYO_TABLERO - indice_fila                       #como el tablero de ajedrez empieza en el 8 y de ahí va para abajo, el numero de fila será el tamaño del tablero (8) menos el numero de vueltas que haya dado el bucle, es decir, el indice.  EJ: quiero la fila 6: 8 (total) - 2 (lleva dos vueltas al bucle)
    linea: str = str(numero_fila) + " "                                    #creo una nueva variable, que es igual a numero_fila más un espacio. Además lo convierto en str porque econ int no puedo añadir el espacio
    for indice_columna in range(TAMANYO_TABLERO):                          #creo un bucle con una nueva variable que es indice_columna, con tamaño TAMANYO_TABLERO, es decir, 8
        simbolo: str = tablero_simbolos[indice_fila][indice_columna]       #defino una nueva variable que es el simbolo que hay en la casilla que le corresponde con respecto a su fila y columna (de la matriz tablero_simbolos)
        if simbolo == "":                                                  #si no hay pieza en la casilla solicitada
            celda: str = " . "                                             #entonces guarda un punto en la variable celda
        else:                                                              #en el caso contrario (sí hay pieza)
            celda: str = " " + simbolo + " "                               #entonces imprime un espacio, el simbolo y otro espacio (los espacios son para que quede más alineado)
            linea: str = linea + celda                                     #actualizo la variable linea, que es la que va construyendo el tablero, es decir, le voy añadiendo cada celda que va recorriendo el bucle
    print(linea)

   #imprime la peticion de casilla o salida
print("")
# CON LISTAS
tablero_list: list[list[str]] = [
    [" ", " ", " "],
    [" ", "\u2656", " "],
    [" ", " ", " "]
]
for fila in tablero_list:
    print(fila)

# CON DICCIONARIOS
tablero_dict: dict = {
    "b2": "\u2656"
}
for fila in tablero_dict:
    print(fila)
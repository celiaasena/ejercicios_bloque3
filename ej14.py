pieza_en: dict = {
    "a1": "torre_blanca",
    "d1": "rey_blanco",
    "g8": "caballo_negro"
}
consultar_pieza = input("dime una pieza:")
print(pieza_en.get(consultar_pieza, "vacio")) 

# si la casilla no contiene nada de lo del diccionario, .get imprime 'vacio'

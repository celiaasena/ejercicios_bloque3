pieza_en: dict = {
    "a1": "torre_blanca",
    "d1": "rey_blanco",
    "g8": "caballo_negro",
    "b1": "caballo_blanco"
}
for casilla, pieza in pieza_en.items():  #el bucle asigna los valores 'casilla' y 'pieza' a cada una de las columnas (casilla = "a1", pieza = "torre_blanca")
    print(casilla, "->", pieza)  #imprime pieza y casilla con una flecha (mejor visualmente)

#en la primera vuelta el bucle asigna a1 a casilla y torre_blanca a pieza, y lo imprime, y otra vuelta
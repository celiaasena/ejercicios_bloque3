nombre_piezas: dict = {
    "torre_negra": "a8",
    "torre_blanca": "a1",
    "alfil_negro": "c8",
}
nombre_piezas["caballo_blanco"] = "b1"   #añado nueva
nombre_piezas["torre_negra"] = "h8"      #modifico la 1ª
del nombre_piezas["alfil_negro"]         #elimino la 3ª

print(nombre_piezas)
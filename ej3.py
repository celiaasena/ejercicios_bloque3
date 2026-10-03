letras_columna: list = ["c", "o", "l", "u", "m", "n", "a"]
print(*letras_columna[-1])
print(*letras_columna[0])
print(*letras_columna[6])
# el indice 8 daría error porque 8 esta fuera del rango, el rango llega a 6 y por lo tanto tambien -6
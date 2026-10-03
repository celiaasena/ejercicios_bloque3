tablero: list = []
for fila in range(8):
    fila_vacia: list = ["·"] * 8    
    tablero.append(fila_vacia)

tablero[7][4] = "\u265A"
print(tablero[7][4]) 
tablero[0][4] = "\u2654"
print(tablero[0][4])

print(tablero)

for i in range(8):
    print(tablero [i])

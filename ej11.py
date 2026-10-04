# MAL, porque las tuplas no se pueden modificar
#  posicion_rey: tuple = (0, 4) 
#  posicion_rey[1] = 5  

# BIEN, como las listas sí se pueden modificar lo he cambiado a una lista
posicion_rey: list = [0, 4]
posicion_rey[1] = 5  
print(posicion_rey)
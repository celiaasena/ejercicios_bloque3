lista: list = []
lista.append("alfil")  #añade
lista.append("peon")
lista.append("rey")
lista.append("reina")
eliminado = lista.pop()  #declara una variable y que haga pop
print(*lista)  #imprime la lista sin el ultimo elemento (pop)
print(eliminado)  #imprime lo que ha quitado el pop
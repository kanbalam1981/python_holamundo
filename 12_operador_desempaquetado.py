lista =[1, 2, 3, 4, 5, 6, 7]
#print(lista)    
#print(*lista) #imprime cualquier iterable
lista2 = [9,12,33]
conbinada = ["hola",* lista,"mudo", lista2,"chanchito feliz"]
print(conbinada)


# ejercicio de desempaquetamineto con diccionarios
punto1 = {"x" : 13}
punto2 = {"y" : 24}
nuevoPunto ={** punto1, ** punto2}
print(nuevoPunto)


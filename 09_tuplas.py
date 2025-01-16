numeros =(1, 2,3) + (4, 5, 6)
print (numeros)
punto = tuple ([1,2])
print(punto)
menosnumeros =numeros[:2] #nos crea una nuevva lista apartir de una tupla
print(menosnumeros)
primero, segundo, *otros = numeros #desempaquetamos los elemntos de una tupla
print(primero, segundo,otros)


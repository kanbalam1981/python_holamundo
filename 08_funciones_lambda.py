numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#numeros.sort(reverse=True) #desrdena 
numeros2 = sorted(numeros, reverse=True)#ordena un conjunto de otra lista
sorted(numeros)
print(numeros2)
usuarios = [
[3,"pelusa"],
[4,"chanchito"],
[1,"felipe"],
[5,"pulga"]
]

def ordena (elemento):
    return elemento
usuarios.sort(key = lambda el:el[1], reverse=True) #funcion lambda`` acede a un elemento de un listado ordenado al reves
print(usuarios)

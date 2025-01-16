punto ={"x" : 25, "y" : 50}
print(punto)
print(punto["x"])
print(punto["y"])

#agrefando una nueva llave
punto ["z"] = 45
#print(punto )
#accediendo a un elemneto que no exixte

if "lala" in punto :
    print("nencotre lala",punto["lala"])  # no imprime na da por que no hay nada

print (punto.get ("x"))
print (punto.get ("lala",87))

#elimina un elemento con su valor
del punto["x"]
print(punto)
del (punto["y"]) #borra una llave que esta asociado a un diccionario
print(punto)
punto ["x"] =656
print(punto)
#for valor in punto:
#   print(valor, punto[valor] )
for valor in punto.items(): #nos devuelve tuplas
    print(valor)
#desempaquetar tupas
for llave ,valor in punto.items():
    print(llave, valor)
#uso realista de los diccionarios

usuarios=[
    {"id": 1,"nombre ": "sandra"},
    {"id": 2,"nombre ": "gustavo"},
    {"id": 3,"nombre ": "byron"},
    {"id": 4,"nombre ": "sharon"},
    ]
#Accediendo a los elementos de un diccionario

for usuario in usuarios:    
     print(usuario ["nombre"])
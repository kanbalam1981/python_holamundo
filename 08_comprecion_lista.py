usuarios = [
["pelusa",4],
["chanchito",3],
["felipe",1],
["pulga",5]
]
#nombres =[]
#for usuario in usuarios:

#    nombres.append(usuario[0])
#print(nombres)
#nombres =[usuario[0]for usuario in usuarios] 
#filtrar y tranformada
#nombres=[usuario for usuario in usuarios if usuario[1]> 2]

#nombres=[usuario [0]for usuario in usuarios if usuario[1]> 2]
#nombres = list(map(lambda usuario: usuarios[0],usuarios))
menosUsuarios = list(filter(lambda usuario: usuario[1]>2,usuarios))# se utiliza en la programacion funcional
print(menosUsuarios)

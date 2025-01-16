def hola(nombre, apellido = "verastegui"):  
    print("Hola Mundo")
    print(f"bienvenido {nombre} {apellido}")

hola("byron", "verastegui")
hola("gustavo")
hola(apellido = 'verastegui', nombre = 'miniño')  # Named arguments

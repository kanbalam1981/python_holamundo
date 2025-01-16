def get_product(**datos): #estamos trabajando con kwargs con los dos **
    print(datos["id"], datos["name"])
    print(type(datos))

get_product(id = "id", name ="iphone", desc = "esto es un iphone", price = 1000)
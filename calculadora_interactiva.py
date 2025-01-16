print("calculadora interactiva")
print("1. suma")
print("2. resta")
print("3. multiplicación")
print("4. división")   
print("5. potencia")
print("6. salir")       
#print("seleccione una opción")
numero = int(input("escriba una operacion: "))

if numero  == 1:
    print("suma")
    numero1 = int(input("Digite un nunúmero: "))
    print(numero1)
    numero2 = int(input("Digite otro número: "))
    print(numero2)
    resultado = numero1 + numero2
    print(resultado)
elif numero == 2:
    print("resta")
    numero1 = int(input("Digite un nunúmero: "))
    print(numero1)
    numero2 = int(input("Digite otro número: "))
    print(numero2)

    resultado = numero - numero2
    print(resultado)    
elif numero == 3:       
    print("multiplicación")
    numero1 = int(input("Digite un nunúmero: "))
    print(numero1)
    numero2 = int(input("Digite otro número: "))
    print(numero2)
    resultado = numero1 * numero2
    print(resultado)
elif numero == 4:
    print("división")
    numero1 = int(input("Digite un nunúmero: "))
    print(numero1)
    numero2 = int(input("Digite otro número: "))
    resultado = numero / numero2
    print(resultado)    
elif numero == 5:
    print("potencia")
    numero1 = int(input("Digite un nunúmero: "))
    print(numero1)
    potencia = int(input("Digite la potencia: "))
    resultado = numero1 ** potencia
    print(resultado)
elif numero == 6:   
    print("salir")
else:
    print("opción no válida")

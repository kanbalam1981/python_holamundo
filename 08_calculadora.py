n1 = int(input("ingrese un numero: \n "))
n2 = int(input("ingrese otro numero \n"))

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2


mensage = f"""

para los numeros {n1} y {n2},
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la multiplicacion es {multiplicacion}
el resultado de la division es {division}


"""
print(mensage)
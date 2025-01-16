print("bienvenido a tu calculadora")
print ("para salir escribe  salir")
print ("las operacioines son , suma, resta,mult, division, potencia")
resultado =""
while True:
    if not resultado:
        resultado = input ("ingrese numero: ")
        if resultado.lower() =="salir":
            break
        resultado = int(resultado)
    op = input ("ingrese operacion: ")
    if op.lower () == "salir" :
        break
n2 = int(n2)
if op.lower() == "suma":
    resultado += n2
elif op.lowe() =="resta":
    resultado -= n2   
elif op.lower (mult):
    resultado *= n2
elif op.lower() == "division":  
    resultado /= n2                 
elif op.lower() == "potencia":
    resultado **= n2
else:
    print("operacion no valida")
print(f"resultado {resultado}")
print("adios")

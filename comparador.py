altura = int(input("ingrese la altura de la sisterna: "))
constante = 720
total_agua = 360000
altura = altura * constante
if altura < total_agua:

    agua_faltante =  altura * constante   
    total_agua_actual = total_agua - agua_faltante
    print("agua faltante en  la sisterna es: ",altura ,"Avisar al supervisor del faltante de agua")
elif altura == total_agua:
    print("la sisterna esta llena", total_agua_actual)
else:
    print("la sisterna esta llena")

cloro_residual  = float(input("ingrese resultado del cloro residual: "))
cloro_permisible = 1.5
contante2= 130000
if cloro_residual <= cloro_permisible:  

    cloro_faltante =  cloro_residual -cloro_residual * altura / contante2



    print("necesita agregar cloro", cloro_faltante, "de litros faltantes")

else:
    print("no es necesario agregar cloro")

import math
from math import sqrt
num = int(input("ingrese el numerador: "))
num = 0
exp = int(input("ingrese el exponente: "))
exp  = 0
raiz =int(input("ingrese la raiz: "))    
r = sqrt(raiz)
dem1 = int(input("ingrese el denominador: "))
dem1= 0
dem2 = int(input("ingrese el denominador: "))
dem2= 0
exp_e = int(input("ingrese el exponente: "))
exp_ej  = exp_e * exp_e

solucion =(num ** exp ) * (r) / dem1 - dem2
print("el resultado de la operacion es: ", num, exp, raiz, dem1, dem2, exp_e)
print ("la solucion es: ", solucion)




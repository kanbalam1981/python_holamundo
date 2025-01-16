from math import pi # Importa el módulo math
class Cilindro:

    # Método constructor
    def __init__(self, radio, height, color):
        self.radio= radio
        self.heigth = height
        self.color= color
    
    # self es una referencia a la instancia actual de la clase
    # self se usa para acceder a las variables de la instancia
    # self se usa para acceder a los métodos de la instancia
    # self no es un keyword, puedes usar cualquier nombre en lugar de self
    # pero se recomienda usar self por convención
    # self no es un argumento de la función, no lo pases al llamar al método
    
    
    # Método de instancia
    def perimeter (self):
        return 2 * pi * self.radio
    def area_base(self):
        return pi * self.radio ** 2
    def volumen(self):
        return self.area_base() * self.heigth   
if __name__ == "__main__":
    cilindro1 = Cilindro(3, 5, "azul")
    print(f'El perímetro del cilindro1.{cilindro1.perimeter()}')
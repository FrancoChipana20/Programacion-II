import math

class FigurasGeometricas:
    def __init__(self, valor1, valor2=0):
        self.valor1 = valor1
        self.valor2 = valor2
    def __pow__(self, other): 
        return math.pi * (self.valor1 ** 2)

    def __mul__(self, other): 
        return self.valor1 * self.valor2

    def __truediv__(self, other): 
        return (self.valor1 * self.valor2) / 2

    def __add__(self, other):  
        return ((self.valor1 + other.valor1) / 2) * self.valor2

    def __mod__(self, other):  
        apotema = self.valor2
        perimetro = 5 * self.valor1
        return (perimetro * apotema) / 2

circulo = FigurasGeometricas(7)
print("Área del círculo:", circulo ** None)

rectangulo = FigurasGeometricas(10, 5)
print("Área del rectángulo:", rectangulo * None)

triangulo = FigurasGeometricas(10, 5)
print("Área del triángulo:", triangulo / None)

trapecio = FigurasGeometricas(8, 5)
print("Área del trapecio:", trapecio + FigurasGeometricas(6, 5))

pentagono = FigurasGeometricas(5, 4) 
print("Área del pentágono:", pentagono % None)

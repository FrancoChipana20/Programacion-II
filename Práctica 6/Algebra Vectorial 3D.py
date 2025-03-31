import math

class Vector3D:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def suma(self, v):
        return Vector3D(self.a + v.a, self.b + v.b, self.c + v.c)

    def producto_escalar(self, r):
        return Vector3D(self.a * r, self.b * r, self.c * r)

    def producto_vectorial(self, v):
        return Vector3D(self.b * v.c - self.c * v.b,
                        self.c * v.a - self.a * v.c,
                        self.a * v.b - self.b * v.a)

    def magnitud(self):
        return math.sqrt(self.a**2 + self.b**2 + self.c**2)

    def normalizar(self):
        mag = self.magnitud()
        if mag == 0:
            raise ValueError("No se puede normalizar un vector cero")
        return Vector3D(self.a / mag, self.b / mag, self.c / mag)

    def producto_punto(self, v):
        return self.a * v.a + self.b * v.b + self.c * v.c

    @staticmethod
    def ingresar_vector(nombre):
        a = float(input(f"Ingrese la componente a del vector {nombre}: "))
        b = float(input(f"Ingrese la componente b del vector {nombre}: "))
        c = float(input(f"Ingrese la componente c del vector {nombre}: "))
        return Vector3D(a, b, c)

    def __str__(self):
        return f"({self.a}, {self.b}, {self.c})"


print("Ingrese los datos del vector A:")
a = Vector3D.ingresar_vector("A")
print("Ingrese los datos del vector B:")
b = Vector3D.ingresar_vector("B")

print("Suma:", a.suma(b))
print("Escalar * Vector (r=3):", a.producto_escalar(3))
print("Magnitud de A:", a.magnitud())
print("Normalización de A:", a.normalizar())
print("Producto punto:", a.producto_punto(b))
print("Producto vectorial:", a.producto_vectorial(b))

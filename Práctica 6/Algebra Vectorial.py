import math

class AlgebraVectorial:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, V):
        return AlgebraVectorial(self.x + V.x, self.y + V.y, self.z + V.z)

    def __sub__(self, V):
        return AlgebraVectorial(self.x - V.x, self.y - V.y, self.z - V.z)

    def producto_punto(self, V):
        return self.x * V.x + self.y * V.y + self.z * V.z

    def producto_cruz(self, V):
        return AlgebraVectorial(
            self.y * V.z - self.z * V.y,
            self.z * V.x - self.x * V.z,
            self.x * V.y - self.y * V.x
        )

    def perpendicular(self, V):
        return "SI SON PERPENDICULARES" if(self.producto_punto(V) == 0) else "NO SON PERPENDICULARES"

    def paralela(self, V):
        cruz = self.producto_cruz(V)
        return "SI SON PARALELOS" if (cruz.x == 0 and cruz.y == 0 and cruz.z == 0) else "NO SON PARALELOS"

    def proyeccion(self, V):
        factor = self.producto_punto(V) / V.magnitud()**2
        proyectado = AlgebraVectorial(V.x * factor, V.y * factor, V.z * factor)
        return f"(x: {proyectado.x}, y: {proyectado.y}, z: {proyectado.z})"

    def componente(self, V):
        return self.producto_punto(V) / V.magnitud()

    @staticmethod
    def ingresar_vector(nombre):
        x = float(input(f"Ingrese la componente x del vector {nombre}: "))
        y = float(input(f"Ingrese la componente y del vector {nombre}: "))
        z = float(input(f"Ingrese la componente z del vector {nombre} (opcional, 0 si no aplica): ") or 0)
        return AlgebraVectorial(x, y, z)


print("Ingrese los datos del vector A:")
a = AlgebraVectorial.ingresar_vector("A")
print("Ingrese los datos del vector B:")
b = AlgebraVectorial.ingresar_vector("B")
print("¿Son perpendiculares?:", a.perpendicular(b))
print("¿Son paralelos?:", a.paralela(b))
print("Proyección de A sobre B:", a.proyeccion(b))
print("Componente de A en la dirección de B:", a.componente(b))

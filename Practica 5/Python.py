import math

def get_discriminante(a, b, c):
    return b**2 - 4*a*c

def get_raiz1(a, b, discriminante):
    return (-b + math.sqrt(discriminante)) / (2 * a)

def get_raiz2(a, b, discriminante):
    return (-b - math.sqrt(discriminante)) / (2 * a)

def resolver_ecuacion(a, b, c):
    discriminante = get_discriminante(a, b, c)

    if discriminante > 0:
        r1 = get_raiz1(a, b, discriminante)
        r2 = get_raiz2(a, b, discriminante)
        print(f"La ecuación tiene dos raíces {r1:.5f} y {r2:.5f}")
    elif discriminante == 0:
        r = get_raiz1(a, b, discriminante)
        print(f"La ecuación tiene una raíz {r:.5f}")
    else:
        print("La ecuación no tiene raíces reales")
a, b, c = map(float, input("Ingrese a, b, c: ").split())
resolver_ecuacion(a, b, c)

import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_discriminante(self):
        return self.b**2 - 4*self.a*self.c

    def get_raiz1(self):
        discriminante = self.get_discriminante()
        if discriminante < 0:
            return None
        return (-self.b + math.sqrt(discriminante)) / (2 * self.a)

    def get_raiz2(self):
        discriminante = self.get_discriminante()
        if discriminante < 0:
            return None
        return (-self.b - math.sqrt(discriminante)) / (2 * self.a)

    def mostrar_solucion(self):
        discriminante = self.get_discriminante()
        if discriminante > 0:
            print(f"La ecuación tiene dos raíces {self.get_raiz1():.5f} y {self.get_raiz2():.5f}")
        elif discriminante == 0:
            print(f"La ecuación tiene una raíz {self.get_raiz1():.5f}")
        else:
            print("La ecuación no tiene raíces reales")
a, b, c = map(float, input("Ingrese a, b, c: ").split())

ecuacion = EcuacionCuadratica(a, b, c)
ecuacion.mostrar_solucion()

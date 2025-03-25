import math

def promedio(numeros):
    return sum(numeros) / len(numeros)

def desviacion(numeros, promedio):
    suma_cuadrados = sum((x - promedio) ** 2 for x in numeros)
    return math.sqrt(suma_cuadrados / (len(numeros) - 1))

numeros = list(map(float, input("Ingrese 10 números separados por espacio: ").split()))

if len(numeros) != 10:
    print("Debe ingresar exactamente 10 números.")
else:
    prom = promedio(numeros)
    desv = desviacion(numeros, prom)

    print(f"El promedio es {prom:.2f}")
    print(f"La desviación estándar es {desv:.5f}")

import math

class Estadisticas:
    def _init_(self, numeros):
        self.numeros = numeros

    def promedio(self):
        return sum(self.numeros) / len(self.numeros)

    def desviacion(self):
        prom = self.promedio()
        suma_cuadrados = sum((x - prom) ** 2 for x in self.numeros)
        return math.sqrt(suma_cuadrados / (len(self.numeros) - 1))

    def mostrar_resultados(self):
        print(f"El promedio es {self.promedio():.2f}")
        print(f"La desviación estándar es {self.desviacion():.5f}")

numeros = list(map(float, input("Ingrese 10 números separados por espacio: ").split()))
if len(numeros) != 10:
    print("Debe ingresar exactamente 10 números.")
else:
    estadistica = Estadisticas(numeros)
    estadistica.mostrar_resultados()

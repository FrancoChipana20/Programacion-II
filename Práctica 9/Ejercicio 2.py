import tkinter as tk
from tkinter import ttk
import random
import math
from abc import ABC, abstractmethod

# ----- Calses -----
class Coloreado(ABC):
    @abstractmethod
    def como_colorear(self) -> str:
        pass

class Figura(ABC):
    def __init__(self, color: str):
        self._color = color

    def set_color(self, color: str):
        self._color = color

    def get_color(self) -> str:
        return self._color

    def __str__(self) -> str:
        return f"Color: {self._color}"

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado: float, color: str = "Rojo"):
        super().__init__(color)
        self.lado = lado

    def area(self) -> float:
        return self.lado ** 2

    def perimetro(self) -> float:
        return 4 * self.lado

    def como_colorear(self) -> str:
        return "Colorear los cuatro lados"

class Circulo(Figura):
    def __init__(self, radio: float, color: str = "Azul"):
        super().__init__(color)
        self.radio = radio

    def area(self) -> float:
        return math.pi * self.radio ** 2

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio

# ----- Interfaz Gráfica -----
class App:
    def __init__(self, r):
        self.r = r
        self.r.title("Figuras Aleatorias")
        self.r.geometry("500x400")
        l = tk.Label(r, text="Generador de Figuras", font=("Arial", 16))
        l.pack(pady=10)
        b = tk.Button(r, text="Generar 5 Figuras", command=self.generar_figuras)
        b.pack(pady=5)
        s = tk.Button(r, text="Salir", command=r.destroy)
        s.pack(pady=5)
        self.t = tk.Text(r, height=15, width=60)
        self.t.pack(pady=10)

    def generar_figuras(self):
        self.t.delete("1.0", tk.END)
        v = []
        for _ in range(5):
            t = random.randint(1, 2)
            if t == 1:
                l = round(random.uniform(1.0, 10.0), 2)
                f = Cuadrado(l)
            else:
                r = round(random.uniform(1.0, 10.0), 2)
                f = Circulo(r)
            v.append(f)

        for f in v:
            s = f"Figura: {type(f).__name__}\n"
            s += f"Color: {f.get_color()}\n"
            s += f"Área: {f.area():.2f}\n"
            s += f"Perímetro: {f.perimetro():.2f}\n"
            if isinstance(f, Coloreado):
                s += f"Cómo colorear: {f.como_colorear()}\n"
            s += "-" * 40 + "\n"
            self.t.insert(tk.END, s)

n = tk.Tk()
a = App(n)
n.mainloop()

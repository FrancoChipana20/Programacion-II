import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

# ----- Clases -----
class Boleto(ABC):
    def __init__(self, numero):
        self.numero = numero

    @abstractmethod
    def calcular_precio(self):
        pass

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.calcular_precio()}"

class Palco(Boleto):
    def calcular_precio(self):
        return 100.0

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias = dias_anticipacion

    def calcular_precio(self):
        return 50.0 if self.dias >= 10 else 60.0

class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias = dias_anticipacion

    def calcular_precio(self):
        return 25.0 if self.dias >= 10 else 30.0

# ----- Interfaz gráfica -----
class TeatroApp:
    def __init__(self, root):
        self.r = root
        self.r.title("Punto de ventas")
        self.r.geometry("400x300")

        tk.Label(self.r, text="Punto de ventas", font=("Arial", 18)).pack(pady=5)

        f = tk.Frame(self.r, relief=tk.GROOVE, bd=2, padx=10, pady=10)
        f.pack(padx=10, pady=5, fill="x")

        self.k = tk.StringVar()
        self.k.set("Palco")

        tk.Label(f, text="Datos del Boleto", font=("Arial", 10)).grid(row=0, columnspan=3, pady=5)
        tk.Radiobutton(f, text="Palco", variable=self.k, value="Palco", command=self.actualizar_campos).grid(row=1, column=0)
        tk.Radiobutton(f, text="Platea", variable=self.k, value="Platea", command=self.actualizar_campos).grid(row=1, column=1)
        tk.Radiobutton(f, text="Galeria", variable=self.k, value="Galeria", command=self.actualizar_campos).grid(row=1, column=2)

        tk.Label(f, text="Número:").grid(row=2, column=0, sticky="e", pady=5)
        self.e1 = tk.Entry(f)
        self.e1.grid(row=2, column=1, columnspan=2)

        self.l = tk.Label(f, text="Cant. Días para el Evento:")
        self.l.grid(row=3, column=0, sticky="e", pady=5)
        self.e2 = tk.Entry(f)
        self.e2.grid(row=3, column=1, columnspan=2)

        tk.Button(f, text="Vende", command=self.vender).grid(row=4, column=1, pady=10)
        tk.Button(f, text="Salir", command=self.r.destroy).grid(row=4, column=2, pady=10)

        self.o = tk.Label(self.r, text="", font=("Arial", 12), fg="blue")
        self.o.pack(pady=10)

        self.actualizar_campos()

    def actualizar_campos(self):
        t = self.k.get()
        if t == "Palco":
            self.e2.config(state="disabled")
        else:
            self.e2.config(state="normal")

    def vender(self):
        try:
            n = int(self.e1.get())
            t = self.k.get()

            if t == "Palco":
                b = Palco(n)
            else:
                d = int(self.e2.get())
                if t == "Platea":
                    b = Platea(n, d)
                elif t == "Galeria":
                    b = Galeria(n, d)

            self.o.config(text=str(b))
        except ValueError:
            messagebox.showerror("Error", "Ingrese datos válidos.")


v = tk.Tk()
t = TeatroApp(v)
v.mainloop()

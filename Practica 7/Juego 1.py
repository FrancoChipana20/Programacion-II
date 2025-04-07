import random
class Juego:
    def __init__(self):
        self.numeroDeVidas = 0
        self.record = 0

    def reiniciaPartida(self):
        print("🔄 Reiniciando partida...")
        self.numeroDeVidas = 3

    def actualizaRecord(self):
        print("✅ Actualizando récord...")
        self.record += 1
        print(f"🏆 Récord actual: {self.record}")

    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            print(f"❌ Te quedan {self.numeroDeVidas} vidas.")
            return True
        else:
            print("💀 No te quedan vidas. Fin del juego.")
            return False


class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_vidas):
        super().__init__()
        self.numeroDeVidas = numero_vidas
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroDeVidas = 3
        self.numeroAAdivinar = random.randint(0, 10)
        print("🎮 Bienvenido al juego de adivinar el número (entre 0 y 10)")

        while True:
            try:
                intento = int(input("👉 Ingresa tu número: "))
            except ValueError:
                print("⚠️ Por favor ingresa un número válido.")
                continue

            if intento == self.numeroAAdivinar:
                print("🎉 ¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if not self.quitaVida():
                    print(f"🔚 El número correcto era: {self.numeroAAdivinar}")
                    break
                elif intento < self.numeroAAdivinar:
                    print("📈 El número es mayor. Intenta de nuevo.")
                else:
                    print("📉 El número es menor. Intenta de nuevo.")


class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()

Aplicacion.main()

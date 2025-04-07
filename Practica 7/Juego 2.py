import random

class Juego:
    def __init__(self):
        self.numeroDeVidas = 0
        self.record = 0

    def reiniciaPartida(self):
        print("🔄 Reiniciando partida...")
        self.numeroDeVidas = 3

    def actualizaRecord(self):
        self.record += 1
        print(f"🏆 Récord actualizado: {self.record}")

    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            print(f"❌ Te quedan {self.numeroDeVidas} vidas.")
            return True
        else:
            print("💀 No quedan vidas. Fin del juego.")
            return False


class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__()
        self.numeroDeVidas = vidas
        self.numeroAAdivinar = 0

    def validaNumero(self, n):
        return 0 <= n <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("🎮 Adivina un número entre 0 y 10")

        while True:
            try:
                intento = int(input("👉 Ingresa un número: "))
            except ValueError:
                print("⚠️ Entrada inválida. Intenta con un número entero.")
                continue

            if not self.validaNumero(intento):
                print("⚠️ Número inválido.")
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


class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if 0 <= n <= 10 and n % 2 == 0:
            return True
        print("🚫 El número no es par o está fuera del rango [0, 10].")
        return False


class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if 0 <= n <= 10 and n % 2 != 0:
            return True
        print("🚫 El número no es impar o está fuera del rango [0, 10].")
        return False


class Aplicacion:
    @staticmethod
    def main():
        print("\n🔢 Juego 1: Adivina cualquier número")
        juego_general = JuegoAdivinaNumero(3)
        juego_general.juega()

        print("\n🟦 Juego 2: Adivina número PAR")
        juego_par = JuegoAdivinaPar(3)
        juego_par.juega()

        print("\n🟥 Juego 3: Adivina número IMPAR")
        juego_impar = JuegoAdivinaImpar(3)
        juego_impar.juega()

Aplicacion.main()

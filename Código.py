# --------------------------
# Patrón Creacional: Singleton
# --------------------------
class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance

    def operation(self):
        return "Operación del Singleton"
# --------------------------
# Patrón Estructural: Adapter
# --------------------------
class Adaptee:
    def specific_request(self):
        return "Respuesta específica del Adaptee"

class Target:
    def request(self):
        raise NotImplementedError

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()
# --------------------------
# Patrón de Comportamiento: Observer
# --------------------------
class Observer:
    def update(self, state):
        raise NotImplementedError

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, state):
        print(f"{self.name} ha sido notificado del nuevo estado: {state}")

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, state):
        for observer in self._observers:
            observer.update(state)

class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    def set_state(self, state):
        self._state = state
        self.notify(state)

    def get_state(self):
        return self._state
# --------------------------
# Ejecución
# --------------------------
if __name__ == "__main__":
    print("=== Singleton ===")
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()
    print(s1.operation())
    print(f"¿s1 es s2?: {s1 is s2}")

    print("\n=== Adapter ===")
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print(adapter.request())

    print("\n=== Observer ===")
    subject = ConcreteSubject()
    obs1 = ConcreteObserver("Observador 1")
    obs2 = ConcreteObserver("Observador 2")
    subject.attach(obs1)
    subject.attach(obs2)
    subject.set_state("ACTIVO")

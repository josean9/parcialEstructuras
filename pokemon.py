class pokemon():
    def __init__(self, ID, nombre, arma, salud, ataque, defensa):
        self.ID = ID
        self.nombre = nombre
        self.arma = arma
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        while True:
            try:
                self.ID = int(self.ID)
                break
            except ValueError:
                self.ID = int(input("El ID debe ser un número, por favor, introduzca un número: "))
        while True:
            try:
                self.salud = int(self.salud)
                break
            except ValueError:
                self.salud = int(input("La salud debe ser un número, por favor, introduzca un número: "))
        while True:
            try:
                self.ataque = int(self.ataque)
                break
            except ValueError:
                self.ataque = int(input("El ataque debe ser un número, por favor, introduzca un número: "))
        while True:
            try:
                self.defensa = int(self.defensa)
                break
            except ValueError:
                self.defensa = int(input("La defensa debe ser un número, por favor, introduzca un número: "))
        while True:
            if arma = "Puñetazo":
                self.arma = input("El arma debe ser Puñetazo, Patada, Codazo o Cabezazo, por favor, introduzca una de estas opciones: ")
                continue
            else:
                break
    def __str__(self):
        return "Pokemon ID: "+str(self.ID)+" con nombre: "+self.nombre+" tiene de arma: "+self.arma+" y salud: "+str(self.salud)
pokemon1 = pokemon(1, "Pikachu", "Rayo", 30, 50, 30)
print(pokemon1)
print("hola")
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
                self.defensa = input("La defensa debe ser un número, por favor, introduzca un número: ")
        while True:
            if self.salud>100 or self.salud<0:
                self.salud = input("La salud debe ser un número entre 0 y 10, por favor, introduzca un número: ")
            else:
                break
        while True:
            if self.ataque>10 or self.ataque<0:
                self.ataque = input("El ataque debe ser un número entre 0 y 10, por favor, introduzca un número: ")
            else:
                break
        while True:
            if self.defensa > 10 or self.defensa < 0:
                self.defensa = input("La defensa debe ser un número entre 0 y 10, por favor, introduzca un número: ")
            else:
                break
        while True:
            if self.arma == "Puñetazo" or self.arma == "Patada" or self.arma == "Codazo" or self.arma == "Cabezazo":
                break
            else:
                self.arma = input("El arma debe ser Puñetazo, Patada, Codazo o Cabezazo, por favor, introduzca una de estas opciones: ")
                print("El arma debe ser Puñetazo, Patada, Codazo o Cabezazo, por favor, introduzca una de estas opciones: ")
                continue
    def is_alive(self):
        if self.salud>0:
            return "Esta vivo"
        else:
            return "Esta muerto"
    def fight_defense(self, points_of_damage):
        if self.defensa>points_of_damage:
            return ("No se ha podido atacar, la defensa es mayor que el ataque")
        else:
            self.salud = self.salud - (points_of_damage - self.defensa)
            return ("Se ha podido atacar, la nueva salud del pokemon es{}".format(self.salud))
    def fight_attack(self, pokemon_to_attack):
        pokemon_to_attack.fight_defense(int(self.ataque))
    def __str__(self):
        return "Pokemon ID: "+str(self.ID)+" con nombre: "+self.nombre+" tiene de arma: "+self.arma+" y salud: "+str(self.salud)
pokemon1 = pokemon(1, "Pikachu", "Puñetazo", 76, 6, 3)
pokemon2 = pokemon(2, "Charmander", "Patada", 32, 3, 2)
pokemon3 = pokemon(3, "Bulbasaur", "Codazo", 56, 7, 4)
pokemon4 = pokemon(4, "Squirtle", "Cabezazo", 34, 5, 6)
print(pokemon1)

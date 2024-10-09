class Heroe:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque = 12
        self.defensa = 10
        self.salud = 100
        self.salud_maxima = 100  # Salud máxima
        self.defensa_temporal = self.defensa  # Defensa aumentada temporalmente

    def atacar(self, enemigo):
        print(f"Héroe ataca a {enemigo.nombre}.")
        dano = self.ataque - enemigo.defensa
        if dano > 0:
            enemigo.salud -= dano
            print(f"El enemigo {enemigo.nombre} ha recibido {dano} puntos de daño.")
        else:
            print("El enemigo ha bloqueado el ataque.")

    def curarse(self):
        cantidad_curada = 10  # Cantidad fija de puntos de salud recuperados
        self.salud = min(self.salud_maxima, self.salud + cantidad_curada)
        print(f"Héroe se ha curado. Salud actual: {self.salud}")


    def defenderse(self):
        self.defensa_temporal = self.defensa + 5
        print(f"Héroe se defiende. Defensa aumentada temporalmente a {self.defensa_temporal}.")

    def reset_defensa(self):
        self.defensa_temporal = self.defensa
        print(f"La defensa de {self.nombre} vuelve a la normalidad.")

    def esta_vivo(self):
        return self.salud > 0


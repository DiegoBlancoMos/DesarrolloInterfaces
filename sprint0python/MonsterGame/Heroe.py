class Heroe:
    def __init__(self, nombre, ataque, defensa):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = 100  # Salud actual
        self.salud_maxima = 100  # Salud máxima
        self.defensa_temporal = 0  # Defensa aumentada temporalmente

    def atacar(self, enemigo):
        print(f"Héroe ataca a {enemigo.nombre}.")
        dano = self.ataque - (enemigo.defensa + enemigo.defensa_temporal)
        if dano > 0:
            enemigo.salud -= dano
            print(f"El enemigo {enemigo.nombre} ha recibido {dano} puntos de daño.")
        else:
            print("El enemigo ha bloqueado el ataque.")

    def curarse(self):
        cantidad_curada = 10  # Cantidad fija de puntos de salud recuperados
        self.salud += cantidad_curada
        if self.salud > self.salud_maxima:
            self.salud = self.salud_maxima
        print(f"Héroe se ha curado. Salud actual: {self.salud}")

    def defenderse(self):
        self.defensa_temporal += 5
        print(f"Héroe se defiende. Defensa aumentada temporalmente a {self.defensa + self.defensa_temporal}.")

    def reset_defensa(self):
        self.defensa_temporal = 0
        print(f"La defensa de {self.nombre} vuelve a la normalidad.")

    def esta_vivo(self):
        return self.salud > 0


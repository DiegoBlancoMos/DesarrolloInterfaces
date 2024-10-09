class Heroe:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque = 12 # Ataque del héroe
        self.defensa = 10 # Defensa del héroe
        self.salud = 100 # Salud inicial
        self.salud_maxima = 100  # Salud máxima
        self.defensa_temporal = self.defensa  # Defensa aumentada temporalmente

    def atacar(self, enemigo):
        print(f"Héroe ataca a {enemigo.nombre}.")
        dano = self.ataque - enemigo.defensa #El DAÑO recibido será el ataque del héroe - la defensa del monstruo
        if dano > 0: # Si es mayor que 0, el monstruo recibirá daño, en caso de que no lo sea, no lo recibirá
            enemigo.salud -= dano
            print(f"El enemigo {enemigo.nombre} ha recibido {dano} puntos de daño.")
        else:
            print("El enemigo ha bloqueado el ataque.")

    def curarse(self):
        cantidad_curada = 10  # Cantidad fija de puntos de salud recuperados
        self.salud = min(self.salud_maxima, self.salud + cantidad_curada)# Si la salud+ la salud curada, es mayor que la salud máxima, se cogerá el valor de la salud máxima que es 100
        print(f"Héroe se ha curado. Salud actual: {self.salud}")


    def defenderse(self):
        self.defensa_temporal = self.defensa + 5 #Aumenta la defensa temporal 5
        print(f"Héroe se defiende. Defensa aumentada temporalmente a {self.defensa_temporal}.")

    def reset_defensa(self):
        self.defensa_temporal = self.defensa #Devuelve la defensa a su valor normal
        print(f"La defensa de {self.nombre} vuelve a la normalidad.")

    def esta_vivo(self):
        return self.salud > 0 #Si el enemigo no tiene salud, devolverá false y se termina el juego.


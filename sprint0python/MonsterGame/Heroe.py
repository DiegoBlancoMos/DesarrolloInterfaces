class Heroe:
    def __init__(self,nombre,ataque,defensa):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = 100
        self.salud_maxima = 100
        print(f"El héroe {self.nombre} ha sido creado con {self.ataque} de ataque y {self.defensa} de defensa.")
 def atacar(self, monstruo):
        dano = self.ataque - monstruo.defensa
        dano = dano if dano > 0 else 0# Evitar daño negativo
        if dano <= monstruo.defensa:
            print("El enemigo ha bloqueado el ataque.")
        monstruo.recibir_dano(dano)
        print(f"El héroe {self.nombre} ataca a {monstruo.nombre} causando {dano} puntos de daño.")

    def defenderse(self):
        # Implementar lógica para aumentar defensa temporalmente si se desea
        print(f"El héroe {self.nombre} se prepara para defenderse, aumentando su defensa.")

    def curarse(self, puntos):
        self.salud += puntos
        if self.salud > self.salud_maxima:
            self.salud = self.salud_maxima
        print(f"El héroe {self.nombre} se cura, recuperando {puntos} de salud.")

    def recibir_dano(self, dano):
        self.salud -= dano
        print(f"El héroe {self.nombre} recibe {dano} puntos de daño.")
        if self.salud < 0:
            self.salud = 0

    def esta_vivo(self):
        if self.salud > 0:
            print(f"El héroe {self.nombre} está vivo.")
            return True
        else:
            print(f"El héroe {self.nombre} ha caído en combate.")
            return False
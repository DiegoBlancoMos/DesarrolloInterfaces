class Monstruo :
    def __init__(self,nombre,ataque,defensa,salud):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

    def atacar(self,heroe):
        print(f"Monstruo ataca a {heroe.nombre}.")
        dano = self.ataque - heroe.defensa_temporal
        if dano > 0:
            heroe.salud -= dano
            print(f"El héroe {heroe.nombre} ha recibido {dano} puntos de daño.")
        else:
            print("El héroe ha bloqueado el ataque.")

    def esta_vivo(self):
        return self.salud>0
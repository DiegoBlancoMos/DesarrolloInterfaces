class Monstruo :
    def __init__(self,nombre,ataque,defensa,salud):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

    def atacar(self,heroe):
        print(f"Monstruo ataca a {heroe.nombre}.")
        dano = self.ataque - heroe.defensa_temporal #El DAÑO recibido será el ataque del monstruo - la defensa del héroe
        if dano > 0: # Si es mayor que 0, el héroe recibirá daño, en caso de que no lo sea, no lo recibirá
            heroe.salud -= dano
            print(f"El héroe {heroe.nombre} ha recibido {dano} puntos de daño.")
        else:
            print("El héroe ha bloqueado el ataque.")

    def esta_vivo(self):
        return self.salud>0  #Si el monstruo no tiene salud, devolverá false y se seguirá con el siguiente monstruo/acabará el juego
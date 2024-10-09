import random

from Monstruo import Monstruo
from Tesoro import Tesoro


class Mazmorra:
    def __init__(self, heroe):
        self.heroe = heroe
        self.monstruos = [
            Monstruo("Goblin", 8, 3, 30),
            Monstruo("Orco", 12, 6, 40),
            Monstruo("Dragón", 15, 8, 60)
        ]  # Lista de monstruos en la mazmorra
        self.tesoro = Tesoro()  # Instancia de la clase Tesoro


    def jugar(self):
        print("Héroe entra en la mazmorra.")
        for monstruo in self.monstruos:
            print(f"Te has encontrado con un {monstruo.nombre}.")
            self.enfrentar_enemigo(monstruo)
            if not self.heroe.esta_vivo():
                print("Héroe ha sido derrotado en la mazmorra.")
                return

        print(f"¡{self.heroe.nombre} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")

    def enfrentar_enemigo(self, enemigo):
        while enemigo.esta_vivo() > 0 and self.heroe.esta_vivo():
            print("¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Defender")
            print("3. Curarse")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.heroe.atacar(enemigo)
                if enemigo.salud > 0:
                    enemigo.atacar(self.heroe)  # El enemigo ataca al héroe
            elif opcion == "2":
                self.heroe.defenderse()
                enemigo.atacar(self.heroe)  # El enemigo ataca al héroe
                self.heroe.reset_defensa()  # Restaurar defensa después del turno
            elif opcion == "3":
                self.heroe.curarse()
                enemigo.atacar(self.heroe)  # El enemigo ataca al héroe
            else:
                print("Opción no válida.")

        if enemigo.salud <= 0:
            print(f"Has derrotado a {enemigo.nombre}.")
            self.buscar_tesoro()

    def buscar_tesoro(self):
        print("Buscando tesoro...")
        self.tesoro.encontrar_tesoro(self.heroe)
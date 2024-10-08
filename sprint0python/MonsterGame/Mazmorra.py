import random

from Monstruo import Monstruo
from Tesoro import Tesoro


class Mazmorra:
    def __init__(self, heroe):
        self.heroe = heroe
        self.monstruos = []  # Lista de monstruos en la mazmorra
        self.tesoro = Tesoro()  # Instancia de la clase Tesoro
        self.crear_monstruos()

    def crear_monstruos(self):
        # Crear algunos monstruos (puedes ajustar los nombres y atributos)
        self.monstruos.append(Monstruo("Orco", ataque=15, defensa=5))
        self.monstruos.append(Monstruo("Esqueleto", ataque=10, defensa=3))
        self.monstruos.append(Monstruo("Dragón", ataque=20, defensa=10))

    def jugar(self):
        print("Héroe entra en la mazmorra.")
        while self.monstruos and self.heroe.esta_vivo():
            enemigo = self.monstruos.pop(0)  # Sacar el primer monstruo de la lista
            print(f"Te has encontrado con un {enemigo.nombre}.")
            self.enfrentar_enemigo(enemigo)

        if self.heroe.esta_vivo():
            print(f"¡{self.heroe.nombre} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")
        else:
            print("Héroe ha sido derrotado en la mazmorra.")

    def enfrentar_enemigo(self, enemigo):
        while enemigo.salud > 0 and self.heroe.esta_vivo():
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
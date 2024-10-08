from Heroe import Heroe
from Mazmorra import Mazmorra


def main():
    nombre_heroe = input("Nombre del Héroe?")
    heroe = Heroe(nombre_heroe)

    mazmorra = Mazmorra(heroe)
    mazmorra.jugar()
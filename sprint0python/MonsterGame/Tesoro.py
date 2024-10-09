import random

class Tesoro:
    def __init__(self):
        self.beneficios =[ #Lista con los posibles beneficios que se pueden obtener al encontrar un tesoro
            "aumento de ataque",
            "aumento de defensa",
            "restauración de salud"
        ]

    def encontrar_tesoro(self,heroe):
        beneficio = random.choice(self.beneficios) # El random.choice, elegirá un beneficio random de los indicados anteriormente
        print(f"Héroe ha encontrado un tesoro: {beneficio}.")

        #Dependiendo cual sea el beneficio obtenido, mejorará una u otra cosa

        if beneficio == "aumento de ataque":
            incremento = 5  # Cantidad de aumento ataque
            heroe.ataque += incremento
            print(f"El ataque de {heroe.nombre} aumenta a {heroe.ataque}.")

        elif beneficio == "aumento de defensa":
            incremento = 5  # Cantidad de aumento de defensa
            heroe.defensa += incremento
            print(f"La defensa de {heroe.nombre} aumenta a {heroe.defensa}.")

        elif beneficio == "restauración de salud":
            heroe.salud = heroe.salud_maxima  # Restaurar salud a la máxima
            print(f"La salud de {heroe.nombre} ha sido restaurada a {heroe.salud_maxima}.")


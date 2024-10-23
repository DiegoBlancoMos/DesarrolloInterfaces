import tkinter as tk
from tkinter import messagebox
import random


class JuegoPiedraPapelTijeras:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel, Tijera")

        self.puntos_jugador1 = 0
        self.puntos_jugador2 = 0

        self.menu_principal()
        self.center_window()

    def menu_principal(self):
        self.limpiar_ventana()

        tk.Label(self.root, text="Selecciona una opción:").pack(pady=10)
        tk.Button(self.root, text="Jugar contra la Máquina", command=self.jugar_con_maquina).pack(pady=5)
        tk.Button(self.root, text="Dos Jugadores", command=self.jugar_dos_jugadores).pack(pady=5)
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=5)

    def jugar_con_maquina(self):
        self.limpiar_ventana()
        self.puntos_jugador1 = 0
        self.puntos_jugador2 = 0
        self.juego_maquina()

    def jugar_dos_jugadores(self):
        self.limpiar_ventana()
        self.puntos_jugador1 = 0
        self.puntos_jugador2 = 0
        self.juego_dos_jugadores()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def juego_maquina(self):
        if self.puntos_jugador1 < 3 and self.puntos_jugador2 < 3:
            self.pedir_jugada("Jugador 1", "Jugador 2 (Máquina)", self.jugada_maquina)
        else:
            self.declarar_ganador()

    def juego_dos_jugadores(self):
        if self.puntos_jugador1 < 3 and self.puntos_jugador2 < 3:
            self.pedir_jugada("Jugador 1", "Jugador 2", self.jugada_dos_jugadores)
        else:
            self.declarar_ganador()

    def pedir_jugada(self, jugador1, jugador2, callback):
        tk.Label(self.root, text=f"{jugador1}, elige:").pack(pady=10)
        self.boton_piedra = tk.Button(self.root, text="Piedra", command=lambda: callback("Piedra"))
        self.boton_papel = tk.Button(self.root, text="Papel", command=lambda: callback("Papel"))
        self.boton_tijeras = tk.Button(self.root, text="Tijeras", command=lambda: callback("Tijeras"))

        self.boton_piedra.pack(side=tk.LEFT, padx=5)
        self.boton_papel.pack(side=tk.LEFT, padx=5)
        self.boton_tijeras.pack(side=tk.LEFT, padx=5)

    def jugada_maquina(self, jugada_jugador1):
        jugadas = ["Piedra", "Papel", "Tijeras"]
        jugada_jugador2 = random.choice(jugadas)
        self.mostrar_resultado(jugada_jugador1, jugada_jugador2, 1)

    def jugada_dos_jugadores(self, jugada_jugador1):
        self.limpiar_ventana()
        tk.Label(self.root, text="Jugador 2, elige:").pack(pady=10)
        self.boton_piedra2 = tk.Button(self.root, text="Piedra",
                                       command=lambda: self.mostrar_resultado(jugada_jugador1, "Piedra", 2))
        self.boton_papel2 = tk.Button(self.root, text="Papel",
                                      command=lambda: self.mostrar_resultado(jugada_jugador1, "Papel", 2))
        self.boton_tijeras2 = tk.Button(self.root, text="Tijeras",
                                        command=lambda: self.mostrar_resultado(jugada_jugador1, "Tijeras", 2))

        self.boton_piedra2.pack(side=tk.LEFT, padx=5)
        self.boton_papel2.pack(side=tk.LEFT, padx=5)
        self.boton_tijeras2.pack(side=tk.LEFT, padx=5)

    def mostrar_resultado(self, jugada_jugador1, jugada_jugador2, jugador):
        resultado = ""
        if jugada_jugador1 == jugada_jugador2: #DECIDIR EL RESULTADO DEPENDIENDO DE LO ELEGIDO
            resultado = "Empate"
        elif (jugada_jugador1 == "Piedra" and jugada_jugador2 == "Tijeras") or \
                (jugada_jugador1 == "Papel" and jugada_jugador2 == "Piedra") or \
                (jugada_jugador1 == "Tijeras" and jugada_jugador2 == "Papel"):
            resultado = "Gana Jugador 1"
            self.puntos_jugador1 += 1
        else:
            resultado = "Gana Jugador 2"
            self.puntos_jugador2 += 1

        mensaje = (f"El jugador uno saca {jugada_jugador1}, el jugador dos saca {jugada_jugador2}. {resultado}."
                   f"           Puntos J1: {self.puntos_jugador1} || Puntos J2: {self.puntos_jugador2}")
        messagebox.showinfo("Resultado", mensaje)

        self.limpiar_ventana()  # Limpiar la ventana antes de la siguiente jugada

        if self.puntos_jugador1 < 3 and self.puntos_jugador2 < 3:
            if jugador == 1:
                self.juego_maquina()  # Si es contra la máquina, solicita la jugada de nuevo
            else:
                self.juego_dos_jugadores()  # Si es entre dos jugadores, solicita la jugada de nuevo
        else:
            self.declarar_ganador()  # Si alguien llega a 3 puntos, declarar ganador

    def declarar_ganador(self):
        if self.puntos_jugador1 > self.puntos_jugador2:
            gandor = "Jugador 1"
        else:
            ganador = "Jugador 2"
        messagebox.showinfo("Fin del Juego", f"{ganador} gana la partida.")
        self.menu_principal()

    def center_window(self):
        #Obtiene el tamaño de los widgets
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        # Obtiene el tamaño de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcula la posición centrada
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        # Establece la posición de la ventana
        self.root.geometry(f"+{x}+{y}")


if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoPiedraPapelTijeras(root)
    root.mainloop()

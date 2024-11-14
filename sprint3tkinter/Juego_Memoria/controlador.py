# controlador.py

import tkinter as tk
from tkinter import simpledialog, messagebox
from vista import MainMenu


class GameController:
    def __init__(self, root):
        self.root = root
        self.player_name = ""
        self.difficulty = ""

        # Inicializa el menú principal y pasa los callbacks para cada botón
        self.main_menu = MainMenu(root, self.start_game_callback, self.show_stats_callback, self.quit_callback)

    def start_game_callback(self):
        """Llama a la función que solicita la dificultad y el nombre del jugador"""
        self.show_difficulty_selection()

    def show_difficulty_selection(self):
        """Solicita al jugador la dificultad y luego su nombre"""
        # Solicitar la dificultad
        difficulty = simpledialog.askstring(
            "Seleccionar Dificultad",
            "Elige una dificultad (facil, medio, dificil):",
            parent=self.root
        ).lower()

        # Validar la dificultad
        while difficulty not in ['facil', 'medio', 'dificil']:
            difficulty = simpledialog.askstring(
                "Seleccionar Dificultad",
                "Por favor, elige una opción válida (facil, medio, dificil):",
                parent=self.root
            ).lower()

        self.difficulty = difficulty

        # Solicitar el nombre del jugador
        self.ask_player_name()

    def ask_player_name(self):
        """Solicitar al jugador su nombre"""
        player_name = simpledialog.askstring(
            "Nombre del Jugador",
            "Ingresa tu nombre:",
            parent=self.root
        )

        if player_name:
            self.player_name = player_name
            # Muestra la información en la consola (o en un label si lo prefieres en la vista)
            print(f"Nombre del jugador: {self.player_name}")
            print(f"Dificultad seleccionada: {self.difficulty}")
            messagebox.showinfo("Inicio del juego",
                                f"¡Bienvenido {self.player_name}! Has seleccionado la dificultad {self.difficulty}.")
        else:
            print("No se ha ingresado un nombre válido.")
            messagebox.showwarning("Error", "Debes ingresar un nombre válido para continuar.")

    def show_stats_callback(self):
        # Para pruebas iniciales, muestra un mensaje indicando que se ha pulsado "Estadísticas"
        messagebox.showinfo("Estadísticas", "Mostrando estadísticas...")

    def quit_callback(self):
        # Cierra la aplicación al pulsar "Salir"
        self.root.quit()
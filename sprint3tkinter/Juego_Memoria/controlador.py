# controlador.py

import tkinter as tk
from tkinter import messagebox
from vista import MainMenu


class GameController:
    def __init__(self, root):
        self.root = root

        # Inicializa el menú principal y pasa los callbacks para cada botón
        self.main_menu = MainMenu(root, self.start_game_callback, self.show_stats_callback, self.quit_callback)

    def start_game_callback(self):
        # Para pruebas iniciales, muestra un mensaje indicando que se ha pulsado "Jugar"
        messagebox.showinfo("Jugar", "¡Iniciar el juego!")

    def show_stats_callback(self):
        # Para pruebas iniciales, muestra un mensaje indicando que se ha pulsado "Estadísticas"
        messagebox.showinfo("Estadísticas", "Mostrando estadísticas...")

    def quit_callback(self):
        # Cierra la aplicación al pulsar "Salir"
        self.root.quit()

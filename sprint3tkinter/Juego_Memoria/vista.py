import tkinter as tk
from tkinter import simpledialog, messagebox
from controlador import GameController

class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        # Guarda la referencia a la ventana principal
        self.root = root
        self.game_controller = GameController(root)
        # Configuración de la ventana de menú
        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack(pady=100)

        # Botón "Jugar"
        self.start_button = tk.Button(self.menu_frame, text="Jugar", command=start_game_callback, width=15, height=2)
        self.start_button.pack(pady=5)

        # Botón "Estadísticas"
        self.stats_button = tk.Button(self.menu_frame, text="Estadísticas", command=show_stats_callback, width=15,height=2)
        self.stats_button.pack(pady=5)

        # Botón "Salir"
        self.quit_button = tk.Button(self.menu_frame, text="Salir", command=quit_callback, width=15, height=2)
        self.quit_button.pack(pady=5)

    def ask_player_name(self):
            """Solicita el nombre del jugador"""
            player_name = simpledialog.askstring("Nombre del jugador", "Ingrese su nombre:")

            if player_name:
                self.player_name = player_name
                self.game_controller.start_game_callback()  # Comienza el juego
            else:
                messagebox.showerror("Error", "El nombre del jugador no puede estar vacío.")

# vista.py

class GameView:
    def __init__(self, root, rows, cols, card_images):
            self.root = root  # Referencia a la ventana principal
            self.rows = rows  # Número de filas
            self.cols = cols  # Número de columnas
            self.card_images = card_images  # Recibe las imágenes descargadas
            self.buttons = []  # Para almacenar los botones del tablero

    def create_board(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(pady=20)

        # Lista de cartas que se deben mostrar (debe ser igual al tamaño del tablero)
        num_cards = self.rows * self.cols
        image_keys = list(self.card_images.keys())  # Lista de URLs de las imágenes

        # Si no hay suficientes imágenes, repetimos las imágenes
        while len(image_keys) < num_cards:
            image_keys += image_keys

        # Distribuir las cartas en el tablero
        for i in range(num_cards):
            # Crear un botón para cada carta
            img = self.card_images[image_keys[i]]  # Obtener la imagen
            button = tk.Button(self.board_frame, text="Carta", width=10, height=4, image=img)
            button.grid(row=i // self.cols, column=i % self.cols)  # Distribuir en filas y columnas
            self.buttons.append(button)
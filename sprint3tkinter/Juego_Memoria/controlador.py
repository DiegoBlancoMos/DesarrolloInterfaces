# controlador.py
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog
from vista import MainMenu, GameView
from modelo import GameModel


class GameController:
    def __init__(self, root):
        self.root = root
        self.images_are_loaded = False
        self.difficulty = None  # Guardar la dificultad seleccionada
        self.player_name = None  # Nombre del jugador

        self.game_model = GameModel(self.on_images_loaded)
        # Inicializa el menú principal y pasa los callbacks para cada botón
        self.main_menu = MainMenu(root, self.start_game_callback, self.show_stats_callback, self.quit_callback)

    def show_difficulty_selection(self):
        """Muestra el cuadro de selección de dificultad"""
        difficulty = simpledialog.askstring("Selección de dificultad", "Elija dificultad (facil, medio, dificil):")

        if difficulty not in ["facil", "medio", "dificil"]:
            messagebox.showerror("Error", "Dificultad no válida. Elija entre 'facil', 'medio' o 'dificil'.")
            return

        self.difficulty = difficulty  # Guardamos la dificultad seleccionada
        self.ask_player_name()  # Llamamos al siguiente paso para pedir el nombre del jugador

    def ask_player_name(self):
        """Solicita el nombre del jugador"""
        player_name = simpledialog.askstring("Nombre del jugador", "Ingrese su nombre:")

        if player_name:
            self.player_name = player_name
            self.start_game_callback()  # Comienza el juego
        else:
            messagebox.showerror("Error", "El nombre del jugador no puede estar vacío.")

    def start_game_callback(self):
        """Acción para iniciar el juego"""
        if not self.difficulty:
            self.show_difficulty_selection()  # Si no se seleccionó dificultad, solicitamos la dificultad primero.
            return

        # Muestra la ventana de carga
        self.show_loading_window()

        # Crea un hilo para descargar las imágenes
        thread = threading.Thread(target=self.download_images)
        thread.start()

    def show_loading_window(self):
        """Mostrar la ventana de carga"""
        self.loading_window = tk.Toplevel(self.root)
        self.loading_window.title("Cargando...")
        self.loading_window.geometry("200x100")
        self.loading_label = tk.Label(self.loading_window, text="Cargando imágenes...", font=("Arial", 12))
        self.loading_label.pack(pady=20)

    def download_images(self):
        """Este método descarga las imágenes de las cartas de forma asíncrona."""
        print("Descargando imágenes...")

        # Creamos una instancia de GameModel para cargar las imágenes
        game_model = GameModel(self.on_images_loaded)
        game_model._load_images()  # Esto descargará las imágenes de forma asíncrona


    def on_images_loaded(self):
        """Este método se ejecuta después de la descarga de imágenes"""
        # Cerrar la ventana de carga
        self.loading_window.destroy()
        print("Imagenes descargadas...")

        # Crear el tablero de juego según la dificultad
        self.root.after(0, self.create_board)

    def create_board(self):
        """Crea el tablero dependiendo de la dificultad seleccionada"""
        # Determinar el tamaño del tablero basado en la dificultad
        if self.difficulty == "facil":
            rows, cols = 4, 4  # Tablero 4x4
        elif self.difficulty == "medio":
            rows, cols = 6, 6  # Tablero 6x6
        else:
            rows, cols = 8, 8  # Tablero 8x8

        # Crea el tablero con el tamaño correspondiente
        game_view = GameView(self.root, rows, cols,self.game_model.card_images)  # Le pasamos las filas y columnas según la dificultad
        game_view.create_board()  # Método que genera las cartas en la vista

    def show_stats_callback(self):
        messagebox.showinfo("Estadísticas", "Mostrando estadísticas...")

    def quit_callback(self):
        self.root.quit()

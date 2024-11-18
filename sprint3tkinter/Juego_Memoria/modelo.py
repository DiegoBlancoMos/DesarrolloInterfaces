import random
import threading
from tkinter import messagebox
from recursos import descargar_imagen


class GameModel:
    def __init__(self, controller_callback=None):
        self.board = []  # El tablero de juego
        self.card_images = {}  # Diccionario para las imágenes de las cartas
        self.images_loaded = False  # Flag para saber si las imágenes están cargadas
        self.controller_callback = controller_callback  # Callback para notificar al controlador

    def _generate_board(self, difficulty):
        """Genera el tablero con cartas aleatorias basadas en la dificultad."""
        if difficulty == "facil":
            num_pairs = 4
        elif difficulty == "medio":
            num_pairs = 6
        else:  # dificil
            num_pairs = 8

        # Lista de cartas numeradas de 1 a num_pairs
        self.board = [i for i in range(1, num_pairs + 1)] * 2  # Se repiten para formar las parejas
        random.shuffle(self.board)  # Barajamos las cartas

    def _load_images(self):
        """Descargar las imágenes de las cartas y la carta oculta."""
        self.card_images = {}
        image_urls = [
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/2C%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/2D%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/2H%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/2S%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/3C%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/3D%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/3H%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/3S%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/4C%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/4D%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/4H%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/4S%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/5C%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/5D%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/5H%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/5S%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/6C%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/6D%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/6H%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/6S%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/7C%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/7D%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/7H%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/7S%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/8C%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/8D%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/8H%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/8S%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/8C%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/8D%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/8H%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/face/8S%401x.png",
            "https://raw.githubusercontent.com/Xadeck/xCards/refs/heads/master/png/back/bicycle_blue%401x.png"
        ]

        def download_images():
            """Descargar todas las imágenes de manera asíncrona."""
            for url in image_urls:
                img = descargar_imagen(url)
                if img:
                    self.card_images[url] = img
                else:
                    messagebox.showerror("Error", "No se pudo descargar la imagen.")
                    return

            self.images_loaded = True  # Establecemos que las imágenes están cargadas

            # Notificar al controlador para que lo sepa
            if self.controller_callback:
                self.controller_callback()  # Notificar al controlador que las imágenes se descargaron

        # Ejecutamos la descarga en un hilo para no bloquear la interfaz
        threading.Thread(target=download_images).start()

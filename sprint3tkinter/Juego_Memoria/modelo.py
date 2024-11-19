import datetime
import threading
import random
from threading import Event

from PIL import Image, ImageTk

import recursos
from recursos import descargar_imagen


class GameModel:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = []
        self.timer_started = False  # Controla si el temporizador ya ha comenzado
        self.time_elapsed = 0  # El tiempo transcurrido en segundos
        self.hidden_image = None
        self.images = {}
        self.images_loaded = Event()  # Usamos un Event para indicar cuando las imágenes están listas
        self.generate_board()

    def generate_board(self):
        # Definir el número de pares de cartas según la dificultad
        if self.difficulty == "facil":
            rows, cols = 4, 4  # 4x4
            num_pares = 8  # 8 pares de cartas
        elif self.difficulty == "medio":
            rows, cols = 6, 6  # 6x6
            num_pares = 18  # 18 pares de cartas
        elif self.difficulty == "dificil":
            rows, cols = 8, 8  # 8x8
            num_pares = 32  # 32 pares de cartas

        # Generar los valores de las cartas (pares de 1 a num_pares)
        cartas = list(range(1, num_pares + 1)) * 2  # Duplicar para formar los pares
        random.shuffle(cartas)  # Mezclar las cartas

        # Crear el tablero, dividiendo las cartas en filas y columnas según las dimensiones
        self.board = [cartas[i:i + cols] for i in range(0, len(cartas), cols)]
        print(f"Tablero generado con dificultad: {self.difficulty}")
        print(f"Estructura del tablero: {self.board}")

    def load_images(self):
        url_base = "https://raw.githubusercontent.com/DiegoBlancoMos/DesarrolloInterfaces/refs/heads/main/sprint3tkinter/img/"
        def load_images_thread():

            # Descargar la imagen oculta
            self.hidden_image = descargar_imagen(url_base + "oculta.png", (45, 45))
            '''           # Descargar cada imagen única
                       for image_id in range(32):
                           image_url = url_base + "img" + str(image_id) + ".png"
                           self.images[image_id] = descargar_imagen(image_url, (45, 45))'''
            # Carga imágenes para cada identificador de carta en el tablero
            unique_ids = set(id for row in self.board for id in row)  # Identificadores únicos de cartas
            for image_id in unique_ids:
                image_url = f"{url_base}img{image_id-1}.png"
                self.images[image_id] = recursos.descargar_imagen(image_url, (45, 45))
            # Marcar que las imágenes se han cargado
            self.images_loaded.set()

        # Iniciar el hilo para cargar las imágenes
        threading.Thread(target=load_images_thread, daemon=True).start()
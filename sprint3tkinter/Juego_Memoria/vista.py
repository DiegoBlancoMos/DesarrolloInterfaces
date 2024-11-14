import tkinter as tk


# vista.py

import tkinter as tk

class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        # Guarda la referencia a la ventana principal
        self.root = root

        # Configuración de la ventana de menú
        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack(pady=100)

        # Botón "Jugar"
        self.start_button = tk.Button(self.menu_frame, text="Jugar", command=start_game_callback, width=15, height=2)
        self.start_button.pack(pady=5)

        # Botón "Estadísticas"
        self.stats_button = tk.Button(self.menu_frame, text="Estadísticas", command=show_stats_callback, width=15,
                                      height=2)
        self.stats_button.pack(pady=5)

        # Botón "Salir"
        self.quit_button = tk.Button(self.menu_frame, text="Salir", command=quit_callback, width=15, height=2)
        self.quit_button.pack(pady=5)

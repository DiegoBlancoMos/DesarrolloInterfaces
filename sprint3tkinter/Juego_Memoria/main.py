# main.py

import tkinter as tk
from controlador import GameController


def main():
    root = tk.Tk()
    root.title("Juego de Memoria")
    root.geometry("400x400")

    # Crea una instancia del controlador principal
    game_controller = GameController(root)

    # Inicia el bucle principal de Tkinter
    root.mainloop()


if __name__ == "__main__":
    main()

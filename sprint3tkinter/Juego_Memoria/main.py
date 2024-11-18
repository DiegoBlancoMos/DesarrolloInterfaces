import tkinter as tk
from vista import MainMenu
from controlador import GameController


def main():
    root = tk.Tk()
    root.title("Juego de Memoria")
    root.geometry("300x300")

    vista = MainMenu(root)
    # Crea una instancia del controlador principal
    game_controller = GameController(root, vista)

    # Inicia el bucle principal de Tkinter
    root.mainloop()


if __name__ == "__main__":
    main()
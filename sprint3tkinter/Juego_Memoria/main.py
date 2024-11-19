import tkinter as tk
from vista import MainMenu
from controlador import GameController


def main():
    root = tk.Tk()
    root.title("Juego de Memoria")
    root.geometry("300x300")

    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    root.geometry(f'{width}x{height}+{x}+{y}')

    vista = MainMenu(root)
    # Crea una instancia del controlador principal
    game_controller = GameController(root, vista)

    # Inicia el bucle principal de Tkinter
    root.mainloop()


if __name__ == "__main__":
    main()
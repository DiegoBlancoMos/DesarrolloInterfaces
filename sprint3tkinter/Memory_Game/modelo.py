import tkinter as tk
from controlador import GameController  # Controlador principal del juego
from modelo import GameModel  # Modelo de datos del juego

if __name__ == "__main__":
    # Variables y componentes principales
    root = tk.Tk()  # Instancia de Tkinter para la ventana principal de la aplicación
    root.title("Juego de Ejemplo")  # Título de la ventana principal
    root.geometry("800x600")  # Tamaño inicial de la ventana

    # Inicialización del modelo de datos del juego
    model = GameModel(dificultad="Normal",nombre_jugador="Jugador1")  # Modelo con valores predeterminados de dificultad y nombre

    # Inicialización del controlador principal
    controller = GameController(root, model)  # Controlador enlazado con la ventana principal y el modelo

    # Inicio del bucle principal de eventos de Tkinter
    root.mainloop()



import tkinter as tk

from ControladorNotas import ControladorNotas
from NotasModel import NotasModel
from VistaNotas import VistaNotas

if __name__ == "__main__":
    root = tk.Tk()
    modelo = NotasModel()
    vista = VistaNotas(root, None)
    controlador = ControladorNotas(vista, modelo)
    vista.controlador = controlador  # Enlaza el controlador a la vista
    root.mainloop()

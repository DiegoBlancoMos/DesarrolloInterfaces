import tkinter as tk
class ControladorNotas:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        self.vista.actualizar_listbox(self.modelo.obtener_notas())

    def agregar_nota(self):
        nueva_nota = self.vista.entry.get()
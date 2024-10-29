import threading
import tkinter as tk
from tkinter import messagebox


class ControladorNotas:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        self.vista.boton_agregar.config(command=self.agregar_nota)
        self.vista.boton_eliminar.config(command=self.eliminar_nota)
        self.vista.boton_guardar.config(command=self.guardar_notas)
        self.vista.boton_cargar.config(command=self.cargar_notas)
        self.vista.boton_descargar_imagen.config(command=self.descargar_imagen)
        self.vista.listbox.bind("<Button-1>", self.actualizar_coordenadas)
        self.vista.actualizar_listbox(self.modelo.obtener_notas())

    def agregar_nota(self):
        nueva_nota = self.vista.entry.get()

        if nueva_nota:
            # Llamar al método agregar_nota() del modelo
            self.modelo.agregar_nota(nueva_nota)
            # Limpiar el Entry después de agregar la nota
            self.vista.entry_nota.delete(0, 'end')
            # Actualizar el Listbox
            self.actualizar_listbox()

    def eliminar_nota(self):
        # Obtener el índice seleccionado del Listbox
        indice_seleccionado = self.vista.listbox.curselection()

        # Verificar que haya un índice seleccionado
        if indice_seleccionado:
            # Obtener el índice como un entero
            indice = indice_seleccionado[0]

            # Llamar al método eliminar_nota() del modelo
            self.modelo.eliminar_nota(indice)

            # Actualizar el Listbox
            self.actualizar_listbox()

    def actualizar_listbox(self):
        self.vista.listbox.delete(0, tk.END)

        # Obtener las notas actuales desde el modelo
        notas = self.modelo.obtener_notas()

        # Insertar cada nota en el Listbox
        for nota in notas:
            self.vista.listbox.insert(tk.END, nota)

    def guardar_notas(self):
        self.modelo.guardar_notas()
        messagebox.showinfo("Confirmación", "Las notas se han guardado correctamente.")

    def cargar_notas(self):
        self.modelo.cargar_notas()
        self.actualizar_listbox()

    def actualizar_coordenadas(self, event):
        # Capturar las coordenadas del clic
        x, y = event.x, event.y

        # Actualizar el Label de coordenadas
        self.vista.label_coordenadas.config(text=f"Coordenadas: {x}, {y}")


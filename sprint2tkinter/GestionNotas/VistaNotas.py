import tkinter as tk


class VistaNotas:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Aplicación de Notas")

        self.root.geometry("400x500")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # Calcula la posición centrada
        x = (screen_width // 2) - (400 // 2)
        y = (screen_height // 2) - (500 // 2)
        # Establece la posición de la ventana
        self.root.geometry(f"+{x}+{y}")


        # Widget Label para mostrar el título de la aplicación
        self.label_titulo = tk.Label(root, text="Mis Notas")
        self.label_titulo.pack(pady=10)

        # Listbox para mostrar las notas agregadas
        self.listbox_notas = tk.Listbox(root, height=10, width=50)
        self.listbox_notas.pack(pady=10)

        # Campo de texto para ingresar nuevas notas
        self.entry_nota = tk.Entry(root, width=40)
        self.entry_nota.pack(pady=5)

        #Botones para agregar/eliminar/guardar/cargar notas
        self.boton_agregar = tk.Button(text="Agregar Nota").pack(pady=5)
        self.boton_eliminar = tk.Button(text="Eliminar Nota").pack(pady=5)
        self.boton_guardar = tk.Button(text="Guardar Notas").pack(pady=5)
        self.boton_cargar = tk.Button(text="Cargar Notas").pack(pady=5)
        self.boton_descargar_img = tk.Button(text="Descargar Imagen").pack(pady=5)


        self.label_coordenadas = tk.Label(root, text="Coordenadas(0,0)").pack(pady=5)

        self.root.bind("<Button-1>", self.capturar_click)

        self.label_imagen = tk.Label(root)
        self.label_imagen.pack(pady=10)

    def capturar_click(self, event):
        # Captura las coordenadas del clic solo fuera de los botones
        widget = event.widget
        if widget not in [self.boton_agregar, self.boton_eliminar, self.boton_guardar, self.boton_cargar, self.boton_descargar_img]:
            coordenadas = f"Coordenadas: ({event.x}, {event.y})"
            self.label_coordenadas.config(text=coordenadas)

if __name__ == "__main__":
    root = tk.Tk()
    vista = VistaNotas(root)
    root.mainloop()

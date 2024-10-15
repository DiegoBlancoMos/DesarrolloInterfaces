import tkinter as tk
from tkinter import messagebox

def abrir_archivo():
    # Función para manejar la opción "Abrir"
    messagebox.showinfo("Abrir", "Función 'Abrir' no implementada.")

def salir():
    # Función para cerrar la ventana
    root.quit()

def acerca_de():
    # Función para mostrar información sobre la aplicación
    messagebox.showinfo("Acerca de", "Esta es una aplicación de ejemplo.")

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación con Menú")

# Crear la barra de menú
menu_barra = tk.Menu(root)

# Menú Archivo
menu_archivo = tk.Menu(menu_barra, tearoff=0)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
menu_barra.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Ayuda
menu_ayuda = tk.Menu(menu_barra, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)
menu_barra.add_cascade(label="Ayuda", menu=menu_ayuda)

# Configurar la barra de menú en la ventana
root.config(menu=menu_barra)

# Iniciar el bucle principal de la interfaz
root.mainloop()

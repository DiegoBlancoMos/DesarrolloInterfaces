import tkinter as tk

def actualizar_etiqueta(valor):
    etiqueta.config(text=f"Valor seleccionado: {valor}")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 11")

# Crear una barra deslizante (Scale)
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=actualizar_etiqueta)
scale.pack(pady=20)

# Crear una etiqueta para mostrar el valor seleccionado
etiqueta = tk.Label(root, text="Valor seleccionado: 0")
etiqueta.pack(pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()

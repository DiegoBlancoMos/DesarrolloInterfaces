import tkinter as tk

def dibujar_formas():
    # Obtener las coordenadas y el tamaño del círculo y el rectángulo
    try:
        x_circulo = int(entry_x_circulo.get())
        y_circulo = int(entry_y_circulo.get())
        radio = int(entry_radio.get())

        x_rectangulo = int(entry_x_rectangulo.get())
        y_rectangulo = int(entry_y_rectangulo.get())
        ancho = int(entry_ancho.get())
        alto = int(entry_alto.get())

        # Dibujar el círculo
        canvas.create_oval(x_circulo - radio, y_circulo - radio,
                           x_circulo + radio, y_circulo + radio,
                           outline="blue", fill="lightblue")

        # Dibujar el rectángulo
        canvas.create_rectangle(x_rectangulo, y_rectangulo,
                                x_rectangulo + ancho, y_rectangulo + alto,
                                outline="red", fill="lightcoral")
    except ValueError:
        print("Por favor, ingresa valores válidos.")


# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 7")

# Crear un Canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Campos de entrada para el círculo
tk.Label(root, text="Círculo (x, y, radio):").pack()
entry_x_circulo = tk.Entry(root)
entry_x_circulo.pack()
entry_y_circulo = tk.Entry(root)
entry_y_circulo.pack()
entry_radio = tk.Entry(root)
entry_radio.pack()

# Campos de entrada para el rectángulo
tk.Label(root, text="Rectángulo (x, y, ancho, alto):").pack()
entry_x_rectangulo = tk.Entry(root)
entry_x_rectangulo.pack()
entry_y_rectangulo = tk.Entry(root)
entry_y_rectangulo.pack()
entry_ancho = tk.Entry(root)
entry_ancho.pack()
entry_alto = tk.Entry(root)
entry_alto.pack()

# Botón para dibujar
boton_dibujar = tk.Button(root, text="Dibujar", command=dibujar_formas)
boton_dibujar.pack()

# Iniciar el bucle principal de la interfaz
root.mainloop()

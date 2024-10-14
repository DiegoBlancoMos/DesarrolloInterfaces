import tkinter as tk

def actualizar_fondo():
    color_seleccionado = var_color.get()

    if color_seleccionado == "Rojo":
        root.config(bg="red")
    elif color_seleccionado == "Verde":
        root.config(bg="green")
    elif color_seleccionado == "Azul":
        root.config(bg="blue")

root = tk.Tk()
root.title("Ejercicio 5")
root.geometry("300x200")

var_color = tk.StringVar()
var_color.set(None)

radio_rojo = tk.Radiobutton(root, text="Rojo", variable=var_color, value="Rojo", command=actualizar_fondo)
radio_rojo.pack()

radio_verde = tk.Radiobutton(root, text="Verde", variable=var_color, value="Verde", command=actualizar_fondo)
radio_verde.pack()

radio_azul = tk.Radiobutton(root, text="Azul", variable=var_color, value="Azul", command=actualizar_fondo)
radio_azul.pack()












root.mainloop()
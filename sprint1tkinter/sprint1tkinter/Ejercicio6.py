import tkinter as tk
from tkinter import messagebox


def mostrar_fruta():
    # Obtener la fruta seleccionada
    try:
        seleccion = listbox.curselection()
        fruta = listbox.get(seleccion)
        etiqueta.config(text=f"Fruta seleccionada: {fruta}")
    except IndexError:
        messagebox.showwarning("Selección", "Por favor, selecciona una fruta.")

root = tk.Tk()
root.title("Ejercicio 5")
root.geometry("400x250")

listbox = tk.Listbox(root)
opciones = ["Manzana","Plátano","Cereza","Naranja"]

for opcion in opciones:
    listbox.insert(tk.END, opcion)
    listbox.pack()

boton = tk.Button(root, text="Mostrar Fruta", command=mostrar_fruta)
boton.pack()

etiqueta = tk.Label(root, text="")
etiqueta.pack()

# Iniciar el bucle principal de la interfaz
root.mainloop()

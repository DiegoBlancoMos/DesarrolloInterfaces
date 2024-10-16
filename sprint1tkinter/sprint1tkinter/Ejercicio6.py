import tkinter as tk
from tkinter import messagebox

def mostrar_fruta():
    # Obtener la fruta seleccionada
    try:
        seleccion = listbox.curselection() #OBTENEMOS LA SELECCIÓN/SELECCIONES ACTUALES
        fruta = listbox.get(seleccion)
        etiqueta.config(text=f"Fruta seleccionada: {fruta}")
    except IndexError:
        messagebox.showwarning("Selección", "Por favor, selecciona una fruta.")

#CREAMOS LA VENTANA PRINCIPAL
root = tk.Tk()
root.title("Ejercicio 5")
root.geometry("400x250")

#CREAMOS LA LISTBOX
listbox = tk.Listbox(root)
opciones = ["Manzana","Plátano","Cereza","Naranja"]
#PONEMOS LAS OPCIONES EN LA LISTBOX
for opcion in opciones:
    listbox.insert(tk.END, opcion)
    listbox.pack()
#CREAMOS BOTÓN PARA MOSTRAR LAS FRUTAS
boton = tk.Button(root, text="Mostrar Fruta", command=mostrar_fruta)
boton.pack()
#CREAMOS UNA ETIQUETA QUE SE ACTUALIZARÁ DEPENDIENDO DE LAS FRUTAS QUE SE SELECCIONEN
etiqueta = tk.Label(root, text="")
etiqueta.pack()

# Iniciar el bucle principal de la interfaz
root.mainloop()

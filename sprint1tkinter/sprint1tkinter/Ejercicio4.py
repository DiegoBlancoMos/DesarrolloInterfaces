import tkinter as tk


# Función que actualiza la etiqueta según las aficiones seleccionadas
def actualizar_aficiones():
    aficiones_seleccionadas = []

    if var_leer.get():
        aficiones_seleccionadas.append("Leer")
    if var_deporte.get():
        aficiones_seleccionadas.append("Deporte")
    if var_musica.get():
        aficiones_seleccionadas.append("Música")

    if aficiones_seleccionadas:
        etiqueta.config(text="Aficiones seleccionadas: " + ", ".join(aficiones_seleccionadas))
    else:
        etiqueta.config(text="No has seleccionado ninguna afición.")

#CREAMOS LA VENTANA PRINCIPAL
root = tk.Tk()
root.title("Ejercicio 4")
root.geometry("300x200")

#CREAMOS LAS DIFERENTES VARIABLES PARA EL CHECKBUTTON
var_leer = tk.BooleanVar()
var_deporte = tk.BooleanVar()
var_musica = tk.BooleanVar()

etiqueta = tk.Label(root, text="")
etiqueta.pack()

#CREAMOS LE CHECKBUTTON
check_leer=tk.Checkbutton(root,text="LEER",variable=var_leer,command=actualizar_aficiones)
check_leer.pack()
check_deporte=tk.Checkbutton(root,text="DEPORTE",variable=var_deporte,command=actualizar_aficiones)
check_deporte.pack()
check_musica=tk.Checkbutton(root,text="MÚSICA",variable=var_musica,command=actualizar_aficiones)
check_musica.pack()

#INICIAMOS EL BUCLE PRINCIPAL
root.mainloop()
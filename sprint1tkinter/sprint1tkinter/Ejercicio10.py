import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 10")

# Crear el widget Text
texto = tk.Text(root, width=50, height=15)
texto.pack(side=tk.LEFT)

# Crear la Scrollbar
scrollbar = tk.Scrollbar(root, command=texto.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configurar el Text para usar la Scrollbar
texto.config(yscrollcommand=scrollbar.set)

# Añadir un texto largo
texto.insert(tk.END,"""
El Real Club Deportivo de La Coruña, comúnmente conocido como Deportivo de La Coruña o simplemente Deportivo, es un club de fútbol español con sede en La Coruña, Galicia. Fundado en 1906, es uno de los clubes más históricos y emblemáticos de España, especialmente reconocido por su rica tradición y su apasionada afición.

El equipo juega sus partidos como local en el Estadio Riazor, que tiene una capacidad para aproximadamente 30,000 espectadores. A lo largo de su historia, el Deportivo ha tenido momentos destacados en el fútbol español, incluyendo su victoria en la Primera División en la temporada 1999-2000, lo que supuso su primer y único título de liga. Durante ese periodo, el equipo fue conocido como uno de los clubes más competitivos de la liga, gracias a jugadores como Roy Makaay, Fernando Vázquez, y Djalminha, entre otros.

El Deportivo también ha tenido éxito en competiciones de copa, ganando la Copa del Rey en dos ocasiones, en 1995 y 2002. Su participación en competiciones europeas ha sido notable, destacando su participación en la Champions League donde alcanzaron las semifinales en la temporada 2003-2004.

A pesar de los altibajos en los últimos años, incluyendo descensos a categorías inferiores, el club sigue contando con una base de seguidores leal y apasionada. La afición del Deportivo es conocida por su fervor y dedicación, llenando las gradas del Estadio Riazor en cada partido.

El Deportivo de La Coruña no solo es un símbolo del deporte en Galicia, sino también un importante referente cultural y social en la ciudad. Con una rica historia y un compromiso continuo con el fútbol, el club busca regresar a la élite del fútbol español y seguir haciendo historia.

""" )

# Iniciar el bucle principal de la interfaz
root.mainloop()

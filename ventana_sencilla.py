#Importa todo la info
from tkinter import *
#Hace una ventana del elemento TK llamado root (Inicializa la ventana como una clase)
root = Tk()
#Crea primero un objeto, localizado en root con el elemento de texto
label = Label(root, text="Hola prueba")
#Acomoda el texto en la configuracion de default que vendria siendo el centro
label.pack()
#Mantiene corriendo el ciclo hasta que este sea cerrado
root.mainloop()
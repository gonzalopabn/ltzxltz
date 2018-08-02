from tkinter import *
root = Tk()

#Contenedor de arriba
top = Frame(root)
top.pack()
bottom = Frame(root)
bottom.pack(side=BOTTOM)

button1 = Button(top, text="Boton 1", fg="red")
button2 = Button(top, text="Boton 2", fg="blue")
button3 = Button(top, text="Boton 3", fg="green")
button4 = Button(bottom, text="Boton 4", fg="yellow")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)
root.mainloop()
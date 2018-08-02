from tkinter import *
root = Tk()

one = Label(root, text="one", bg="red", fg="white")
one.pack()
two = Label(root, text="two", bg="green", fg="black")
#Rellena el ancho de la pantalla
two.pack(fill=X)
three = Label(root, text="three", bg="blue", fg="black")
#Rellena el ancho de la pantalla
three.pack(fill=Y,side=LEFT)


root.mainloop()
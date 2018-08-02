from tkinter import *
root = Tk()

def imprimir():
    print(("Hola me llamaste?"))

button1 = Button(root, text="Mandame a llamar", command=imprimir)
button1.pack()


root.mainloop()
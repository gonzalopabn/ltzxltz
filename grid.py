from tkinter import *

root = Tk()
root.geometry("800x600")
#Crea las etiquetas para los textbox
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")

#Crea el textbox
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Manteneme adentro")
c.grid(columnspan=2)

root.mainloop()
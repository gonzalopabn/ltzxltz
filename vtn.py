from tkinter import *
root = Tk()
root.attributes('-fullscreen', True)
root.title("Ventana Prueba")
root.geometry('800x600')
### Etiqueta de titulo ###
label_1= Label(root, text="Cuentalitros pa' las fiestas PABN",bg="blue", fg="white", anchor=CENTER, height= "3", font="Roboto 20")
label_1.pack(fill=X)

### Text Box ###
entry_1 = Text(root, height=4, width=30)
entry_1.place(x=100,y=160)
entry_2 = Text(root, height=4, width=30)
entry_2.place(x=100,y=290)
entry_2 = Text(root, height=4, width=30)
entry_2.place(x=100,y=420)

### Etiquetas Textbox ###
label_2 = Label(root, text="Conteo Actual", bg="white", anchor=CENTER, height="2", width="20", font="Roboto 20")
label_2.place(x=400,y=160)
label_3 = Label(root, text="Conteo Diario", bg="white", anchor=CENTER, height="2", width="20", font="Roboto 20")
label_3.place(x=400,y=290)
label_4 = Label(root, text="Conteo Semanal", bg="white", anchor=CENTER, height="2", width="20", font="Roboto 20")
label_4.place(x=400,y=420)
root.mainloop()
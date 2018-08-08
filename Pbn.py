from tkinter import  *

### Se tiene que definir la clase de la primera ventana, dentro de la clase se incluira todo lo relevante a la ventana
class Login():
    ### Se define el construtctor y se usarara "Self para denominarrse a si misma
    def __init__(self,master):
        self.master = master
        #self.master.attributes('-fullscreen', True)
        self.master.geometry("400x300")
        self.master.title("LOGIN")

        self.label1=Label(self.master, text="Usuario", bg="red", fg="black", anchor=CENTER, height="1", width="9",
                        font="Roboto 16").place(x=50,y=50)
        self.labelw = Label(self.master, text="Contrasena", bg="red", fg="black", anchor=CENTER, height="1", width="9",
                            font="Roboto 16").place(x=50, y=100)
        self.ent11 = Entry(self.master, width="9", font="Roboto 16").place(x=200, y=50)
        self.ent12=Entry(self.master,  width="9", font="Roboto 16").place(x=200,y=100)
        self.btn1 = Button(self.master, text="Cambia de ventana", fg="red",command=self.gotoconteo).place(x=300,y=300)

    ## Envia a la segunda ventana
    def gotoconteo(self):
        root2 = Toplevel(self.master)
        gui2 = Conteo(root2)
    ## Se asegura que termine el ciclo
    def fin(self):
        self.master.destroy()

### Segunda clase para segunda ventana
class Conteo():
    def __init__(self,master):
        self.master = master
        self.master.geometry("800x600")
        self.master.title("CONTEO")

        label_1 = Label(self.master, text="Cuentalitros pa' las fiestas PABN", bg="blue", fg="white", anchor=CENTER,
                        height="2", font="Roboto 20")
        label_1.pack(fill=X)
        abst = 0
        ### Text Box ###
        # entry_1 = Text(root, height=4, width=30)
        # entry_1.place(x=100,y=160)
        label_5 = Label(self.master, text="Conteo Actual", bg="red", fg="black", anchor=CENTER, height="2", width="18",
                        font="Roboto 20")
        label_5.place(x=100, y=100)
        label_6 = Label(self.master, text="Conteo Actual", bg="red", fg="black", anchor=CENTER, height="2", width="18",
                        font="Roboto 20")
        label_6.place(x=100, y=230)
        label_7 = Label(self.master, text="Conteo Actual", bg="red", fg="black", anchor=CENTER, height="2", width="18",
                        font="Roboto 20")
        label_7.place(x=100, y=360)

        ### Etiquetas Textbox ###
        label_2 = Label(self.master, text="Conteo Actual", bg="white", anchor=CENTER, height="2", width="20", font="Roboto 20")
        label_2.place(x=400, y=100)
        label_3 = Label(self.master, text="Conteo Diario", bg="white", anchor=CENTER, height="2", width="20", font="Roboto 20")
        label_3.place(x=400, y=230)
        label_4 = Label(self.master, text="Conteo Semanal", bg="white", anchor=CENTER, height="2", width="20",
                        font="Roboto 20")
        label_4.place(x=400, y=360)


### Ciclo main, de ahi corre todo lo que queiro que empiece
def main():
    root = Tk()
    Inicio = Login(root)
    root.mainloop()
## Repeticion iguess
if __name__ == '__main__':
    main()
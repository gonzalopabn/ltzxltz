from tkinter import  *
import  time
import pymysql.cursors
import tkinter.messagebox

# Connect to the database.
connection = pymysql.connect(host='aguaelrubi.no-ip.com',
                             user='gg',
                             password='1234',
                             db='pipas',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
print("connect successful!!")

### Se tiene que definir la clase de la primera ventana, dentro de la clase se incluira todo lo relevante a la ventana
class Login():
    ### Se define el construtctor y se usarara "Self para denominarrse a si misma
    def __init__(self,master):
        self.master = master
        self.master.configure(bg="white")
        label_10 = Label(self.master, text="Inicia tu sesion para continuar", bg="blue", fg="white", anchor=CENTER,
                        height="2", font="Roboto 20")
        label_10.pack(fill=X)
        #self.master.attributes('-fullscreen', True)
        self.master.geometry("1000x700")
        self.master.title("LOGIN")

        self.usuario = StringVar()
        self.contrasena = StringVar()
        self.label11=Label(self.master, text="Usuario:", fg="black",bg="white", anchor=E, height="2",font="Roboto 26").place(x=180,y=150)
        self.label12= Label(self.master, text="Contrasena:", fg="black",bg="white", anchor=E, height="2",
                            font="Roboto 26").place(x=120, y=250)
        self.ent11= Entry(self.master,textvariable=self.usuario, width="8", font="Roboto 48").place(x=350,y=150)
        self.ent12= Entry(self.master,textvariable=self.contrasena, width="8", font="Roboto 48").place(x=350,y=250)
        self.btn1 = Button(self.master, text="Cambia de ventana", fg="red",command=self.fin).place(x=100,y=200)
        self.btn2 = Button(self.master, text="Iniciar Sesion",font="Roboto 26",command=self.getLogin).place(x=300,y=350)

    ## Envia
    ## Envia a la segunda ventana
    def gotoconteo(self):
        root2 = Toplevel(self.master)
        gui2 = Conteo(root2)
    ## Se asegura que termine el ciclo
    def fin(self):
        connection.commit()
        connection.close()
        print ("Ya me desconecte")
        self.master.destroy()
    def getLogin(self):
        print (self.usuario.get())
        print (self.contrasena.get())
        try:
            query = connection.cursor()

            if (query.execute("SELECT * FROM `usuarios` WHERE `id`='" + str(self.usuario.get()) + "' AND `contrasena`='" + str(self.contrasena.get()) + "'")):
                connection.commit()
                tkinter.messagebox.showinfo('','Gracias por conectarte')
                self.gotoconteo()
            else:
                connection.commit()
                tkinter.messagebox.showwarning('','ERROR')

        finally:
            # Close connection.
            connection.commit()
            #connection.close()

### Segunda clase para segunda ventana
class Conteo():
    def __init__(self,master):
        self.master = master
        self.master.geometry("800x600")
        self.master.title("CONTEO")
        #self.master.attributes('-fullscreen', True)
        self.master.configure(bg="white")
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
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

        def accion():
            # Define como variable global la variable externa a la funcion
            global a, b, c, d
            self.a = self.a + 1
            if self.a == 1:
                if self.b == 0:
                    d = time.time()
            # Asi cambia la propiedad en especifico que se necesita del constructor de etiqueta
            label_5['text'] = self.a
            label_6['text'] = self.b
            label_7['text'] = self.c
            # Calculo para el tiempo activo del llenado
            if self.a == 3:
                self.a = 0
                self.b = self.b + 1
                self.c = self.c + 1
                if self.c == 4:
                    e = time.time()
                    diff = (e - d)
                    minutes, seconds = diff // 60, diff % 60
                    print(minutes)
                    print(seconds)
                    try:

                        with connection.cursor() as cursor:

                            # SQL
                            sql = "INSERT usuario1(identrada,fecha, litros) VALUES (%s, %s, %s)"

                            # Execute query.
                            cursor.execute(sql, (int(18), time.ctime(), self.b))
                            print("enviado")


                    finally:
                        # Close connection.
                        connection.commit()
                        #connection.close()

        btn_1 = Button(self.master, text="Tocame", command=acci on)
        btn_1.place(x=450, y=500)


### Ciclo main, de ahi corre todo lo que queiro que empiece
def main():
    root = Tk()
    Inicio = Login(root)
    root.mainloop()

## Repeticion iguess
if __name__ == '__main__':
    main()

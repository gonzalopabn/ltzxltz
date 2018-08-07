from tkinter import *
import  time
import pymysql.cursors

# Connect to the database.
connection = pymysql.connect(host='aguaelrubi.no-ip.com',
                             user='gg',
                             password='1234',
                             db='pipas',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print("connect successful!!")


root = Tk()
#root.attributes('-fullscreen', True)
root.title("Ventana Prueba")
root.geometry('720x400')
### Etiqueta de titulo ###
label_1= Label(root, text="Cuentalitros pa' las fiestas PABN",bg="blue", fg="white", anchor=CENTER, height= "2", font="Roboto 20")
label_1.pack(fill=X)
abst = 0
### Text Box ###
#entry_1 = Text(root, height=4, width=30)
#entry_1.place(x=100,y=160)
label_5 = Label(root, text="Conteo Actual", bg="red", fg="black", anchor=CENTER, height="2", width="18", font="Roboto 20")
label_5.place(x=100,y=100)
label_6 = Label(root, text="Conteo Actual", bg="red", fg="black", anchor=CENTER, height="2", width="18", font="Roboto 20")
label_6.place(x=100,y=230)
label_7 = Label(root, text="Conteo Actual", bg="red", fg="black", anchor=CENTER, height="2", width="18", font="Roboto 20")
label_7.place(x=100,y=360)


### Etiquetas Textbox ###
label_2 = Label(root, text="Conteo Actual", bg="white", anchor=CENTER, height="2", width="20", font="Roboto 20")
label_2.place(x=400,y=100)
label_3 = Label(root, text="Conteo Diario", bg="white", anchor=CENTER, height="2", width="20", font="Roboto 20")
label_3.place(x=400,y=230)
label_4 = Label(root, text="Conteo Semanal", bg="white", anchor=CENTER, height="2", width="20", font="Roboto 20")
label_4.place(x=400,y=360)

a = 0
b = 0
c = 0

def accion():
    #Define como variable global la variable externa a la funcion
    global a, b, c, d
    a = a+1
    if a == 1:
        if b == 0:
            d = time.time()
    #Asi cambia la propiedad en especifico que se necesita del constructor de etiqueta
    label_5['text']= a
    label_6['text']= b
    label_7['text']= c
    # Calculo para el tiempo activo del llenado
    if a == 3:
        a = 0
        b = b+1
        c = c+1
        if b == 4:
            e = time.time()
            diff = (e-d)
            minutes, seconds = diff // 60, diff % 60
            print (minutes)
            print (seconds)
            try:

                with connection.cursor() as cursor:

                    # SQL
                    sql = "INSERT usuario1(identrada,fecha, litros) VALUES (%s, %s, %s)"

                    # Execute query.
                    cursor.execute(sql, (int(10), time.ctime(), b))
                    print ("enviado")


            finally:
                # Close connection.
                connection.commit()
                connection.close()



btn_1= Button(root, text="Tocame", command=accion)
btn_1.place(x=450,y=500)

root.mainloop()
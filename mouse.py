from tkinter import  *
root = Tk()

def leftClick(event):
    print("IZQUIERDA")

def rightClick(event):
    print(("DERECHA"))


frame = Frame(root, width=300, height=250)
#Asocia el frame con el click de la ezquierda a la accion leftclick
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-3>", rightClick)

frame.pack()



root.mainloop()
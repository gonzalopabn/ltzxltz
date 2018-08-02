from tkinter import *


class botones:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.printButton = Button(frame, text="Print message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Salir", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("WOW HOLA")

root = Tk()
b= botones(root)
root.mainloop()
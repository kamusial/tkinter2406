from tkinter import *

root = Tk()
root.geometry('750x500')

def pozycja(e):
    print(e)
    print(e.x)
    print(e.y)


root.bind('<Motion>', pozycja)

root.mainloop()
import tkinter as tk

root = tk.Tk()
root.title('Tkinter')
root.geometry('600x400+100+50')  #wielkość ona i położenie
#root.resizable(True, False)   #zmiana wielkości okna
root.minsize(200, 200)
root.maxsize(800, 600)
root.attributes('-alpha', 0.5)
root.attributes('-topmost', 1)


message1 = tk.Label(root, text='Pierwszy napis')
message1.pack()   #umieść w oknie

message2 = tk.Label(root, text='Drugi napis')
message2.pack()

root.mainloop()

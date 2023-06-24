import tkinter as tk

root = tk.Tk()
root.title('Tkinter')
root.geometry('600x400+100+50')

message1 = tk.Label(root, text='Pierwszy napis')
message1.pack()

message2 = tk.Label(root, text='Drugi napis')
message2.pack()

root.mainloop()

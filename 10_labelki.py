import tkinter as tk
root = tk.Tk()
root.title('Pojemniki')
root.geometry('400x200')
root.attributes('-topmost', 1)

box1 = tk.Label(root, text="Pojemnik 1", bg='green', fg='white')
box1.pack(padx=10, pady=10)
box2 = tk.Label(root, text="Pojemnik 2", bg='red', fg='white')
box2.pack(ipadx=50, ipady=10)

root.mainloop()
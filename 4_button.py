import tkinter as tk

root = tk.Tk()
root.geometry('500x600')
root.title('Przyciski')
root.attributes('-topmost', 1)
root.configure(bg='light blue')

label = tk.Label(root, text='Hello', font=('Arial', 20))
label.pack(padx=20, pady=50)

#tk.Label(root, text='Hello', font=('Arial', 20)).pack(padx=20, pady=50)

textbox = tk.Text(root, height=3, font=('Arial', 20))
textbox.pack(padx=20, pady=50)

buttonframe = tk.Frame(root)

btn1 = tk.Button(buttonframe, text='1', font=('Arial', 15))
btn1.grid(row=0, column=0)
btn2 = tk.Button(buttonframe, text='2', font=('Arial', 15))
btn2.grid(row=0, column=1)
btn3 = tk.Button(buttonframe, text='3', font=('Arial', 15))
btn3.grid(row=0, column=2)
btn4 = tk.Button(buttonframe, text='4', font=('Arial', 15))
btn4.grid(row=1, column=0)
btn5 = tk.Button(buttonframe, text='5', font=('Arial', 15))
btn5.grid(row=1, column=1)
btn6 = tk.Button(buttonframe, text='6', font=('Arial', 15))
btn6.grid(row=1, column=2)

buttonframe.pack()



root.mainloop()
import tkinter as tk


class MyGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pierwszy program w python GUI tkinter")
        self.root.geometry('600x400+50+20')
        self.root.attributes('-alpha', 0.8)
        self.root.config(background = "Light Blue")
        self.root.attributes('-topmost', 1)

        self.label = tk.Label(self.root, text='moj tekst')
        self.label.config(
            background='#555',
            fg='#F00',
            font=('Arial', 20),
            padx=20,
            pady=20
        )
        self.label.pack()

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 15))

        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text='show', font=('Arial', 15), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Show Message', font=('Arial', 16), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        self.root.mainloop()

    def show_message(self):
        print('Message')
        print(self.check_state.get())
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))   #od początku do końca
        else:


MyGui()
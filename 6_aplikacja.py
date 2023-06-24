import tkinter as tk
from tkinter import messagebox


class MyGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pierwszy program w python GUI tkinter")
        self.root.geometry('600x400+50+20')
        self.root.attributes('-alpha', 0.8)
        self.root.config(background = "Light Blue")
        self.root.attributes('-topmost', 1)

        #menu
        self.menubar = tk.Menu(self.root)

        self.filemenu1 = tk.Menu(self.menubar)
        self.filemenu1.add_command(label='Close', command=self.zamknij)
        self.filemenu1.add_command(label='Clear', command=self.clear)

        self.filemenu2 = tk.Menu(self.menubar)
        self.filemenu2.add_command(label='wiadomosc', command=self.show_message)
        self.filemenu2.add_command(label='wyjscie', command=exit)

        self.menubar.add_cascade(menu=self.filemenu1, label='setings')
        self.menubar.add_cascade(menu=self.filemenu2, label='others')
        self.root.config(menu=self.menubar)

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

        self.textbox.bind("<KeyPress>", self.keypress)

        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text='show', font=('Arial', 15), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Show Message', font=('Arial', 16), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clear_button = tk.Button(self.root, text='Clear', font=('Arial', 16), command=self.clear)
        self.clear_button.pack(padx=10, pady=10)


        self.root.protocol('WM_DELETE_WINDOW', self.zamknij)
        self.root.mainloop()

    def show_message(self):
        print('Message')
        print(self.check_state.get())
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))   #od początku do końca
        else:
            messagebox.showinfo(title='Wiadomosc', message=self.textbox.get('1.0', tk.END))

    def keypress(self, event):
        # print('\n',event)
        # print(event.keysym)
        # print(event.state)
        if event.keysym == 'Return' and event.state == 12:
            print('Nacisnieto ctrl+enter - tak jak prycisk')
            self.show_message()

    def zamknij(self):
        print('Zamknij')
        if messagebox.askyesno(title='Potwierdzenie', message='Czy napewno chces zamaknac?'):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0', tk.END)
        messagebox.showinfo(title='', message='wyczyszczono dane')

MyGui()
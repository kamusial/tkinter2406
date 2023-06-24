import tkinter as tk
from tkinter.messagebox import showinfo
root = tk.Tk()
entry_text = tk.StringVar()
def button_clicked():
    msg = f'Wpisałeś: {entry_text.get()}'
    showinfo(title='Info',message=msg)
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill='x', expand=True)
label = tk.Label(frame, text="Wpisz coś:")
label.pack(fill='x', expand=True)
entry = tk.Entry(frame, textvariable=entry_text)
entry.pack(fill='x', expand=True)
entry.focus()
button = tk.Button(frame, text="Kliknij", command=button_clicked)
button.pack(fill='x', expand=True, pady=10)

root.mainloop()

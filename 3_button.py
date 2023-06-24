import tkinter as tk

root = tk.Tk()

exit_button1 = tk.Button(root, text='Exit', command=lambda: root.quit())
exit_button1.pack(padx=10, pady=10)

exit_button2 = tk.Button(root, text='Exit', command=lambda: root.quit())
exit_button2.pack(padx=10, pady=10)



root.mainloop()
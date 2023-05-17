from tkinter import *
from tkinter import ttk
import Functions as f

root = Tk()
root.title('TLBot v0.01')
root.geometry('400x500+500+300')
root.resizable(False,False)
root.attributes("-alpha", 1)

root.update_idletasks()

btn = ttk.Button(text = "Ключ", command=f.click)
btn.place(x = 30, y = 30, width=80, height=40)

label = Label(text = "Подключение бота")
label.pack()
label.place(x = 30, y = 5)

root.mainloop()
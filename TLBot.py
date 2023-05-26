from tkinter import *
from tkinter import ttk
import threading
import Functions as f

def run_async(event=None):
    threading.Thread(target=f.bot_run).start()

root = Tk()
root.title('TLBot v0.01')
root.geometry('400x500+500+300')
root.resizable(False,False)
root.attributes("-alpha", 1)

root.update_idletasks()

btn_1 = ttk.Button(text = "Ключ", command=f.click)
btn_1.place(x = 30, y = 30, width=80, height=40)

btn_2 = ttk.Button(text = "Пуск", command=run_async)
btn_2.place(x = 120, y = 30, width=50, height=40)

btn_3 = ttk.Button(text = "Стоп", command=f.bot_stop)
btn_3.place(x = 180, y = 30, width=50, height=40)

label = Label(text = "Подключение бота")
label.pack()
label.place(x = 30, y = 5)

root.mainloop()
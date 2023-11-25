import threading

from Functions import *

def run_async(event=None):
    threading.Thread(target=bot_run).start()

root = Tk()
root.title('TLBot v0.01')
root.geometry('400x250+500+300')
root.resizable(False,False)
root.attributes("-alpha", 1)

root.update_idletasks()

entry1 = ttk.Entry()
entry1.place(x = 30, y = 100, width=300, height=20)

# query = entry.get()

entry2 = ttk.Entry()
entry2.place(x = 30, y = 150, width=300, height=20)


btn_1 = ttk.Button(text = "Ключ", command=enter_key)
btn_1.place(x = 30, y = 30, width=80, height=40)

btn_2 = ttk.Button(text = "Пуск", command=run_async)
btn_2.place(x = 120, y = 30, width=50, height=40)

btn_3 = ttk.Button(text = "Стоп", command=bot_stop)
btn_3.place(x = 180, y = 30, width=50, height=40)

btn_4 = ttk.Button(text = "Добавить запрос", command=lambda: add_data(entry1.get(),entry2.get()))
btn_4.place(x = 30, y = 185, width=120, height=30)

label1 = Label(text = "Подключение бота")
label1.place(x = 30, y = 5)

label2 = Label(text = "Вопрос пользователя")
label2.place(x = 30, y = 75)

label3 = Label(text = "Ответ бота")
label3.place(x = 30, y = 125)

root.mainloop()
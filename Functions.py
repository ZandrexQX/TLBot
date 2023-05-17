from tkinter import *
from tkinter import ttk
import telebot

def tbot(key):
    bot = telebot.TeleBot(key, parse_mode=None)
    bot.send_message(375230092, "Бот запущен")

def get_key(window, entry):
    window.grab_release()
    key = entry.get()
    window.destroy()
    tbot(key)

def click():
    window = Toplevel()
    window.title("Ввод ключа Бота")
    window.geometry("500x80+300+300")
    window.protocol("WM_DELETE_WINDOW", lambda: get_key(window, entry)) # перехватываем нажатие на крестик
    
    entry = ttk.Entry(window)
    entry.pack()
    entry.place(x = 10, y = 30, width=400, height=20)
    
    label = Label(window, text = "Введите ключ:")
    label.pack()
    label.place(x = 8, y = 5)
    
    close_button = ttk.Button(window, text="Ok", command=lambda: get_key(window, entry))
    close_button.pack()
    close_button.place(x = 415, y = 28)
    
    window.grab_set()
import os
import aiosqlite
import sqlite3

if not os.path.exists('mydatabase.db'):
    conn = aiosqlite.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE bot_data
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_query TEXT NOT NULL,
                    bot_answer TEXT NOT NULL);''')
    # cursor.execute('''CREATE TABLE answers
    #                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                 user_answer TEXT NOT NULL);''')
    conn.commit()
    conn.close()


# cursor.execute("INSERT INTO bot_data (user_query, bot_answer) VALUES ('Привет', 'Приветствую')")

async def read_data(a):
    async with aiosqlite.connect('mydatabase.db') as db:
        cursor = await db.execute(f"SELECT bot_answer FROM bot_data WHERE user_query = '{a}'")
        try:
            answer, = await cursor.fetchone()
        except:
            answer = ""
        await db.commit()
        return answer

async def add_data(query, answer):
    async with aiosqlite.connect('mydatabase.db') as db:
        cursor = await db.cursor()
        await cursor.execute(f"INSERT INTO bot_data (user_query, bot_answer) VALUES ('{query}', '{answer}')")
        await db.commit()



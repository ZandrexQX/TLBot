import asyncio
import telegram
from telegram.error import NetworkError
import Dict_bot

UPDATE_ID = None
flag = None

async def update_bot(bot):
    global UPDATE_ID
    for update in await bot.get_updates(offset=UPDATE_ID, timeout=10):
        UPDATE_ID = update.update_id + 1
        # print(UPDATE_ID)
                  
        id_chat =  (await bot.get_updates())[0].message.from_user.id
        text = ((await bot.get_updates())[0].message.text)
        if text in Dict_bot.dict_command.keys():
            await bot.send_message(text=Dict_bot.dict_command[text], chat_id=id_chat)
        else: await bot.send_message(text="Ответа на это нет", chat_id=id_chat)

class TBot:
    def __init__(self, key):
        self.__key = key
    
    async def bot_run(self):
        global UPDATE_ID
        global flag
        flag = True
        bot = telegram.Bot(self.__key)
        async with bot:
            await bot.send_message(text='Бот запущен', chat_id=375230092)
            # print(await bot.get_me())
            # print((await bot.get_updates())[0])
            try:
                UPDATE_ID = (await bot.get_updates())[0].update_id
            except IndexError:
                UPDATE_ID = None
            while flag:
                asyncio.sleep(1000)
                try:
                    await update_bot(bot)
                except NetworkError:
                    asyncio.sleep(5)
                    
    def bot_stop(self):
        global flag
        flag = False
    
    
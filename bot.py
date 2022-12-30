import time
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import logging
from config import TOKEN
import sort as s



logging.basicConfig(level=logging.INFO)
bot = Bot(token = TOKEN)
dp = Dispatcher(bot)
async def on_startup(_):
    print('Bot is running...')

@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЯ умею выполнять операции с числами\n"
                        "Введите выражение:\n "
                        "(пример:\n 2-3j + 1+4j\n 1/2 * 3/4\n 3 - 5)")
    # start_buttons = ['complex', 'rational', 'button3']
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*start_buttons)
    # await message.answer('Выберете действие', reply_markup=keyboard)


@dp.message_handler()
async def calc(message: types.Message):
    await message.reply(s.sort(message.text))


#time.asctime() #текущее время
# await message.answer(message.text)
# await message.reply(message.text)
#await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)








import logging
from aiogram import Bot, Dispatcher, executor, types
import markup as nav

API_TOKEN = '2034064673:AAF2bjxD6CdtbBqC8HNyYsdZeD3FHwvD3CQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Powered by @vetallb\nВиберіть 'Лекційний', або 'Практичний'", reply_markup = nav.mainMenu)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == 'Лекційний':
        await bot.send_message(message.from_user.id, 'Лекційне 🪟Меню', reply_markup = nav.lecMenu)
    elif message.text == '🎲Інженерія':
        await bot.send_message(message.from_user.id, 'Барабан https://meet.google.com/ywq-mxdr-jwp')
    elif message.text == '🍕Графіка':
        await bot.send_message(message.from_user.id, 'Сілагін https://meet.google.com/ims-obmj-kxw')
    elif message.text == '💹Ймовірність':
        await bot.send_message(message.from_user.id, 'Озеранський В.С https://meet.google.com/gzb-opih-efj')
    elif message.text == '🔱Виш мат':
        await bot.send_message(message.from_user.id, 'Кирилащук С.А. https://meet.google.com/vzn-xsqv-kix')
    elif message.text == '🍫Фіз-вих':
        await bot.send_message(message.from_user.id, 'Тихонова С.В. https://meet.google.com/qpo-yurf-iau')
    elif message.text == '💤Філософія':
        await bot.send_message(message.from_user.id, 'Хома О.І. https://meet.google.com/gvs-xwxz-tjd')
    elif message.text == '🙉Психологія':
        await bot.send_message(message.from_user.id, 'Прищак М.Д. https://meet.google.com/prz-chxu-sny')
    elif message.text == '🏳️‍⚧️English':
        await bot.send_message(message.from_user.id, 'English', reply_markup = nav.EnglecMenu)
    elif message.text == '🪟Меню':
        await bot.send_message(message.from_user.id, '🪟Меню Лекцій', reply_markup = nav.lecMenu)
    elif message.text == '📜Меню':
        await bot.send_message(message.from_user.id, '📜Меню Практика', reply_markup = nav.practMenu)
    elif message.text == '👈👈👈':
        await bot.send_message(message.from_user.id, '👌', reply_markup = nav.mainMenu)
    elif message.text == '😎1 пг':
        await bot.send_message(message.from_user.id, '1 пг Габрійчук Л.Е https://meet.google.com/cip-rgri-sws')
    elif message.text == '👻2 пг':
        await bot.send_message(message.from_user.id, '2 пг ХЗ https://meet.google.com/qqb-agmt-bhe')


#--- Практичний тиждень
    if message.text == 'Практичний':
        await bot.send_message(message.from_user.id, '📜Меню Практика', reply_markup = nav.practMenu)
    elif message.text == '🐻Ймовірність':
        await bot.send_message(message.from_user.id, 'Крилик Л.В https://meet.google.com/NO_INFO_YET')
    elif message.text == '✨Виш мат':
        await bot.send_message(message.from_user.id, 'Абрамчук І.В https://meet.google.com/NO_INFO_YET')
    elif message.text == '🔥Інженерія':
        await bot.send_message(message.from_user.id, 'Белзецький Р.С :( https://meet.google.com/sqs-kbgf-tyq')


    
#--- Практичний тиждень

    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)





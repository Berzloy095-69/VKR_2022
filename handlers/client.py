from aiogram import types,Bot
from create import Dispatcher,bot
from keyboard import kb_client
from aiogram.types import ReplyKeyboardRemove



#@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
  try:
    await bot.send_message(message.from_user.id,'Здравствуйте',reply_markup=kb_client)
    await message.delete()
  except:
    await message.reply('Общение с ботом через ЛС,напишите ему:\nhttps://web.telegram.org/k/')
    

#@dp.message_handler(commands=['Режим_работы'])
async def work_open_command(message:types.Message):
  await bot.send_message(message.from_user.id,'Пн-Пт с 8:00 ДО 18:00, Сб-Вс выходной!')

#@dp.message_handler(commands=['Геолокация'])
async def work_location_command(message:types.Message):
  await bot.send_message(message.from_user.id,'Рабочая д.15', reply_markup=ReplyKeyboardRemove())



#dp.message_handler(commands=['Вакансии'])
#async def work_have_command(message:types.Message):
  #for ret in cur.execute("SELECT * for menu"). fetchall():
   # await bot.send_photo(message.from_user.id, ret[0],f'{ret[1]}\nОписание: {ret[2]}\nЗарплата {ret[-1]}')




def register_handler_worker(dp:Dispatcher):
  dp.register_message_handler(send_welcome,commands=['start','help'])
  dp.register_message_handler(work_open_command,commands=['Режим_работы'])
  dp.register_message_handler(work_location_command,commands=['Геолокация'])
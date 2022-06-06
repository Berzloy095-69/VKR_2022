from aiogram import types 
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup




class FSMadmin(StatesGroup):
    photo = State()
    name = State()
    classes = State()
    price = State()

@dp.message_handler(commands="Загрузить",state=None)
async def cm_start(message : types.Message):
    await FSMadmin.photo.set
    await message.reply('Напиши сколько классов закончино')




@dp.message_handler(content_types=['Загрузить'],state=FSMadmin.photo)
async def write_clases(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['Загрзить'] = message.photo[0].file.id
    await FSMadmin.next()
    await message.reply('Теперь введи название')

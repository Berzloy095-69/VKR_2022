from aiogram.utils import executor
from create import dp


async def on_startup(_):
  print('Бот вышел в онлайн')
  

from handlers import admin, client,other

client.register_handler_worker(dp)
other.register_handler_other(dp)


executor.start_polling(dp,skip_updates=True, on_startup=on_startup)

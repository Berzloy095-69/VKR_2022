from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove


b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Геолокация')
b3 = KeyboardButton ('/Вакансии')
b4 = KeyboardButton('/поделиться номером', request_contact=True)
b5 = KeyboardButton('/Отправить местоположение', request_location=True)


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2, b3).add(b4).add(b5)

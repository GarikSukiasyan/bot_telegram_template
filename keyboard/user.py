from telebot import types


# ============================ Markup Buttons ======================


# Клавиатура при нажатии -> /start
btn_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
_btn_key_market_1 = types.KeyboardButton("Профиль")
_btn_key_market_2 = types.KeyboardButton("Баланс")
_btn_key_market_3 = types.KeyboardButton("Маркет")
btn_menu.add(_btn_key_market_1, _btn_key_market_2)
btn_menu.add(_btn_key_market_3)

# Клавиатура при нажатии -> /start
btn_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
_btn_menu_profile = types.KeyboardButton("Профиль")
_btn_menu_accounts = types.KeyboardButton("Аккаунты")
_btn_menu_function = types.KeyboardButton("Функции")
btn_menu.add(_btn_menu_profile, _btn_menu_accounts)
btn_menu.add(_btn_menu_function)


# Клавиатура при нажатии -> Профиль
btn_profile = types.ReplyKeyboardMarkup(resize_keyboard=True)
_btn_profile_0 = types.KeyboardButton("Кнопка")
_btn_profile_1 = types.KeyboardButton("Назад")
btn_profile.add(_btn_profile_0)
btn_profile.add(_btn_profile_1)


# Клавиатура при нажатии -> Аккаунты
btn_accounts = types.ReplyKeyboardMarkup(resize_keyboard=True)
_btn_accounts_0 = types.KeyboardButton("Добавить")
_btn_accounts_1 = types.KeyboardButton("Удалить")
_btn_accounts_2 = types.KeyboardButton("Статус")
_btn_accounts_3 = types.KeyboardButton("Назад")
btn_accounts.add(_btn_accounts_0, _btn_accounts_1)
btn_accounts.add(_btn_accounts_2, _btn_accounts_3)


# Клавиатура при нажатии -> Функции
btn_function = types.ReplyKeyboardMarkup(resize_keyboard=True)
_btn_function_0 = types.KeyboardButton("Спаммер")
_btn_function_1 = types.KeyboardButton("Инвайтер")
_btn_function_2 = types.KeyboardButton("Парсер")
_btn_function_3 = types.KeyboardButton("Вступить")
_btn_function_4 = types.KeyboardButton("Инструкция")
_btn_function_5 = types.KeyboardButton("Назад")
btn_function.add(_btn_function_0, _btn_function_1, _btn_function_2)
btn_function.add(_btn_function_3, _btn_function_4, _btn_function_5)

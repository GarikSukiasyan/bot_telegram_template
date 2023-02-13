from telebot import types

# Клавиатура при нажатии -> /admin
btn_admin_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
_btn_admin_menu_1 = types.KeyboardButton("Stat")
_btn_admin_menu_2 = types.KeyboardButton("User")
_btn_admin_menu_3 = types.KeyboardButton("/start")
_btn_admin_menu_4 = types.KeyboardButton("Shop")
btn_admin_menu.add(_btn_admin_menu_1, _btn_admin_menu_2)
btn_admin_menu.add(_btn_admin_menu_3, _btn_admin_menu_4)


# Клавиатура при нажатии -> User
btn_admin_user = types.ReplyKeyboardMarkup(resize_keyboard=True)
_btn_admin_user_1 = types.KeyboardButton("Ban")
_btn_admin_user_2 = types.KeyboardButton("Unban")
_btn_admin_user_3 = types.KeyboardButton("Money")
_btn_admin_user_4 = types.KeyboardButton("Unmoney")
_btn_admin_user_5 = types.KeyboardButton("Mailing")
_btn_admin_user_6 = types.KeyboardButton("Info")
_btn_admin_user_7 = types.KeyboardButton("/start")
btn_admin_user.add(_btn_admin_user_1, _btn_admin_user_2)
btn_admin_user.add(_btn_admin_user_3, _btn_admin_user_4)
btn_admin_user.add(_btn_admin_user_5)
btn_admin_user.add(_btn_admin_user_6, _btn_admin_user_7)


# Клавиатура при нажатии -> Магазин
btn_admin_shop = types.ReplyKeyboardMarkup(resize_keyboard=True)
_btn_admin_shop_1 = types.KeyboardButton("Status")
_btn_admin_shop_2 = types.KeyboardButton("/admin")
_btn_admin_shop_3 = types.KeyboardButton("Добавить")
_btn_admin_shop_4 = types.KeyboardButton("Удалить")
btn_admin_shop.add(_btn_admin_shop_1, _btn_admin_shop_2)
btn_admin_shop.add(_btn_admin_shop_3, _btn_admin_shop_4)


# Клавиатура при нажатии -> Отменить
btn_admin_cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
_btn_admin_cancel_1 = types.KeyboardButton("Отменить")
btn_admin_cancel.add(_btn_admin_cancel_1)


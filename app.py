#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

from handler import admin
from handler import user
from function.bot_and_db.bot_and_db import bot


print('Bot is Start')

# Регистрируем команды Пользователей
user.register_handler_user(bot)

# Регистрируем команды Администратора
#admin.register_handler_admin(bot)


bot.polling(none_stop=True, interval=2)

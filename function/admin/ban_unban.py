from keyboard import admin
from function.bot_and_db.bot_and_db import bot
from function.bot_and_db.bot_and_db import db




# Блочим пользователя по id
def user_ban(message):
	user_id = message.text

	if user_id != "Отменить":

		stat = db.ban_user(user_id)

		if str(stat) == "Good":
			bot.send_message(message.from_user.id, "Пользователь был заблокирован", reply_markup=admin.btn_admin_user)

			bot.send_message(user_id, "Вы были заблокированы")

		elif str(stat) == "Error":
			bot.send_message(message.from_user.id, "Прозошла ошибка, пользователь не найден", reply_markup=admin.btn_admin_user)

		else:
			pass

	elif user_id == "Отменить":
		bot.send_message(message.from_user.id, "Вы отменили действие бана", reply_markup=admin.btn_admin_user)


# Разблокируем пользователя по id
def user_unban(message):
	user_id = message.text

	if user_id != "Отменить":
		stat = db.ban_user(user_id)

		if str(stat) == "Good":
			bot.send_message(message.from_user.id, "Пользователь был разблокирован", reply_markup=admin.btn_admin_user)

			bot.send_message(user_id, "Вы были разблокированы")

		elif str(stat) == "Error":
			bot.send_message(message.from_user.id, "Прозошла ошибка, пользователь не найден", reply_markup=admin.btn_admin_user)

		else:
			pass

	elif user_id == "Отменить":
		bot.send_message(message.from_user.id, "Вы отменили действие бана", reply_markup=admin.btn_admin_user)

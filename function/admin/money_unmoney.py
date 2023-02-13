from keyboard import admin
from function.bot_and_db.bot_and_db import bot
from function.bot_and_db.bot_and_db import db




# Выдать n-ую сумму на счет | получаем id пользователя
def add_money(message):
	user_id = message.text

	if user_id != "Отменить":
		stat = db.check_user_in_db(user_id)

		if str(stat) == "Good":
			bot.send_message(message.from_user.id, "Пользователь найде, теперь пришлите сумму которую нужно выдать", reply_markup=admin.btn_admin_cancel)

			bot.register_next_step_handler(message, add_money_2)

		elif str(stat) == "Error":
			bot.send_message(message.from_user.id, "Прозошла ошибка, пользователь не найден")

		else:
			pass

	elif user_id == "Отменить":
		bot.send_message(message.from_user.id, "Вы отменили действие бана", reply_markup=admin.btn_admin_user)


# Выдать n-ую сумму на счет | получаем сумму
def add_money_2(message):
	money = message.text

	if money != "Отменить":
		stat = db.check_user_in_db(money)

		if str(stat) == "Good":
			bot.send_message(message.from_user.id, "Сумма была выдана", reply_markup=admin.btn_admin_cancel)

			# bot.send_message(user_id, "Ваш баланс пополнени на: xx руб")

		elif str(stat) == "Error":
			bot.send_message(message.from_user.id, "Прозошла ошибка, пользователь не найден")

		else:
			pass

	elif money == "Отменить":
		bot.send_message(message.from_user.id, "Вы отменили действие бана", reply_markup=admin.btn_admin_user)


# Снять n-ую сумму со счета | получаем id
def del_money(message):
	user_id = message.text

	if user_id != "Отменить":
		stat = db.check_user_in_db(user_id)

		if str(stat) == "Good":
			bot.send_message(message.from_user.id, "Пользователь найде, теперь пришлите сумму которую нужно выдать", reply_markup=admin.btn_admin_cancel)

		elif str(stat) == "Error":
			bot.send_message(message.from_user.id, "Прозошла ошибка, пользователь не найден")

		else:
			pass

	elif user_id == "Отменить":
		bot.send_message(message.from_user.id, "Вы отменили действие бана", reply_markup=admin.btn_admin_user)


# Снять n-ую сумму со счета | получаем сумму
def del_money_2(message):
	money = message.text

	if money != "Отменить":
		stat = db.check_user_in_db(money)

		if str(stat) == "Good":
			bot.send_message(message.from_user.id, "Сумма была выдана", reply_markup=admin.btn_admin_cancel)

			# bot.send_message(user_id, "Ваш баланс пополнени на: xx руб")

		elif str(stat) == "Error":
			bot.send_message(message.from_user.id, "Прозошла ошибка, пользователь не найден")

		else:
			pass

	elif money == "Отменить":
		bot.send_message(message.from_user.id, "Вы отменили действие бана", reply_markup=admin.btn_admin_user)
from keyboard import admin
from function.bot_and_db.bot_and_db import bot
from function.bot_and_db.bot_and_db import db




# Получаем id пользователя
def user_information(message):
	user_id = message.text

	if user_id != "Отменить":

		name, link, balance, black = db.my_profil(user_id)

		if str(name) != "Error":
			bot.send_message(
				message.from_user.id,
				"ID: " + str(user_id) +
				"\nИмя: " + str(name) +
				"\nСсылка: @" + str(link) +
				"\nБаланс: " + str(balance) +
				"\nБан: " + str(black),
				reply_markup=admin.btn_admin_user)

		elif str(name) == "Error":
			bot.send_message(message.from_user.id, "Прозошла ошибка, пользователь не найден", reply_markup=admin.btn_admin_user)

		else:
			pass

	elif user_id == "Отменить":
		bot.send_message(message.from_user.id, "Вы отменили действие бана", reply_markup=admin.btn_admin_user)
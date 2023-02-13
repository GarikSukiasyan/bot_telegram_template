from function.bot_and_db.bot_and_db import bot
from function.bot_and_db.bot_and_db import db
from keyboard import admin




# делаем рассылку сообщения
def mailing(message):
	if message.text != "Отменить":

		list_users = db.list_user_id()

		bot.send_message(
			message.from_user.id,
			"Началась рассылка",
			reply_markup=admin.btn_admin_user)

		for i in list_users:
			bot.forward_message(chat_id=i[0],
			                    from_chat_id=message.chat.id,  #
			                    message_id=message.message_id)


	elif message.text == "Отменить":
		bot.send_message(message.from_user.id, "Вы отменили действие бана", reply_markup=admin.btn_admin_user)
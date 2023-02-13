import os

from function.bot_and_db.bot_and_db import bot
from function.bot_and_db.bot_and_db import db
import zipfile
from config import config

# Сохраняем архив
def save_zip_file_akk(message):
	try:
		chat_id = message.chat.id

		file_info = bot.get_file(message.document.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		# Сохраним в корне проекта
		src = message.document.file_name;

		if config.status_os == "MAC":
			src = src
		elif config.status_os == "Windows":
			src = "database\\users\\" + str(message.from_user.id) + "\\" + src

		with open(src, 'wb') as new_file:
			new_file.write(downloaded_file)

		bot.reply_to(message, "Пожалуй, я сохраню это")

		if config.status_os == "MAC":
			path = "" + str(message.from_user.id)
		elif config.status_os == "Windows":
			path = "database\\users\\" + str(message.from_user.id) + "\\"

		# Разархивируем
		fantasy_zip = zipfile.ZipFile(src)
		fantasy_zip.extractall(path)
		fantasy_zip.close()

		# Удаляем скаченый архив
		os.remove(src)


	except Exception as e:
		bot.reply_to(message, e)
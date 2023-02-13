import os.path
from config import config

# Узнать количество аккаунтов у пользователя
def num_akk_user(user_id):
	path = ''

	if config.status_os == "MAC":
		path = "" + str(user_id)
	elif config.status_os == "Windows":
		path = "database\\users\\" + str(user_id)

	num_akk = len([f for f in os.listdir(path)
	                 if os.path.isfile(os.path.join(path, f))])

	if int(num_akk) != 0:
		num_akk = int(num_akk) / 2

	return int(num_akk)


# Удалить аккаунт у пользователя
def dell_my_akk(message):
	path = ''

	if config.status_os == "MAC":
		path = "" + str(message.from_user.id)
	elif config.status_os == "Windows":
		path = "database\\users\\" + str(message.from_user.id)

	list_my_akk = [f for f in os.listdir(path)
	                 if os.path.isfile(os.path.join(path, f))]

	# Проверяем отменили ли действие
	# Если нет, проверяем наличие акка в папке
	# Если акк есть то удаляем его
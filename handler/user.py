import time
from config import config
from function.bot_and_db.bot_and_db import bot
from function.bot_and_db.bot_and_db import db
from function.user.my_akk_num import *
from function.user.save_akk import *
from keyboard import user


# Функция обработки команды /start | Готово
def get_text_start(message):
	# user_id записан в базе ?
	status_user = db.check_the_user(message.from_user.id, message.from_user.last_name, message.from_user.username)

	# Если да
	if status_user == True:
		bot.send_message(message.from_user.id, "Выберите действие",
						 reply_markup=user.btn_menu)


	# Если нет
	elif status_user == False:
		# Текущее время
		tek_ti = time.time()

		if config.status_os == "MAC":
			path = "stat.txt"
		elif config.status_os == "Windows":
			path = "database\\stat.txt"

		# Записываем статистику
		with open(path, 'a', encoding="utf-8") as f:
			f.write(f'{message.from_user.id}:{int(tek_ti)} \n')

		bot.send_message(
			message.from_user.id,
			text='Toftik Бот - Это телеграм бот для управления Вашими аккаунтами телеграмма. Инструкция бла бла бла',
			reply_markup=user.btn_menu)

#ol_t = 0

# Функция обарботки кнопки "Профиль" Исправь имя ишет Фамилию
def get_button_profile(message):
	# Статус бана
	name, link, balance, user_ban = db.my_profil(message.from_user.id)

	num_akk = num_akk_user(message.from_user.id)

	# Система анти флуда
	#global ol_t

	#t = time.time()

	#print(int(t))
	#print(int(ol_t))

	# if int(t) != int(ol_t):
	# 	pass
	# elif int(t) == int(ol_t):
	# 	ol_t = t
	# 	print("Спамит")

	if user_ban == 'False': # and int(t) != int(ol_t):
		#ol_t = t

		bot.send_message(
			message.from_user.id,
			"[Профиль]"
			"\nИмя: " + str(name) +
			"\nID: " + str(message.from_user.id) +
			"\nБаланс: " + str(balance) +
			"\nАккаунтов: " + str(num_akk) +
			"\nПополнить баланс:")

	elif user_ban == 'True':
		pass


# Функция обработки кнопки "Аккаунты" | Готово
def get_button_accounts(message):
	# Статус бана
	name, link, balance, user_ban = db.my_profil(message.from_user.id)

	if user_ban == 'False':
		bot.send_message(message.from_user.id, "Доступные действия:",
						 reply_markup=user.btn_accounts)


	elif user_ban == 'True':
		pass


# Функция обработки кнопки "Функции" | Готово
def get_button_function(message):
	# Статус бана
	name, link, balance, user_ban = db.my_profil(message.from_user.id)

	if user_ban == 'False':
		bot.send_message(message.from_user.id,
		                 "Доступный функционал бота",
						 reply_markup=user.btn_function)

	elif user_ban == 'False':
		pass


# Функция обработки кнопки "Спаммер"
def get_button_spam(message):
	# Статус бана
	name, link, balance, user_ban = db.my_profil(message.from_user.id)

	if user_ban == 'False':
		bot.send_message(message.from_user.id, "Функция спама")

	elif user_ban == 'False':
		pass


# Функция обработки кнопки "Инвайтер"
def get_button_invite(message):
	# Статус бана
	name, link, balance, user_ban = db.my_profil(message.from_user.id)

	if user_ban == 'False':
		bot.send_message(message.from_user.id, "Функция инвайта")

	elif user_ban == 'False':
		pass


# Функция обработки кнопки "Парсер"
def get_button_parser(message):
	# Статус бана
	name, link, balance, user_ban = db.my_profil(message.from_user.id)

	if user_ban == 'False':
		bot.send_message(message.from_user.id, "Функция парсера")

	elif user_ban == 'False':
		pass


# Функция обработки кнопки "Вступить"
def get_button_subscription(message):
	# Статус бана
	name, link, balance, user_ban = db.my_profil(message.from_user.id)

	if user_ban == 'False':
		bot.send_message(message.from_user.id, "Вступление в чаты")

	elif user_ban == 'False':
		pass


# Функция обработки кнопки "Инструкция"
def get_button_manual(message):
	# Статус бана
	name, link, balance, user_ban = db.my_profil(message.from_user.id)

	if user_ban == 'False':
		bot.send_message(message.from_user.id, "Инструкция работы с ботом")

	elif user_ban == 'False':
		pass


# Функция обработки кнопки "Купить"
def get_button_buy_akk(message):
	# Статус бана
	name, link, balance, user_ban = db.my_profil(message.from_user.id)

	if user_ban == 'False':
		bot.send_message(message.from_user.id, "Купить аккаунт")

	elif user_ban == 'False':
		pass


# Функция обработки кнопки "Добавить"
def get_button_add_akk(message):
	# Статус бана
	name, link, balance, user_ban = db.my_profil(message.from_user.id)

	if user_ban == 'False':
		bot.send_message(
			message.from_user.id,
			"Что бы добавить аккаунты, пришлите архив хранящий аккаунты.")

		bot.register_next_step_handler(message, save_zip_file_akk)

	elif user_ban == 'False':
		pass


# Функция обработки кнопки "Удалить"
def get_button_akk_del(message):
	# Статус бана
	name, link, balance, user_ban = db.my_profil(message.from_user.id)

	if user_ban == 'False':
		bot.send_message(message.from_user.id, "Удалить аккаунт")

	elif user_ban == 'False':
		pass


# Функция обработки кнопки "Статус"
def get_button_akk_stat(message):
	# Статус бана
	name, link, balance, user_ban = db.my_profil(message.from_user.id)

	if user_ban == 'False':
		bot.send_message(
			message.from_user.id,
			"Статус аккаунтов:"
			"\nВсего:"
			"\nБан навсегда:"
			"\nБан временный:")

	elif user_ban == 'False':
		pass


# Функция возврата в "Меню"
def get_button_back(message):
	# Статус бана
	name, link, balance, user_ban = db.my_profil(message.from_user.id)

	if user_ban == 'False':
		bot.send_message(message.from_user.id, "Доступные действия:",
						 reply_markup=user.btn_menu)

	elif user_ban == 'False':
		pass


# регестрируем наши финкции указывая для каждой команды свою функцию
def register_handler_user(bot):
	bot.register_message_handler(get_text_start, commands=['start'])
	bot.register_message_handler(get_button_profile, regexp='Профиль')
	bot.register_message_handler(get_button_accounts, regexp='Аккаунты')
	bot.register_message_handler(get_button_function, regexp='Функции')
	bot.register_message_handler(get_button_spam, regexp="Спаммер")
	bot.register_message_handler(get_button_invite, regexp="Инвайтер")
	bot.register_message_handler(get_button_parser, regexp="Парсер")
	bot.register_message_handler(get_button_subscription, regexp="Вступить")
	bot.register_message_handler(get_button_manual, regexp="Инструкция")
	bot.register_message_handler(get_button_buy_akk, regexp="Купить")
	bot.register_message_handler(get_button_add_akk, regexp="Добавить")
	bot.register_message_handler(get_button_akk_del, regexp="Удалить")
	bot.register_message_handler(get_button_akk_stat, regexp="Статус")
	bot.register_message_handler(get_button_back, regexp='Назад')
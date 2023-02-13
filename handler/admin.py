from function.bot_and_db.bot_and_db import bot
from function.bot_and_db.bot_and_db import db
from function.admin.ban_unban import *
from function.admin.stat_all import *
from function.admin.info_user import *
from function.admin.mailing import *
from keyboard import admin
from config import config

# Функция обработки команды /admin | Готово
def get_text_admin_admin(message):
	if message.from_user.id == config.admin_id:
		bot.send_message(message.from_user.id, "Аве админ", reply_markup=admin.btn_admin_menu)


# Функция обработки команды Stat | Готово
def get_text_admin_stat(message):
	if message.from_user.id == config.admin_id:

		load_cpu, load_mem = load_my_server()

		num_akk = num_akk_shop()

		nums_users = db.info_nums_user()

		bot.send_message(
			message.from_user.id,
			"[Общая статистика]" +
			"\nНагрузка ЦП: " + str(load_cpu) +
			"\nЗанято ОЗУ: " + str(load_mem) +
			"\nВсего пользователей: " + str(nums_users) +
			"\nАккаунтов на продаже: " + str(num_akk))


# Функция обработки команды User | Готово
def get_text_admin_user(message):
	if message.from_user.id == config.admin_id:
		bot.send_message(message.from_user.id, "Команды связаные с пользователями:", reply_markup=admin.btn_admin_user)


# Функция обработки команды Ban | Готово
def get_text_admin_ban(message):
	if message.from_user.id == config.admin_id:
		bot.send_message(message.from_user.id, "Пришлите id для бана:", reply_markup=admin.btn_admin_cancel)

		bot.register_next_step_handler(message, user_ban)


# Функция обработки команды Unban | Готово
def get_text_admin_unban(message):
	if message.from_user.id == config.admin_id:
		bot.send_message(message.from_user.id, "Пришлите id для разбана", reply_markup=admin.btn_admin_cancel)

		bot.register_next_step_handler(message, user_unban)


# Функция обработки команды Money
def get_text_admin_money(message):
	if message.from_user.id == config.admin_id:
		bot.send_message(message.from_user.id, "Пришлите id кому пополнить баланс", reply_markup=admin.btn_admin_cancel)


# Функция обработки команды Unmoney
def get_text_admin_unmoney(message):
	if message.from_user.id == config.admin_id:
		bot.send_message(message.from_user.id, "Пришлите id у кого снять деньги с баланса", reply_markup=admin.btn_admin_cancel)


# Функция обработки команды Mailing
def get_text_admin_mailing(message):
	if message.from_user.id == config.admin_id:
		bot.send_message(
			message.from_user.id,
			"Пришлите сообщение и оно будер отправленно всем пользователям",
			reply_markup=admin.btn_admin_cancel)

		bot.register_next_step_handler(message, mailing)


# Функция обработки команды Info | Готово
def get_text_admin_info(message):
	if message.from_user.id == config.admin_id:
		bot.send_message(message.from_user.id, "Укажите id для получения доп инфы о пользователе", reply_markup=admin.btn_admin_cancel)

		bot.register_next_step_handler(message, user_information)


# Функция обработки команды Shop
def get_text_admin_shop(message):
	if message.from_user.id == config.admin_id:
		bot.send_message(message.from_user.id, "Команды связаные с Магазином аккаунтов бота", reply_markup=admin.btn_admin_shop)


# Функция обработки команды Status
def get_text_admin_status(message):
	if message.from_user.id == config.admin_id:
		bot.send_message(
			message.from_user.id,
			"Статистика магазина:" +
			"\nВсего товаров: " +
			"\nКупленно: " +
			"\nНа продаже: ")


# Функция обработки команды Добавить
def get_text_admin_add(message):
	if message.from_user.id == config.admin_id:
		bot.send_message(message.from_user.id, "Пришлите архив с аккаунтами", reply_markup=admin.btn_admin_cancel)


# Функция обработки команды Удалить
def get_text_admin_del(message):
	if message.from_user.id == config.admin_id:
		bot.send_message(message.from_user.id, "Укажите номер аккаунта для удаления", reply_markup=admin.btn_admin_cancel)


# регестрируем наши финкции указывая для каждой команды свою функцию
def register_handler_admin(bot):
	bot.register_message_handler(get_text_admin_admin, commands=['admin'])

	bot.register_message_handler(get_text_admin_stat, regexp="Stat")
	bot.register_message_handler(get_text_admin_user, regexp="User")
	bot.register_message_handler(get_text_admin_shop, regexp="Shop")

	bot.register_message_handler(get_text_admin_ban, regexp="Ban")
	bot.register_message_handler(get_text_admin_unban, regexp="Unban")
	bot.register_message_handler(get_text_admin_money, regexp="Money")
	bot.register_message_handler(get_text_admin_unmoney, regexp="Unmoney")
	bot.register_message_handler(get_text_admin_mailing, regexp="Mailing")
	bot.register_message_handler(get_text_admin_info, regexp="Info")

	bot.register_message_handler(get_text_admin_status, regexp="Status")
	bot.register_message_handler(get_text_admin_add, regexp="Добавить")
	bot.register_message_handler(get_text_admin_del, regexp="Удалить")
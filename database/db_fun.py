import os
from config import config
import sqlite3

# класс взаимодействия с базой данных
class database_management():
	# Функция запускатся при старте
	def __init__(self):
		self._create_db_users()


	# Создаем базу пользователей db_1
	def _create_db_users(self):

		if config.status_os == "MAC":
			# Создаем базу users.db через обьект connect()
			self.db_1 = sqlite3.connect('users.db', check_same_thread=False)
		elif config.status_os == "Windows":
			# Создаем базу users.db через обьект connect()
			self.db_1 = sqlite3.connect('database\\users.db', check_same_thread=False)

		# cursor() позволяет делать sql запросы
		self.sql_1 = self.db_1.cursor()

		# Создаем таблицу если она не создана users - название таблицы
		self.sql_1.execute("""CREATE TABLE IF NOT EXISTS users (
		ID INT, 
		NAME TEXT, 
		LINK TEXT,
		BALANCE INT,
		IAGREE TEXT,
		BLACKL TEXT
		)""")

		# ID        - id пользователя
		# NAME      - имя
		# LINK      - @link
		# BALANCE   - баланс
		# IAGREE    - Согласие с правилами использования бота бота
		# BLACKL    - Наличие бана

		# Подтверждаем сохранение
		self.db_1.commit()

	# Создаем базу хранящую id, hash, num от аккаунта db_2
	def _create_db_account(self):
		pass


	# Проверить наличие пользователя в базе
	def check_the_user(self, user_id: int, user_name: str, user_link: str) -> bool:
		# Выбрать столбел ID в таблице users, где ID равен = user_login
		self.sql_1.execute(f"SELECT ID FROM users WHERE ID = '{user_id}'")

		# Если такого KEY нету в базе, то
		if self.sql_1.fetchone() is None:

			# Добавим запись в базу данных
			self.sql_1.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", (user_id, user_name, user_link, 0, 'False', 'False'))

			# подтвердим сохранение
			self.db_1.commit()

			if config.status_os == "MAC":
				path = "" + str(user_id)
			elif config.status_os == "Windows":
				path = "database\\users\\" + str(user_id)

			try:
				# создадим папку для еего фоток
				os.mkdir(path)
			except Exception:
				pass

			# Раньше его не было
			return False

		# Если ключ есть в базе
		else:
			# Раньше он был
			return True


	# Проверяем есть ли пользователь в базе
	def check_user_in_db(self, user_id):
		try:
			# Проверка наличия
			self.sql_1.execute(f"SELECT BLACKL FROM users WHERE ID = '{user_id}'")
			user_ban_status = self.sql_1.fetchone()[0]

			return "Good"
		except Exception:
			return "Error"

	# Поверка согласия с правилами
	def verification_of_consent(self, user_id: int) -> str:
		# Читаем IAGREE из таблицы users, где ID равн user_id
		self.sql_1.execute(f"SELECT IAGREE FROM users WHERE ID = '{user_id}'")
		user_iagree_status = self.sql_1.fetchone()[0]

		return user_iagree_status


	# Проверка наличия бана
	def checking_the_black_spike(self, user_id: int) -> str:
		# Читаем BLACKL из таблицы users, где ID равн user_id
		self.sql_1.execute(f"SELECT BLACKL FROM users WHERE ID = '{user_id}'")
		user_ban_status = self.sql_1.fetchone()[0]

		return user_ban_status


	# указываем что пользователь согласен с правилами
	def iagree(self, user_id: int) -> None:
		# Обновить в таблице users, добавить в столбце IAGREE новое значение, где столбец IAGREE равен = user_id
		self.sql_1.execute(f'UPDATE users SET IAGREE = "{True}" WHERE ID = "{user_id}"')
		# Подтвердили изменения
		self.db_1.commit()


	# Заблокировать пользователя
	def ban_user(self, user_id):
		try:
			# Проверка наличия
			self.sql_1.execute(f"SELECT BLACKL FROM users WHERE ID = '{user_id}'")
			user_ban_status = self.sql_1.fetchone()[0]

			# Обновить в таблице users, добавить в столбце BLACKL новое значение, где столбец ID равен = False
			self.sql_1.execute(f'UPDATE users SET BLACKL = "True" WHERE ID = "{user_id}"')
			self.db_1.commit()  # Подтвердили изменения

			return "Good"
		except Exception:
			return "Error"


	# Узнаем количество людей в базе
	def info_nums_user(self):
		# Читаем ID из таблицы users
		self.sql_1.execute(f"SELECT ID FROM users")
		nums = self.sql_1.fetchall()

		return len(nums)


	# Получаем список id всех пользователей из базы
	def list_user_id(self):
		# Читаем ID из таблицы users
		self.sql_1.execute(f"SELECT ID FROM users")
		nums = self.sql_1.fetchall()

		return nums

	# Получаем информацию о профиле
	def my_profil(self, user_id):
		try:
			# Читаем NAME из таблицы users, где ID равен user_id
			self.sql_1.execute(f"SELECT NAME FROM users WHERE ID = '{user_id}'")
			us_name = self.sql_1.fetchone()[0]

			# Читаем LINK из таблицы users, где ID равен user_id
			self.sql_1.execute(f"SELECT LINK FROM users WHERE ID = '{user_id}'")
			us_link = self.sql_1.fetchone()[0]

			# Читаем BALANCE из таблицы users, где ID равен user_id
			self.sql_1.execute(f"SELECT BALANCE FROM users WHERE ID = '{user_id}'")
			us_balance = self.sql_1.fetchone()[0]

			# Читаем BLACKL из таблицы users, где ID равен user_id
			self.sql_1.execute(f"SELECT BLACKL FROM users WHERE ID = '{user_id}'")
			us_st_black = self.sql_1.fetchone()[0]


			return us_name, us_link, us_balance, us_st_black
		except Exception:
			return "Error", "Error", "Error", "Error"


	# Разблокировать пользователя
	def unban_user(self, user_id):
		try:
			# Обновить в таблице users, добавить в столбце BLACKL новое значение, где столбец ID равен = False
			self.sql_1.execute(f'UPDATE users SET BLACKL = "False" WHERE ID = "{user_id}"')
			self.db_1.commit()  # Подтвердили изменения

			return "Good"
		except Exception:
			return "Error"


	# Узнаем количество людей в базе
	def info_nums_user(self):
		# Читаем ID из таблицы users
		self.sql_1.execute(f"SELECT ID FROM users")
		nums = self.sql_1.fetchall()

		return len(nums)


	# Получаем список id всех пользователей из базы
	def list_user_id(self):
		# Читаем ID из таблицы users
		self.sql_1.execute(f"SELECT ID FROM users")
		nums = self.sql_1.fetchall()

		return nums

	# Получаем информацию о профиле
	def my_profil(self, user_id):
		try:
			# Читаем NAME из таблицы users, где ID равен user_id
			self.sql_1.execute(f"SELECT NAME FROM users WHERE ID = '{user_id}'")
			us_name = self.sql_1.fetchone()[0]

			# Читаем LINK из таблицы users, где ID равен user_id
			self.sql_1.execute(f"SELECT LINK FROM users WHERE ID = '{user_id}'")
			us_link = self.sql_1.fetchone()[0]

			# Читаем BALANCE из таблицы users, где ID равен user_id
			self.sql_1.execute(f"SELECT BALANCE FROM users WHERE ID = '{user_id}'")
			us_balance = self.sql_1.fetchone()[0]

			# Читаем BLACKL из таблицы users, где ID равен user_id
			self.sql_1.execute(f"SELECT BLACKL FROM users WHERE ID = '{user_id}'")
			us_st_black = self.sql_1.fetchone()[0]


			return us_name, us_link, us_balance, us_st_black
		except Exception:
			return "Error", "Error", "Error", "Error"
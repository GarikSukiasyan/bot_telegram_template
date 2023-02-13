
from database import db_fun
from config import config
import telebot

# Создаем обьект бота
bot = telebot.TeleBot(config.token)

# Подключаем класс для работы с базой данных
db = db_fun.database_management()
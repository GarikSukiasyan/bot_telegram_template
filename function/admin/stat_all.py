import psutil
import os.path

# Узнаем нагрузку ЦП и Оперативки
def load_my_server():
	load_cpu = psutil.cpu_percent(interval=1)
	load_mem = psutil.virtual_memory().percent

	return load_cpu, load_mem


# узнать количество аккаунтов на продаже
def num_akk_shop():
	path = 'shop'
	num_akk = len([f for f in os.listdir(path)
	                 if os.path.isfile(os.path.join(path, f))])

	if int(num_akk) != 0:
		num_akk = int(num_akk) / 2

	return int(num_akk)

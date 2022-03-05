from time import sleep
import os

name = input('Введите название файла который хотите создать или изменить: ')

os.system('cls' if os.name == 'nt' else 'clear')

sleep(2)





while True:
	print('File Writer By KarasTipoNoNet')
	print('Нажмите ENTER для записи строки в файл')

	text = input('Введите текст который хотите записать: ')

	file = open(f'{name}.txt', 'a')
	file.write(text + '\n')
	file.close()

	print('Строка записана!')

	sleep(2)

	os.system('cls' if os.name == 'nt' else 'clear')

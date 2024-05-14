import os

pattern = str(input('Введите шаблон наименования папок: '))
first_num = int(input('Введите номер первой папки: '))
last_num = int(input('Введите номер последней папки: '))

if first_num <= last_num:
    while first_num <= last_num:
        try:
            os.mkdir(f'{pattern}{first_num}')
        except FileExistsError:
            print(f'Директория {pattern}{first_num} уже существует.')
        first_num += 1

else:
    while first_num >= last_num:
        try:
            os.mkdir(f'{pattern}{last_num}')
        except FileExistsError:
            print(f'Директория {pattern}{last_num} уже существует.')
        last_num += 1
pattern = input('Создание завершено. Нажмите ENTER, чтобы закрыть программу.')

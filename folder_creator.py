import os

pattern = str(input('Введите шаблон наименования папок: '))
first_num = int(input('Введите номер первой папки: '))
last_num = int(input('Введите номер последней папки: '))

if first_num <= last_num:
    while first_num <= last_num:
        os.mkdir(f'{pattern}{first_num}')
        first_num += 1

else:
    while first_num >= last_num:
        os.mkdir(f'{pattern}{last_num}')
        last_num += 1
pattern = input('Создание завершено. Нажмите ENTER, чтобы закрыть программу')

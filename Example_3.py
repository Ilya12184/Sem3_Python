# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

import sys

quarter = int(input('Введите число от 1 до 4 - номер четверти: '))

if 0 < quarter < 5:
    if quarter == 1:
        print(f'x = (0 : {sys.maxsize}), y = (0 : {sys.maxsize})')

    elif quarter == 2:
        print(f'x = (0 : {-sys.maxsize - 1}), y = (0 : {sys.maxsize})')

    elif quarter == 3:
        print(f'x = (0 : {-sys.maxsize - 1}), y = (0 : {-sys.maxsize - 1})')

    elif quarter == 4:
        print(f'x = (0 : {sys.maxsize}), y = (0 : {-sys.maxsize - 1})')
else:
    print('Ошибка ввода!')
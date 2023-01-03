# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

number = (input("Введите вещественное число: "))

if float(number) < 0:
    x = float(number) * (-1)

summ = 0
for i in str(number):
    if i != '.':
        summ += int(i)
print(f'Сумма цифр числа = {summ}')
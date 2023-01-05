# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input('Введите число: '))
lst = []
first = 0
entry = ''

while number != 1 and number != 0:
    digit = number % 2
    number = number//2
    lst.append(digit)

lst.reverse()
first = number

for num in lst:
    entry = entry + str(num)
print(str(first)+entry)

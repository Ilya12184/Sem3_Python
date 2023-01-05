# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

lst = list(map(float, input('Введите список через пробел: ').split()))
lst2 = []
print(lst)

for number in lst:
    value = round(number - (int(number)), 15)
    lst2.append(value)
result = round(max(lst2)-min(lst2), 15)

print(result)
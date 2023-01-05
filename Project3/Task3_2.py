# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst = list(map(int, input('Введите список через пробел: ').split()))
lst2 = []
prod = 0

if len(lst) % 2 == 0:
    volume = len(lst)//2
else:
    volume = len(lst)//2+1

for ind in range(volume):
    if ind != len(lst)//2:
        prod = lst[ind]*lst[-(ind+1)]
        lst2.append(prod)
    else:
        prod = lst[ind]**2
        lst2.append(prod)
print(lst2)
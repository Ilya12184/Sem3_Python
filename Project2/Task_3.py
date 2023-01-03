# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input('Введите n: '))
#form = 0
lst = []

for i in range(1, n+1):
    form = (1 + 1/i) ** i
    lst.append(form)
print("Сумма: "'{0:.2f}'.format(sum(lst)))

"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
 В последующих  строках записаны N целых чисел Ai.
 Последняя строка содержит число X
*Пример:*   5    1 2 3 4 5    6    -> 5
"""

import random
n = int(input("Введите количество элементов в массиве: "))
x = int(input("Введите число для поиска "))
my_list = [random.randint(1, 99) for i in range(n)]
print(my_list)
index_el = 0
min_el = abs(x - my_list[0])
for i in range(1, n):
    diff_value = abs(x - my_list[i])
    if diff_value < min_el:
        min_el = diff_value
        index_el = i
print(f"Самый близкий по значению элемент к заданному числу {my_list[index_el]}")

'''
# или вариант без random
n = abs(int(input('Введите количество элементов в массиве: ')))
i = 0
Ai = []
for i in range(n):
    dig = input("Введите одно целое число: ")
    Ai.append(dig)
my_list = list(map(int, Ai))
print(my_list)
x = int(input("Введите число для поиска "))
index_el = 0
min_el = abs(x - my_list[0])
for i in range(1, n):
    diff_value = abs(x - my_list[i])
    if diff_value < min_el:
        min_el = diff_value
        index_el = i
print(f"Самый близкий по значению элемент к заданному числу {my_list[index_el]}")
'''
# Пользователь вводит размер массива – N
# и элементы массива (целые числа).
# (пользовательский ввод можно заменить на рандомный)
# нужно посчитать сколько повторений у каждого числа
# посчитанные числа можно посчитать повторно
# в паре с другими числами
# Ввод: 1 2 3 2 3 2
# Вывод: 4


import random


def find_dubli_1(tuple_a: tuple) -> int:
    count = 0
    for i in range(len(tuple_a)-1):
        for j in range(i + 1, len(tuple_a)):
            if tuple_a[i] == tuple_a[j]:
                count += 1
    return count


# 2 Вариант


def find_dubli_2(tuple_a: tuple) -> int:
    count = 0
    for i in range(len(tuple_a) - 1):
        count += tuple_a[i + 1:].count(tuple_a[i])
    return count


num = int(input("Укажите размер массива: "))
tuple_1 = tuple(random.randint(1, 10) for i in range(num))
print(tuple_1)
print(find_dubli_1(tuple_1))
print(find_dubli_2(tuple_1))

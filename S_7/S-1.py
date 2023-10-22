# Даны два массива чисел. 
# Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), 
# которых нет во втором массиве. Пользователь вводит число 
# N - количество элементов в первом массиве, 
# затем N чисел- элементы массива. 
# Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# Вывод:
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)


import random
import time


def generate_list(num: int) -> list[int]:
    # list_res = []
    # for _ in range(num):
    #     list_res.append(random.randint(1, 15))
    return [random.randint(1, 100000) for _ in range(num)]

def find_list_1(lst_a: list, lst_b: list) -> list[int]:
    set_b = set(lst_b)
    list_res = []
    for el in lst_a:
        if el not in set_b:
            list_res.append(el)
    return list_res

#  2 вариант функции

def find_list_2(lst_a: list, lst_b: list) -> list[int]:
    set_b = set(lst_b)
    return [el for el in lst_a if el not in set_b]

# 3 вариант функции

def find_list_3(lst_a: list, lst_b: list):
    set_b = set(lst_b)
    for i in range(len(lst_a)-1, -1, -1):    # [:: - 1]:
        if lst_a[i] in set_b:
            del lst_a[i]


list1_size = int(input("Введите число: "))
list_1 = generate_list(list1_size)
# print(list_1)

list2_size = int(input("Введите число: "))
list_2 = generate_list(list2_size)
# print(list_2)

start_time_1 = time.time()
print(find_list_1(list_1, list_2))
finish_time_1 = time.time()
data_time_1 = finish_time_1 - start_time_1
print(f"{data_time_1 = }")



start_time_2 = time.time()
print(find_list_2(list_1, list_2))
finish_time_2 = time.time()
data_time_2 = finish_time_2 - start_time_2
print(f"{data_time_2 = }")



start_time_3 = time.time()
find_list_3(list_1, list_2)
print(*list_1)
finish_time_3 = time.time()
data_time_3 = finish_time_3 - start_time_3
print(f"{data_time_3 = }")
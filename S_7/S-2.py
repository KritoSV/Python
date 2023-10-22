# 2) (пользовательский ввод можно заменить на рандомный)
# Пользователь вводит размер массива – N
# и элементы массива (целые числа).
# нужно из этого массива вывести количество элементов, 
# у которых ближайшие соседние элементы меньше самого элемента.
# Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод:
# 0 2


import random


def generate_arr(num: int) -> tuple[int]:
    # list_res = []
    # for _ in range(num):
    #     list_res.append(random.randint(1, 15))
    return tuple(random.randint(1, 15) for _ in range(num))



def find_count_1(tuple_a: tuple) -> int:
    count = 0
    for i in range(1, len(tuple_a)-1):
        if tuple_a[i] > tuple_a[i-1] and tuple_a[i] > tuple_a[i+1]:
            count += 1
    return count


# 2 Вариант 

def find_count_2(tuple_a: tuple) -> int:
    count = 0
    for i in range(1, len(tuple_a)-1):
        if tuple_a[i] > tuple_a[i-1] and tuple_a[i] > tuple_a[i+1]:
            count += 1
    return sum([1 for i in range(1, len(tuple_a)-1) if tuple_a[i] > tuple_a[i-1] and tuple_a[i] > tuple_a[i+1]])


list1_size = int(input("Введите число: "))
tuple_1 = generate_arr(list1_size)
print(tuple_1)
print(find_count_1(tuple_1))

print(find_count_2(tuple_1))
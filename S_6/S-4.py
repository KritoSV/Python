# Дано натуральное число N и последовательность 
# из N элементов. Требуется вывести эту 
# последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять 
# массивы и использовать циклы (даже для ввода и вывода).
# Input:    2 -> 3 4
# Output: 4 3

# def revers_nums(count_nums):
#     if count_nums == 0:
#         return ''
#     k = input("Введите число: ")
#     return revers_nums(count_nums - 1) + ' ' + k

# nums = int(input("Введите количество чисел: "))
# print(revers_nums(nums))


# 2


def revers_nums(count_nums):
    if count_nums == 1:
        k = input('Введите число: ')
        return  k + ' '
    k = input('Введите число: ')
    return  revers_nums(count_nums - 1) + k + ' '

nums = int(input('Введите количество чисел: '))
print(revers_nums(nums))

# Доп. задача.

import time
import random

def max_to_min1(arr):
    set_arr = set(arr)
    min_arr = min(set_arr)
    max_arr = max(set_arr)
    return [min_arr if num == max_arr else num for num in arr]


def max_to_min2(arr):
    min_arr = arr[0]
    max_arr = arr[0]
    max_index = [0]
    for i in range(1, len(arr)):
        if arr[i] > max_arr:
            max_arr = arr[i]
            max_index = [i]
        elif arr[i] == max_arr:
            max_index.append(i)
        if arr[i] < min_arr:
            min_arr = arr[i]
    for i in max_index:
        arr[i] = min_arr


n = int(input('Введите количество оценок: '))
nums1 = [random.randint(1, 5) for num in range(n)]
nums2 = nums1.copy()


start1 = time.time()
max_to_min1(nums1)
end1 = time.time()
time1 = end1 - start1


start2 = time.time()
max_to_min2(nums2)
end2 = time.time()

print(time1)
print(end2 - start2)
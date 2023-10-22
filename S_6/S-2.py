# Хакер Василий получил доступ к классному 
# журналу и хочет заменить все свои минимальные 
# оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# import random

# def max_to_min(arr):
#     min_arr = min(arr)
#     max_arr = max(arr)
#     return [min_arr if num == max_arr else num for num in arr]



# n = int(input("Введите количество оценок: "))
# nums = []


# for nums in range(n):
#     nums.append(random.randint(1, 5))
# print(nums)

# nums = [random.randint(1, 5) for num in range(n)]

# print(nums)
# print(max_to_min(nums))



# 2

import random

def max_to_min(arr):
    min_arr = arr[0]
    max_arr = arr[0]
    max_index = [0]
    for i in range(len(arr)):
        if max_arr < arr[i]:
            max_arr = arr[i]
            max_index = [i]
        elif arr[i] == max_arr:
            max_index.append(i)
        if arr[i] < min_arr:
            min_arr = arr[i]
    for i in max_index:
        arr[i] = min_arr



n = int(input("Введите количество оценок: "))
nums = []


nums = [random.randint(1, 5) for num in range(n)]

print(nums)
max_to_min(nums)
print(nums)

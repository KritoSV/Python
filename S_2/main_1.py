# Дано натуральное число A > 1. 
# Определите, каким по счету числом 
# Фибоначчи оно является, то есть выведите 
# такое число n, что φ(n)=A. Если А не является 
# числом Фибоначчи, выведите число -1.

# Input:     5
# Output:  6
# Ряд чисел Фибоначчи:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 
# 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …

# f_res = int(input("Введите натуральное число > 1: "))
# f1 = 1
# f2 = 2
# i = 4
# while f2+f1 <= f_res:
#     f = f1 + f2
#     f1 = f2
#     f2 = f
#     # f1, f2 = f2, f1+f2
#     i += 1
# print(i)



# 2) Пользователь вводит число N (1 ≤ N ≤ 10). 
# Далее построчно N чисел от -50 до 50. 
# Нужно вывести наибольшее количество идущих 
# подряд положительных чисел.

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2

# import random

# n = int(input("Введите число "))

# max_pos_num = 0
# count = 0
# for i in range(n):
#     num = random.randint(-50, 50)
#     print(num, end=" ")
#     if num > 0:
#         count = count+1
#         # max_pos_num = max(max_pos_num, count)
#         if max_pos_num < count:
#             max_pos_num = count
#     else:
#         count = 0

# print(max_pos_num)



# 2) Пользователь вводит одно число N.  
# Далее идут N чисел, записанных на новой 
# строчке каждое. Вывести максимальное 
# и минимальное (циклы)
# Input:    5 -> 5 1 6 5 9
# Output:    1 9

# import random

# n = int(input("Введите число: "))
# max_num = 1
# min_num = 1000000
# for i in range(n):
#     num = random.randint(1, 20)
#     print(num, end=" ")
#     if num < min_num:
#         min_num = num
#     if num>max_num:
#         max_num=num
# print()
# print(f'минимальное число {min_num}\nмаксимальное число {max_num}')

# /2 вариант.
# import random

# n = int(input("Введите число: "))
# num = random.randint(1, 20)
# max_num = num
# minnum = num
# print(num, end=" ")
# for  in range(n-1):
#     num = random.randint(1, 20)
#     print(num, end=" ")
#     if num < min_num:
#         min_num = num
#     if num>max_num:
#         max_num=num
# print()
# print(f'минимальное число {min_num}\nмаксимальное число {max_num}')





# На столе лежат n монеток. Некоторые из монеток 
# лежат вверх решкой, а некоторые – гербом. Ваша 
# задача - определить минимальное количество монеток, 
# которые нужно перевернуть, чтобы все монетки лежали 
# одной и той же стороной вверх.
# Входные данные:
# На вход программе подается список coins, 
# где coins[i] равно 0, если i-я монетка лежит гербом вверх, 
# и равно 1, если i-я монетка лежит решкой вверх. 
# Размер списка не превышает 1000 элементов.
# Выходные данные:
# Программа должна вывести одно целое число - 
# минимальное количество монеток, которые нужно перевернуть.
# Пример использования На входе:
# coins = [0, 1, 0, 1, 1, 0]
# На выходе:
# 3

# import random

# coins = []

# for _ in range(6):
#     coins.append(random.randint(0, 1))
# print(coins)

# mininmum = min(coins.count(0), coins.count(1))
# print(mininmum)

# Второе решение...

# count_zero = 0
# count_one = 0

# for coin in coins:
#     if coin == 0:
#         count_zero += 1
#     else:
#         count_one += 1

# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)




# Требуется вывести все целые 
# степени двойки (т.е. числа вида 2k), 
# не превосходящие числаN.
# Пример
# n = 16
# Вывод
# 1
# 2
# 4
# 8
# 16


# n = 2021515812
# num = 1
# while num <= n:
#     print(num)
#     num *= 2

# Второе решение...

# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1



# Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X, Y ≤ 1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# Примечание: числа S и P задавать не нужно,
# они будут передаваться в тестах. В результате
# вы должны вывести все возможные варианты чисел X и Y через пробел.
# Пример
# На входе:
# s = 12
# p = 27
# На выходе:
# 3 9
# 9 3

# import time
# start_time = time.perf_counter()

# from math import sqrt

# x = 2000
# y = 1000 * 1000

# D = x*x + 4*(-y)  
# if D >= 0:  
#     x1 = int((x - sqrt(D)) / 2)
#     x2 = int((x + sqrt(D)) / 2)

# print(x1, x2)
# if x1 != x2:
#     print(x2, x1)

# end_time = time.perf_counter()

# print(end_time - start_time)



# Второй вариант...

# import time
# start_time = time.time()

# s = 2000
# p = 1000 * 1000

# for i in range(s):
#     for j in range(p):
#         if s == i + j and p == i * j:
#             print(i, j)

# end_time = time.time()

# elapsed_time = end_time - start_time
# print('Разница между стартом и концом: ', elapsed_time)

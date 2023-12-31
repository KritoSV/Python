# Черника
# Ваша задача - написать программу, которая определит 
# максимальное число ягод, которое может собрать один 
# собирающий модуль за один заход, находясь перед некоторым кустом грядки.
# Входные данные:
# На вход программе подается список arr, 
# где arr[i] (1 ≤ arr[i] ≤ 1000) 
# - урожайность i-го куста черники. 
# Размер списка не превышает 1000 элементов.
# Выходные данные:
# Программа должна вывести одно целое число 
# - максимальное количество ягод, которое может 
# собрать собирающий модуль, 
# находясь перед некоторым кустом грядки.
# На входе:
# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# На выходе:
# 19

arr = [5, 8, 6, 4, 9, 2, 7, 3]

sum_ = []
for i in range(len(arr)):
    sum_.append(arr[i] + arr[i - 1] + arr[(i + 1) % len(arr)])
print(sum_)
print(max(sum_))

sum_ = set()
for i in range(len(arr)):
    sum_.add(arr[i] + arr[i - 1] + arr[(i + 1) % len(arr)])
print(sum_)
print(max(sum_))

# Этанол

arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])

# Вывод максимальной урожайности, которую может собрать собирающий модуль
print(max(arr_count))

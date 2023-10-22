# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]
# Примечание: Пользователь может вводить 
# значения списка или список задан изначально.

# list_1 = [1, 2, 3, 4, 5] 
# k = int(input("Введите число на которое необходимо сделать сдвиг: ")) %len(list_1)
# # k = 1 -> [5, 1, 2, 3, 4] list_1[-1:] + list_1[:-1]
# # k = 2 -> [4, 5, 1, 2, 3] list_1[-2:] + list_1[:-2]

# print(list_1[-k:] + list_1[:-k])

# from random import randint
# k = randint(1, 50)
# size = randint(5, 10)
# arr_1 = []
# for i in range(size):
#     arr_1.append(randint(1,100))
# arr_2 = [randint(1,100) 
#          for i in range(size)
#         ]
# print(arr_1)
# print(arr_2)
# print(k)
# print(size)
# k = k % len(arr_1)

# print(arr_1[-k : ] + arr_1[ : -k])
# print(arr_2[-k : ] + arr_2[ : -k])


# list_1 = [1, 2, 3, 4, 5] 
# k = int(input("Введите коэфицент сдвига: ")) %len(list_1)
# for i in range(k):
#     list_1 = [list_1[-1]] + list_1[:-1]
# print(list_1)

list_1 = [1, 2, 3, 4, 5] 
k = int(input("Введите коэфицент сдвига: ")) %len(list_1)
for i in range(k):
    last_num = list_1.pop()
    list_1.insert(0, last_num)
print(list_1)
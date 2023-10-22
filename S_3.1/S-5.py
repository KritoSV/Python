# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая подсчитает 
# количество элементов массива, больших 
# предыдущего (элемента с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 
# Пояснение: (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить 
# значения списка или список задан изначально.

# list_1 = [0, -1, 5, 2, 3]
# count = 0
# for i in range(len.list_1):
#     if list_1[i] < list_1[i + 1]:
#         count += 1
# print(count)


from random import randint

# list_1 = [0, -1, 5, 2, 3]
size = int(input("Введите количество элементов: "))
list_1 = [randint(-10, 10) for i in range(size)]
print(list_1)
count = 0
for i in range(len(list_1) - 1):
    if list_1[i] < list_1[i + 1]:
        count += 1
print(count)

list_2 = [1 for i in range(len(list_1) - 1) if list_1[i] < list_1[i + 1]]
print(list_2)
print(sum(list_2))


list_3 = [1 if list_1[i] < list_1[i + 1] else 0 for i in range(len(list_1) - 1)]

print(list_3)

list_4 =[
    4 if list_1[i] % 4 == 0 
    else 2 if list_1[i] % 2 == 0 
    else 1 
    for i in range(len(list_1) - 1)
    ]

print(list_4)






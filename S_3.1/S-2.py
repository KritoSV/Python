# Дан список чисел. Определите,
# сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить
# значения списка или список задан изначально.

# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# list_2 = []

# for num in list_1:
#     if num not in list_2:  # Если нет повторяющегося элемента num в list_2
#         list_2.append(num)  # Функция .append() добавляет num в конец списка.

# print(len(list_2))

# print(len(set(list_1)))

from random import randint
n = int(input('Введите количество чисел: '))
arr = []
for i in range(n):
    arr.append(randint(-100,100))
print(arr)
print(f'В массиве {len(set(arr))} уникальных чисел')
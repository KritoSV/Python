# Встречаемость элемента в массиве
# Инструкция по использованию платформы
# Требуется вычислить, сколько раз 
# встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# Пример:

from random import randint
k = 3
list_1 = [randint(1, 5) for i in range(10)]
print(list_1)
print(list_1.count(k))

# Этанол.....

count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)
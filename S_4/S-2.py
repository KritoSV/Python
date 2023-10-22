# Ближайший элемент в массиве
# Инструкция по использованию платформы
# Требуется найти в массиве list_1 самый 
# близкий по величине элемент к заданному 
# числу k и вывести его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5



# from random import randint
# k = 3
# list_1 = [randint(1, 5) for i in range(5)]
# print(list_1)
# max_num = 0
# for i in range(len(list_1)):
#    if list_1[i] - k 

# print(max(filter(lambda x: x < k, list_1), default=None))
# print(min(filter(lambda x: x > k, list_1), default=None))




from random import randint

list_1 = [randint(1, 10) for i in range(5)]
print(list_1)
k = 6
num_1 = list_1[0]
min_num = abs(list_1[0] - k)
for i in range(1, len(list_1)):
   if abs(list_1[i] - k) < min_num:
      min_num = abs(list_1[i] - k)
      num_1 = list_1[i]
print(num_1)

# Этанол....

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)
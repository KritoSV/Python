# Напишите функцию same_by(characteristic, objects), 
# которая проверяет, все ли объекты имеют одинаковое 
# значение некоторой характеристики, и возвращают True, 
# если это так. Если значение характеристики для разных 
# объектов отличается - то False. Для пустого набора объектов, 
# функция должна возвращать True. Аргумент characteristic - 
# это функция, которая принимает объект и вычисляет его характеристику.
# Ввод
# values = [1, 3, 11, 7]
# if same_by(lambda x: x % 2, values):
# 	print(‘same’)
# else:
# 	print(‘different’)
# Вывод:
# same


# 1
def same_by_1(charact, obj: list()) -> bool:
	list_res = list(filter(charact, obj))
	print(list_res, obj == list_res)
	return obj == list_res and len(list_res) == 0

values = [0, 2, 6, 10]
# values = [1, 3, 11, 7]
if same_by_1(lambda x: x % 2 == 0, values):
	print('same')
else:
	print('different')


# 2
def same_by_2(charact, obj: list()) -> bool:
	list_res = list(map(charact, obj))
	print(list_res, obj == list_res)
	return obj == list_res and len(list_res) == 0

values = [0, 2, 6, 10]
# values = [1, 3, 11, 7]
if same_by_2(lambda x: x % 2 == 0, values):
	print('same')
else:
	print('different')


# 3
def same_by_3(charc, obj: list) -> bool:
    list_res = list(map(charc, obj))
    # first_el = list_res[0]
    # for el in list_res[1:]:
    #     if first_el!=el:
    #         return False
    # return True
    return all(list_res) == any(list_res)

values = [0, 2, 6, 10]
if same_by_3(lambda x: x % 2 == 0, values):
    print("same")
else:
    print('different')


# 4
def same_by_4(charact, obj):
    objects_new = list(filter(charact, obj))
    print(objects_new)
    return obj == objects_new
values = ["03q", "w4i", "10d", "odt"]
if same_by_4(lambda x: len(x) == 3, values):
    print("same")
else:
    print("different")
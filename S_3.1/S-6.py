import copy

list_1 = [1, 2, 3, 4, 5, [111, 222, 333, [11, 22, 33, 44]]] 
print(f'{list_1=}')
# list_2 = list_1
# print(f'{list_2=}')
# list_2[0] = 0
# print(f'{list_1=}')
# print(f'{list_2=}')

# list_3 = list_1.copy()
# # list_4 = list_1[:]
# list_3[3] = 999
# print(f'{list_1=}')
# print(f'{list_3=}')
# list_3[-1][1] = '***'

# print(f'{list_1=}')
# print(f'{list_3=}')

list_5 = copy.deepcopy(list_1)
list_5[3] = 999
print(f'{list_1=}')
print(f'{list_5=}')
list_5[-1][-1][2] = '***'
print(f'{list_1=}')
print(f'{list_5=}')

12:21
list_1 = [1, 2, 3, 4, 5] 
set_1 = set(list_1)
num = 999
list_new = [111, 222, 333] 
text = 'Python'
list_1.append(num)
print(f'{list_1=}')
list_1.append(list_new)
print(f'{list_1=}')
list_1.append(text)
print(f'{list_1=}')
print()
list_2 = [1, 2, 3, 4, 5] 
print(f'{list_2=}')
list_2.extend(list_new)
print(f'{list_2=}')
list_2.extend(text)
print(f'{list_2=}')

set_1 = {1, 2, 3, 4, 5}
num = 999
tuple_new = (111, 222, 333) 
tuple_new_2 = (111, 222, 333, [123,234,3456]) 
tuple_new_2[-1][-1] = 9999
text = 'Python'
set_1.add(num)
print(f'{set_1=}')
set_1.add(tuple_new)
print(f'{set_1=}')
set_1.add(text)
print(f'{set_1=}')
print()
set_2 = {1, 2, 3, 4, 5} 
print(f'{set_2=}')
set_2.update(tuple_new)
print(f'{set_2=}')
set_2.update(text)
print(f'{set_2=}')
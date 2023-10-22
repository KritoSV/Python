# Напишите программу для печати всех уникальных значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит

# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# set_1 = set()
# for item in list_1:
#     set_1.update(item.values())
# print(set_1)



list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
{"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
set_1 = set()
for item in list_1:
    set_1 = set_1.union(set(item.values()))
print(set_1)


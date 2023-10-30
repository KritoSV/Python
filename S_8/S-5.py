# print_operation_table
# Напишите функцию print_operation_table(operation, num_rows, num_columns), 
# которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают 
# число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.
# Пример
# На входе:
# print_operation_table(lambda x, y: x * y, 3, 3)
# На выходе:
# 1 2 3
# 2 4 6 
# 3 6 9


# 1
def print_operation_table(operation, num_rows, num_columns):

    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    a[0] = [i for i in range(1, num_columns +1)] 
    num = 1
    for el in a:
        el[0] = num
        num += 1
    if num_columns < 2 or num_rows < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    else:
        for i in a:
            print(*[f"{x: }" for x in i])

print_operation_table(lambda x, y: x / y, 4, 4)



# Этанол

def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))


print_operation_table(lambda x, y: x / y, 4, 4)

# Задача № 1

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = list()

for i in data:
    if i % 2 == 0:
        res.append((i, i**2))

print(res)


# Вариант 2

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

print(res)

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
res = where(lambda x: x % 2 == 0, res)

print(res)

res = list(select(lambda x:(x, x**2), res))
print(res)


# //////////////////////////////////


# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# /////////////////////////

data = '15 156 96 3 5 8 52 5'
print(data)

data = data.split()
print(data)

data = '15 156 96 3 5 8 52 5'
print(data)

data = list(map(int, data.split()))
print(data)

# ///////////////////////////////

data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)

# import random


# numbers = []

# for _ in range(1000):
#     Nums = random.randint(0, 50)
#     while Nums in numbers:
#           Nums = random.randint(0, 50)
#     numbers.append(Nums)

# print(numbers)

# print(sorted(numbers)[:: - 1])

# print(reversed(sorted(numbers)))


# n = int(input("Приветствую тебя Повелитель, Прошу, Введи число: "))
# prim = int(input("Повелитель, Нам Необходимо больше цифр: "))
# res = ""
# while n:
#     res = str(n % prim) + res
#     n //= prim
# print(res)
# print(int(res, prim))

# На вход алгоритма подаётся натуральное число N.
# Алгоритм строит по нему новое число R следующим образом.
# 1)Строится двоичная запись числа N.
# 2)К этой записи дописываются справа ещё два разряда по следующему правилу:
# а)складываются все цифры двоичной записи, и остаток от деления суммы на 2
# дописывается в конец числа (справа).
# Например, запись 11100 преобразуется в запись 111001;
# б)над этой записью производятся те же действия —
# справа дописывается остаток от деления суммы цифр на 2.
# Полученная таким образом запись (в ней на два разряда больше,
# чем в записи исходного числа N) является двоичной записью искомого числа R.
# Укажите минимальное число R, которое превышает 43
# и может являться результатом работы алгоритма.
# В ответе это число запишите в десятичной системе.


# for n in range(1, 100):
#     r = bin(n)[2:]
#     if r.count("1") % 2 == 0:
#         r += "00"
#     else:
#         r += "10"
#     r = int(r, 2)
#     if r > 43:
#         print(r)
#         break
# # 46


# n = 1

# while True:
#     r = bin(n)[2:]
#     if r.count("1") % 2 == 0:
#         r += "00"
#     else:
#         r += "10"
#     r = int(r, 2)
#     if r > 43:
#         print(r)

#         break
#     n += 1

# numbers = []

# for _ in range(1):
#     Nums = random.randint(0, 100)
#     while Nums in numbers:
#           Nums = random.randint(0, 100)
#     numbers.append(Nums)

# import random

# flag = True
# a = random.randrange(1, 100)
# b = random.randrange(1, 100)
# exitit = input("Хочешь выйти? -> ")
# while exitit == "нет":
#     print(f"Здравствуй, давай решать задачи: Ввдети сумму {a} + {b} -> ")
#     if int(input()) == a + b:
#         print("Ты молодец!")
#         a = random.randrange(1, 100)
#         b = random.randrange(1, 100)
#         exitit = input("Хочешь выйти? ->")
#     else:
#         print("Это не правильный ответ.")




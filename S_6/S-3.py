# Напишите функцию, которая принимает одно 
# число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, 
# которое имеет 2 делителя: 1  и n(само число)
# Input: 5
# Output: yes

# def is_prime_number(num):
#     for div in range(2, num ** 0,5 + 1):
#         if num % div == 0:
#             return "no"
#     return "yes"

# number = int(input("Введите число: "))
# print(is_prime_number(number))


# 2

def is_prime_number(num):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 and num not in (2, 3, 5, 7):
        return "no" 
    for div in range(3, int(num ** 0.5) + 1, 2):
        if num % div == 0:
            return "no"
    return "yes"


number = int(input("Введите число: "))
print(is_prime_number(number))

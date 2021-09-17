# 1(1) задание
# Функция, которая принимает 1 аргумент - номер месяца и возвращает
# название сезона, к которому относится этот месяц
# def month_to_season(number):
#     if number == 12:
#         print('Зима')
#     elif number == 1:
#         print('Зима')
#     elif number == 2:
#         print('Зима')
#     elif number == 3:
#         print('Весна')
#     elif number == 4:
#         print('Весна')
#     elif number == 5:
#         print('Весна')
#     elif number == 6:
#         print('Лето')
#     elif number == 7:
#         print('Лето')
#     elif number == 8:
#         print('Лето')
#     elif number == 9:
#         print('Осень')
#     elif number == 10:
#         print('Осень')
#     elif number == 11:
#         print('Осень')
#     else:
#         print('Неверно введен номер месяца')
#
#
# number = int(input('Введите номер месяца:'))
# month_to_season(number)

# ------------------------- METHOD1-----------------------------

# 1(2) задание
# month = 0
#
#
# def month_to_season():
#     month = int(input('Введите номер месяца:'))
#     print(month)
#     season = {'Зима': (1, 2, 12), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
#
#     for i in season.keys():
#         if month in season[i]:
#             return i
#
#
# print(month_to_season())

# ------------------------- METHOD1-----------------------------

# 2 задание
# def bank(A, years):
#
#     for i in range(years):
#         A = A + A * 0.1
#     return A
#
#
# A = int(input('Введите сумму:'))
# years = int(input('Введите срок вложения:'))
#
# print(bank(A, years))

# ------------------------- METHOD1-----------------------------

# 3 задание
import string
import random


def encrypt(str_1):
    letters = string.ascii_letters
    print(letters)
    new_string = ''
    key = tuple()
    for i in str_1:
        index = letters.index(i)
        random_number = random.randint(3, 5)
        new_string += letters[index + random_number]
        key += (random_number, )
    return new_string, key


def decrypt(str_2, key):
    letters = string.ascii_letters
    new_string = ''
    for n, i in enumerate(str_2):
        new_string += letters[letters.index(i) - int(key[n])]
    return new_string


a = encrypt(input('Введите строку для шифрования:'))
print(a[0], a[1])
s0 = input('Строка для дешифровки: ')
s1 = input('ключ: ').split()
print(s1)
print(decrypt(s0, s1))





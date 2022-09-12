from tkinter import *
from decimal import *
# Tkinter для графического интерфейса;
# Decimal для вычислений с большей точность, так как точности float не достаточно.


def calculate(x, a, y):
    if a == '+':
        return x + y
    elif a == '-':
        return x - y
    elif a == '*':
        return x * y
    elif a == '/':
        return x / y


# def addition(x, y):
#     return x + y
#
#
# def subtraction(x, y):
#     return x - y
#
#
# def multiplication(x, y):
#     return x * y
#
#
# def division(x, y):
#     return x / y

# z
buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )
# кортеж с кнопками. Кортеж использую, потому что нужны неизменные числа.

while True:
    try:
        print('Введите выражение')
        string = input()
        s = string.split(' ')
        print('Ответ', calculate(float(s[0]), s[1], float(s[2])))
    except Exception as e:
        print('Ошибка ввода', e)

#  Цикл, с обработкой ошибки
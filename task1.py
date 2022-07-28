# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input("Введите вещественное число: ")

def Calc(n):
    n = str(n).replace(',', '')
    sum=0
    for i in n:
        sum = int(sum) + int(i)
    return sum

print (Calc(number))


# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input("Введите первый элемент арифметической прогрессии: "))
d = int(input("Введите шаг арифметической прогрессии: "))
n = int(input("Введите количество членов арифметической прогрессии: "))

def Arith():
    ArProg = []
    for i in range(n):
        if i == 0:
            ArProg.append(a)
        else:
            ArProg.append(ArProg[i-1]+d)
    print(ArProg)
Arith()
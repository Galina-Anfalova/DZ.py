'''Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
превосходящие числа N.'''

a = int(input())
count = 0
while a ** count <= a:
    print(a ** count)
    count += 1
# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N

number = int(input('введите число: '))
k = 1
while number > k:
    print(k,  end=' ')
    k = k * 2

# 2: Написать функцию, которая возвращает первые три символа из каждого слова, если в слове меньше, чем три символа,
# оставшееся место стоит заполнить пробелами. Дополнительно сделать тоже самое при помощи регулярных выражений.


import re


def symbolThree(s):
    lst = s.split(' ')
    for i in range(0, len(lst)):
        print(lst[i][:3].ljust(3), len(lst[i][:3].ljust(3)))


a = 'qwerty qw a dfg'
symbolThree(a)



# 1: Написать функцию, которая возвращает первое слово из строки используя
# методы строки и отдельно регулярные выражения.

import re


def find_second_max(st):
   return st[:st.find(' ')]


a = 'qwerty asdfgh'
a1 = 'Hello, wold'
a2 = 'A B C'
print(find_second_max(a))
print(find_second_max(a1))
print(find_second_max(a2))

#using regexp

res = re.search(r'^\S+\s', a)
print('using regexp  ',res.group())


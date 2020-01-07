#10: Написать функцию, которая принимает в качестве аргумента строку и возвращает длину предпоследнего слова.
#Пример: penultimate_len('In the end the winner is still the last man standing') >> 3’


def testWold(s):
    s = s.split(' ')
    return len(s[-2])

a = 'In the end the winner is still the last man standing'
a1 = 'In the end the winner is still'
a2 = 'man standing still '
print(testWold(a))
print(testWold(a1))
print(testWold(a2))

#6: Написать функцию, которая принимает строку в качестве аргумента и возвращает строку, в которой все пробелы заменены на дефис.
#Пример: replace_spaces(‘Hello World’) >> ‘Hello-World’

def replace_spaces(s):
    return s.replace(' ', '-')

a = 'H e l l o W o r l d'
a1 = 'Hello World'
print(replace_spaces(a))
print(replace_spaces(a1))
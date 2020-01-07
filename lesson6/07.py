#7: Написать функцию, которая принимает в качестве аргументов строку,
#индекс, символ. Функция должна вернуть строку, в которой под указанным индексом будет заменен символ
#Пример: replace_char(‘Hello World’, 1, ‘a’) >> ‘Hallo World’


def replace_char(stroka,index, symbol):
    try:
        r = list(stroka)
        r[index] = symbol
        return ''.join(r)
    except IndexError as ie:
        return  ie
    except TypeError as te:
        return  te

a = 'Hello World'
print(replace_char(a, 3, 'X'))
print(replace_char(index=2, stroka=a, symbol='$'))
print(replace_char(a, 22, 'X'))
print(replace_char(a, 2, 1))


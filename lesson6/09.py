#9: Написать функцию, которая принимает в качестве аргумента строку. Функция должна возвращать “перевернутую” строк.
#Пример: reverse_string(‘never give up’) >> ‘up give never’

def reversString(s):
    s = s.split(' ')
    return ' '.join(s[::-1])


a = 'never give up'
print(reversString(a))
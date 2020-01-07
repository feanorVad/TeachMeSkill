# 7: Написать программу, которая будет генеририровать случайные строки, произвольной
# длинные в диапазоне от 1 до 4, в верхнем и нижнем регистре на вводимую пользователем длинну.
#Например 25: ['HT', 'rv', 'UL', 'mD', 'ad', 'Qw', 'ad', 'EX', 'Kn', 'kD', 'MI', 'ti', 'HB', 'Xk',
# 'ET', 'xO', 'lh', 'pg', 'VN', 'su', 'kc', 'iF', 'Bm', 'vK', 'Vd', 'wF', 'zh', 'Ph', 'KY', 'Go']

import random
import string

res = []

try:
    a = int(input('Enter '))
    for i in range(0, a):
        s = ''
        for j in range(0, random.randint(1, 4)):
            s += random.choice(string.ascii_letters)
        res.append(s)
    print(res)
except ValueError as e:
    print('Error at input: ', e)





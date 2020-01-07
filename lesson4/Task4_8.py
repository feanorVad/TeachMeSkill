# 8: Необходимо написать программу, которая сортирует список из примера задачи №7
# игнорируя заглавные и строчные буквы в обратном порядке. Должно получиться:
#['BH', 'ck', 'da', 'da', 'Dk', 'Dm', 'dV', 'Fi', 'Fw', 'gp', 'hl', 'hP', 'hz', 'IM', 'it', 'Kv', 'kX', 'LU',
# 'mB', 'nK', 'NV', 'oG', 'Ox', 'TE', 'TH', 'us', 'vr', 'wQ', 'XE', 'YK']


def reverselement(inputStr):
    return ''.join(reversed(inputStr))


a = ['HT', 'rv', 'UL', 'mD', 'ad', 'Qw', 'ad', 'EX', 'Kn', 'kD', 'MI', 'ti', 'HB', 'Xk', 'ET', 'xO', 'lh', 'pg', 'VN', 'su', 'kc', 'iF', 'Bm', 'vK', 'Vd', 'wF', 'zh', 'Ph', 'KY', 'Go']
for i in range(0,len(a)):
    a[i] = reverselement(a[i])

print(sorted(a, key=lambda x: (str(x[0]).lower(), str(x[1]).lower())))

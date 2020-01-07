# 2: Написать функцию, которая в качестве первого аргумента принимает число,
# а в качестве второго - словарь. Программа должна возвращать True,
# если первый аргумент представлен в значения словаря и False, если нет. Пример:
# a = 5, b = {'foo': 5, 'bar': 8}

def testArgument(arg, dict):
    if (list(dict.values()).count(arg)) > 0:
        return True
    else:
        return False


test_dic = {'q': 1, 'w': 2, 'e': 3, 't': 4, 'y': 5}
a1 = 5
a2 = 13
print(testArgument(a1, test_dic))
print(testArgument(a2, test_dic))

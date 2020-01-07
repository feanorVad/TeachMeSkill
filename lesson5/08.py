# 8: Написать функцию, которая принимает в качестве аргумента строку и возвращает True, если эта строка "зеркальная". Пример:
#abba - True
#hello, world! = False
#radar - True

def tryRevers(stroka):
    if stroka == stroka[::-1]:
        return True
    else:
        return False


a1 = 'abba'
a2 = 'hello, world!'
a3 = 'radar'
print(a1, tryRevers(a1))
print(a2, tryRevers(a2))
print(a3, tryRevers(a3))
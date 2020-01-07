#8: Написать функцию, которая принимает в качестве аргумента строку. Функция должна проверять и возвращать True,
# если переданная строка является палиндромом, в противном случае - False.
#Пример: check_palindrome(‘Never odd or even’) >> True

def testPalindrom(s):
    s = s.replace(' ', '').lower()
    if s == s[::-1]:
        return True
    else:
        return False



a = 'Never odd or even'
a1 = 'A bara Ba'
a2 = 'qwerty qwerty'
print(testPalindrom(a))
print(testPalindrom(a1))
print(testPalindrom(a2))

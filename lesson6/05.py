#5: Написать функцию, которая принимает строку в качестве аргумента и возвращает строку,
# в которой все строчные буквы заменены на заглавные и наоборот.
#Пример: swap_case(‘Hello World’) >> ‘hELLO wORLD’

def swap_case(s):
    return s.swapcase()


a = 'Hello World'
a1 = 'SMALL big'
print(swap_case(a))
print(swap_case(a1))
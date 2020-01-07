# 5: Написать функцию, которая в качестве аргумента принимает строку и считает количество заглавных,
# строчных букв, знаков препинания и выводит их сумму. Пример: "Hello, Wolrd!",
# результат: upper: 2, lower: 8, space: 1, punctuation: 2.


def workString(a):
    space = a.count(' ')
    upper = lower = 0
    for i in a:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    punctuation = len(a) - space-upper-lower
    return 'upper: ' + str(upper) + ' lower: ' + str(lower) + ' space: ' + str(space) + ' punctuation: ' + str(punctuation)

print(workString("Hello, Wolrd!1"))
print(workString("Hello, Wolrd!"))
print(workString("В языке Python есть строковые методы islower() и isupper(). Первый проверяет, являются ли все символы в строке маленькими, второй - большими."))


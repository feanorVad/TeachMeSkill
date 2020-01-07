# 4**: Смысл тот же, что и взадании 3, только программа будет принимать последовательность аргументов
# которые помимо чисел принимают операторы, кроме того, числовой ряд будет от 0 до 100 включительно. Пример:
#"twenty one", "plus", "forty two", "minus", "four", "multiply", "five", рузультат: 21 + 42 - 4 * 5 = 43.


dict_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                'nine': 9, 'ten': 10,'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
                'sixteen': 16,'seventeen': 17,'eighteen': 18,'nineteen': 19, 'twenty': 20, 'thirty': 30,
                'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100,
                'plus': '+', 'minus': '-', 'multiply': '*', 'division': '/'}


def argumet(a):
    space = a.find(' ')
    if space != -1:
        return str(dict_num.get(a[:space]) + dict_num.get(a[1+space:]))
    else:
        return str(dict_num.get(a))



def strMath(*args):
    lst = list(args)
    s = ''
    if lst[0] == 'minus':
        for i in range(0, len(lst)):
            if i % 2 >= 0:
                s += argumet(lst[i])
            else:
                s += dict_num.get(lst[i])
    else:
        for i in range(0, len(lst)):
            if i % 2 <= 0:
                s += argumet(lst[i])
            else:
                s += dict_num.get(lst[i])
    return eval(s)


print(strMath("twenty one", "plus", "forty two", "minus", "four", "multiply", "five"))
print(strMath("minus", "twenty one", "plus", "forty two", "minus", "four", "multiply", "five"))






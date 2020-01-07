# 3: Написать функцию, которая принимает неограниченное количество аргументов цифр,
# написанных прописью на английском языке и должна возвращать в качестве аргументов
# результат суммы в целочисленном представлении. Пример:
#ввод: "five", "six", результат 11. Допущение: функция должна быть расчитана на аргументы от 0 до 10 включительно.

def sumASstrig(*args):
    lst = list(args)
    sum = 0
    dict_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                'nine': 9, 'ten': 10}
    try:
        for i in range(0, len(lst)):
            sum += dict_num.get(lst[i])
        return sum
    except TypeError as e:
        return e
    print(sum)




print(sumASstrig('two', 'seven'))
print(sumASstrig('two', 'sevent',))
print(sumASstrig('zero', 'ten'))
print(sumASstrig('two', 'seven', 'six', 'one'))

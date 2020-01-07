# 11*: Необходимо написать программу используя list comprehension,
# которая будет генерировать список словарей,
# каждый словарь которых содержит в качестве ключа случайную последовательность длинною от 1 до 5 заглавных символов,
# а в качестве значения список словарей,
# каждый их которых в свою очередь содержит две пары ключ-значение 'required' и 'selected'
# со случайными числами в диапазоне от 1 до 10 для 'required' и от 1, 6 для 'selected'.
# В общей сложности должен получиться список следующего вида:
#[{'PH': [{'required': 1, 'selected': 1}, {'required': 2, 'selected': 5}, {'required': 5, 'selected': 9}]}, {'XKEOG': [{'required': 3, 'selected': 1}]}, {'J': [{'required': 5, 'selected': 8}, {'required': 5, 'selected': 10}, {'required': 5, 'selected': 10}]}, {'NVQG': [{'required': 5, 'selected': 8}, {'required': 5, 'selected': 6}, {'required': 5, 'selected': 9}, {'required': 4, 'selected': 6}, {'required': 4, 'selected': 9}]}, {'XGDB': [{'required': 2, 'selected': 10}, {'required': 2, 'selected': 4}, {'required': 5, 'selected': 7}]}, {'DZXN': [{'required': 3, 'selected': 3}, {'required': 3, 'selected': 3}, {'required': 4, 'selected': 4}]}, {'Y': [{'required': 1, 'selected': 8}, {'required': 3, 'selected': 9}]}, {'V': [{'required': 1, 'selected': 8}]}, {'I': [{'required': 3, 'selected': 10}]}, {'YU': [{'required': 4, 'selected': 1}, {'required': 4, 'selected': 8}, {'required': 2, 'selected': 1}]}]
import random
import string


s = [str(random.choice(string.ascii_uppercase)) for i in range(random.randint(1, 5))]
print(''.join(s))
lst = [{'required': random.randint(1, 10), 'selected': random.randint(1, 6)} for i in range(2)]
print(lst)
final_lst = [{''.join(s): lst} for i in range(5)]
print(final_lst)
final_lst2 = [{''.join([str(random.choice(string.ascii_uppercase)) for i in range(random.randint(1, 5))]):[{'required': random.randint(1, 10), 'selected': random.randint(1, 6)} for i in range(2)]} for i in range(5)]
print('\n\n')
print(final_lst2)

# А теперь главный вопрос: не сильно ли сложная конструкция для final_lst2? Как правильнее: такое награмождение
#или все же лучше постепенно?
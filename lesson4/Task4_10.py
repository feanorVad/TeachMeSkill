## 10: Написать программу, которая принимает список список
# [[3, 5, 8], [5, 8, 10], [1, 2], [2, 13, 9]],
# и выводит в качестве результата отсортированный список по сумме чисел подсписков в обратном порядке:
# [[2, 13, 9], [5, 8, 10], [3, 5, 8], [1, 2]]

def sum_element(list_int):
    return sum(list_int)
a = [[3, 5, 8], [5, 8, 10], [1, 2], [2, 13, 9] ]
a.sort(reverse=True, key=sum_element)
print(a)
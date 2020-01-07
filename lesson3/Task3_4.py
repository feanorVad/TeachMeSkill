#4. Написать программу, которая принимает два аргумента: месяц и год в формате целых чисел,
# а на выходе возвращает календарь для переданных данных, например: 2019, 12 (декабрь 19-го года):

import  calendar

try:
    y = int(input('Enter  year :'))
    m = int(input('Enter the number of month : '))
    a = calendar.TextCalendar(firstweekday=0)
    print(a.formatmonth(y, m))
except calendar.IllegalMonthError as ill_e:
    print('Exeption Month :', ill_e)
except IndexError as i_e:
    print('Exeption index : ', i_e)
except ValueError as v_e:
    print('Error at input : ', v_e)
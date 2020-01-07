# 1: Написать программу, которая в качестве аргумента принимает объект данных datettime,
# необходимо найти сколько времени с времени переданного объекта в днях, часах, минутах.
import datetime

try:
    a = input('Input date at format (yyyy-mm-dd): ')
    d = datetime.datetime.today()-datetime.datetime(*map(int, a.split('-')))
    print('Result full: ', d)
    print('Result  Days:', d.days)
    print('Result  Hours: ', d.total_seconds()//3600)
    print('Result  Minutes: ', (d.total_seconds()//60))
except ValueError as e:
    print('Error at Input: ', e)




#5. Написать программу, которая принимает в качестве аргумента даты в строковом представлении и возвращает
# количество рабочих дней между ними (пн, вт, ср, чт, пт - рабочие дни, сб, вс - выходные).
# Пример  '2019_7_2', '2019_7_11' - 8 рабочих дней, включая эти даты.


#import datetime
#a='2019_7_11'
#b='2019_7_2'
#a = a.split('_')
#b = b.split('_')
#aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
#bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
#print(str(aa-bb).split()[0])

#from datetime import date,timedelta
import  datetime

a = input('First date (yyyy_mm_dd): ')
b = input('First date (yyyy_mm_dd): ')
a = a.split('_')
b = b.split('_')
fromdate = datetime.date(int(a[0]), int(a[1]), int(a[2]))
todate = datetime.date(int(b[0]), int(b[1]), int(b[2]))
daygenerator = datetime.timedelta(fromdate,todate)
  #  (fromdate + datetime.timedelta(x) for x in range((todate - fromdate).days + 1))
print(str(daygenerator))
res = sum(1 for day in daygenerator if day.weekday() < 5)

print(res)
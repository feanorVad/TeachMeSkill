# 3: Написать функцию, которая находит выводит в качестве результата список всех доменов при помощи методов строк.
# Дополнительно сделать это при помощи регулярных выражений. Список:
#['baveja@att.net', 'mhassel@comcast.net', 'heine@sbcglobal.net', 'gbacon@comcast.net', 'slaff@hotmail.com', 'seemant@yahoo.com', 'miltchev@verizon.net', 'ducasse@hotmail.com', 'chaikin@yahoo.ca', 'agolomsh@yahoo.ca', 'joehall@msn.com', 'ilikered@optonline.net']
#Результат: ['@att', '@comcast', '@sbcglobal', '@comcast', '@hotmail', '@yahoo', '@verizon', '@hotmail', '@yahoo', '@yahoo', '@msn', '@optonline']

def findDomen(lst):
    res = []
    for l in lst:
        res.append(l[l.find('@'):l.find('.')])
    return res

a = ['baveja@att.net', 'mhassel@comcast.net', 'heine@sbcglobal.net', 'gbacon@comcast.net', 'slaff@hotmail.com', 'seemant@yahoo.com', 'miltchev@verizon.net', 'ducasse@hotmail.com', 'chaikin@yahoo.ca', 'agolomsh@yahoo.ca', 'joehall@msn.com', 'ilikered@optonline.net']
print(findDomen(a))


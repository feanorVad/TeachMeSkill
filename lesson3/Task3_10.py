#*10. Написать программу, которая принимает в качестве аргумента два списка и проверяет, является ли второй список
# "подмассивом" первого. Например: [1, 2, 3, 5, 8, 13, 42, 5, 8], [5, 8, 13, 42] -> True
lst1 = [1, 2, 3, 5, 8, 13, 42, 5, 8]
lst2 = [5, 8, 13, 42]
s1=''
s2=''
for i in range(0, len(lst1)):
    s1=s1+str(lst1[i])
for i in range(0, len(lst2)):
    s2 = s2+str(lst2[i])
if s1.find(s2) != -1:
    print(True)
else:
    print(False)
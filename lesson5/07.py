# 7: Написать функцию, которая принимает в качестве аргумента число и возвращает True, если это число делиться без остатка только на себя и на единицу и False, если нет.
#11 - True,
#12 - False,
#13 - True,
#18 - Flase,
#23 - True.

def isPrime(n):
   d = 2
   while n % d != 0:
       d += 1
   return d == n

print(isPrime(11))
print(isPrime(12))
print(isPrime(13))
print(isPrime(18))
print(isPrime(23))

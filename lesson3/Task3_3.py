#3. Написать программу, которая принимает на входе число n и выводит на экран n + nn - nnn * nnnn, пример: число 5
#5 + 55 - 555 * 5555 = -3082965


n = input(' Enter n : ')
try:
    print('Result: ', int(n)+int(n*2)-int(n*3)*int(n*4))
except ValueError as ee:
    print('Input Error : ', ee)


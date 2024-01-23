user = int(input('Введите пятизначное число:'))
a=10000
b=1000
c=100
d=10
num = user // a
num1 = user % a

num2 = num1 // b
num3 = num1 % b

num4 = num3 // c
num5 = num3 % c

num6 = num5 // d
num7 = num5 % d

num, num2, num4, num6, num7 = num7, num6, num4, num2, num

result = num *10000 + num2 * 1000 + num4 * 100 + num6 *10 + num7 *1
print(result)

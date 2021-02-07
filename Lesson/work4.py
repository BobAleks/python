num = int(input('Введите целое число: '))
a = -1
while num > 10:
    b = num % 10
    num //= 10
    if b > a:
        a = b
print(a)
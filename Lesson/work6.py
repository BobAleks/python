fday = int(input('Сколько километров вы пробежали в первый день: '))
eday = int(input('Какого результата хотите добиться: '))
day = 1
while fday < eday:
    fday *= 1.1
    day += 1
print(day)
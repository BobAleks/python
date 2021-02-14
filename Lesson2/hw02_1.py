# Задача-1: Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_int = 10
my_float = 4.3
my_str = "Всем привет"
my_list = ['first', '5','double', '10']
my_tuple = ('num', '7','5')
my_dict = {'name': 'Jhon', 'famille': 'Scott', 'age': '40'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')
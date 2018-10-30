# Создайте функцию, которая выводит приветствие для пользователя с заданным именем.
# Если имя не указано, она должна выводить приветствие для пользователя с Вашим именем.



#1 variant
# def hello(name):
#     if name:
#         name = str(input('enter your name please '))
#         print('Hello, ', name, '!')
#     else:
#         return
# hello('Hello, Anton')





#2 variant
def hello(name):
    if not name:
        return
        print('Hello, Anton!')
    else:
        name = str(input('enter your name please ')
hello ('Hello, ', name, '!')
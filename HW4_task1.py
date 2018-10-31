# Создайте функцию, которая выводит приветствие для пользователя с заданным именем.
# Если имя не указано, она должна выводить приветствие для пользователя с Вашим именем.




def hello():
    name = str(input('enter your name please '))
    if name:
        print('Hello, ', name, '!')
    else:
        print('Hello Anton')
        return
hello()

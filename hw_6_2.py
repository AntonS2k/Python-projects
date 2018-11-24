""" Задание №2.
Переделать Задание №1 с созданием и использованием собственное исключение
WhitespaceError с атрибутами:
    position - позиция в строке
    symbol - какой именно непечатный символ
Функция main() демонстрирует работу вашей функции, должна красиво показывать
что именно вызвало исключение.
"""


def main():
    whitespace = ['t','n','r','x','0','b','x','0','c']
    try:
        symb = str(input('Type a symbol: ')) # юзер вводит text, *args, **kwargs и введенная информация сравнивается с whitespace
        symb_pos = whitespace.index(symb)
        for i in symb:
            if i in whitespace:
                print('matched:', i) # выводится на печать какой именно символ совпал
                print('position:', symb_pos)
            else:
                print("Please type valid data")
    except (ValueError) as error:
            print()
main()



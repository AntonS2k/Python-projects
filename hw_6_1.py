def main():
    whitespace = str('tnrx0bx0c')
    try:
        text = str(input('Type a symbol: ')) # юзер вводит text, *args, **kwargs и введенная информация сравнивается с whitespace
        for i in text:
            if i in whitespace:
                print('matched:',i) # выводится на печать какой именно символ совпал
            else:
                print("Please type valid data")
    except (ValueError) as error:
            print()


main()


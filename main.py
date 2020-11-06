import Cezar
import Atbash
import Afin


def load_text(filename):
    filename = "data/" + filename
    try:
        with open(filename, 'r', encoding='utf-8') as textFile:
            text = [line for line in textFile]
    except FileNotFoundError as message:
        print('Такого файла по данному пути не существует: ', filename)
        raise SystemExit()
    return text[0].split()


def save_text(text, file_name):
    filename = "data/" + file_name + '.txt'
    try:
        with open(filename, 'w', encoding='utf-8') as textFile:
            textFile.write(text)
    except FileNotFoundError as message:
        print('Такого файла по данному пути не существует: ', filename)
        raise SystemExit()


print('Приветствую в программе шифровки разными способами.')
method = None
com_text = None
com = None
save_com = None
exit_or_no = None
while True:
    if not method:
        print('\nВ данный момент доступно 3 метода шифровки. Выберите нужный:\n1. Цезарь\n2. Атбаш\n3. Афинный')
        method = int(input('Введите номер метода: '))
        if method == 1:
            print('\nВы выбрали: Цезарь')
        elif method == 2:
            print('\nВы выбрали: Атбаш')
        elif method == 3:
            print('\nВы выбрали: Афинный')
        else:
            print('\nВы ввели неверно. Повторите попытку')
            method = None
            continue


    if not com_text:
        print('\nВы можете ввести текст самостоятельно или вставить готовый текст формата txt.\n1. Вводить самостоятельно\n'
              '2. Вставить готовый')
        com_text = int(input('Введите выбранный ответ: '))
        if com_text == 1:
            print('Введите текст:')
            text = input()
        elif com_text == 2:
            text = load_text(input('Введите название файла: ') + '.txt')
            text = ' '.join(text)
        else:
            print('\nВы ввели неверно. Повторите попытку')
            com_text = None
            continue
        print('\nВаш текст:', text, sep='\n')
    if not com:
        print('\nДоступные команды:\n1. Зашифровать текст\n2. Расшифровать текст')
        com = int(input('Выберите команду: '))
        if com == 1:
            if method == 1:
                key = int(input('Введите ключ для шифра цезаря: '))
                r_text = ' '.join(Cezar.cezar_encode(text, key))
                print('\nВаш зашифрованный текст:', r_text, sep='\n')
            elif method == 2:
                r_text = ' '.join(Atbash.atbash(text))
                print('\nВаш зашифрованный текст:', r_text, sep='\n')
            elif method == 3:
                a, b = map(int, input('Введите ключ a и b для афинного шифра: ').split())
                r_text = ' '.join(Afin.afin_encode(text, a, b))
                print('\nВаш зашифрованный текст:', r_text, sep='\n')
        elif com == 2:
            if method == 1:
                key = int(input('Введите ключ для шифра цезаря: '))
                r_text = ' '.join(Cezar.cezar_decode(text, key))
                print('\nВаш расшифрованный текст:', r_text, sep='\n')
            elif method == 2:
                r_text = ' '.join(Atbash.atbash(text))
                print('\nВаш Расшифрованный текст:', r_text, sep='\n')
            elif method == 3:
                a, b = map(int, input('Введите ключ a и b для афинного шифра: ').split())
                r_text = ' '.join(Afin.afin_decode(text, a, b))
                print('\nВаш Расшифрованный текст:', r_text, sep='\n')
        else:
            print('\nВы ввели неверно. Повторите попытку')
            com = None
            continue
    if not save_com:
        print('\nХотите ли вы сохранить текст?:\n1. Да\n2. Нет')
        save_com = int(input('Введите выбранный ответ: '))
        if save_com == 1:
            name = input('Введите названия для файла, куда сохранится текст: ')
            save_text(r_text, name)
            print('\nФайл успешно сохранен в', name + '.txt')
        elif save_com == 2:
            print('\nВы решили не сохранять текст')
        else:
            print('\nВы ввели неверно. Повторите попытку')
            method = None
            continue
    print('\nХотите завершить работу программы?:\n1. Да\n2. Нет')
    exit_or_no = int(input('Введите выбранный ответ: '))
    if exit_or_no == 1:
        print('\nСпасибо за использование данной программы. До свидания!')
        break
    elif exit_or_no == 2:
        method = None
        com_text = None
        com = None
        save_com = None
        exit_or_no = None
        continue
    else:
        print('\nВы ввели неверно. Повторите попытку')
        method = None
        continue


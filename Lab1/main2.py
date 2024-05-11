from main import *

def print_menu():
    print("Меню:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Сложение в IEEE 754")
    print("6. Перевод числа в двоичный код")
    print("7. Перевод числа в IEEE 754")
    print("8. Выход")

# Главный цикл программы
while True:
    print("----"*8)
    print_menu()
    try:
        choice = input("Выберите опцию (1-8): ")
    except:
        print("Ошибка ввода :( ")
        break

    if choice == "1":
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(f'{a} + {b}: {add(a, b)}')
        print(f'Ответ : {a + b}')

    elif choice == "2":
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(f'{a} - {b}: {substract(a,b)}')
        print(f'Ответ : {a - b}')


    elif choice == "3":
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(f'{a} * {b}: {multiply(a, b)}')
        print(f'Ответ : {a * b}')

    elif choice == "4":
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(f'{a} / {b}: {divide_binary(a, b)}')
        print(f'Ответ : {a / b}')

    elif choice == "5":
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        print(f'{a} + {b}: {add_ieee754(decimal_to_ieee754(a), decimal_to_ieee754(b))}')
        print(f'Ответ : {a + b}')

    elif choice == "6":
        a = int(input('Введите число: '))
        print(f'{a} в Прямом : {direct_complement(a)}')
        print(f'{a} в Обратном : {inverse_complement(a)}')
        print(f'{a} в Дополнительном : {twos_complement(a)}')

    elif choice == "7":
        a = float(input('Введите число: '))
        print(f'{a} в IEEE 754 : {decimal_to_ieee754(a)}')


    elif choice == "8":
        print("Программа завершена.")
        break

    else:
        print("Некорректный выбор. Попробуйте еще раз.")
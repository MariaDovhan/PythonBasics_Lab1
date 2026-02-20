import sys

def parseInput(number):
    # Дано три спроби ввести число
    for i in range(0, 2):
        try:
            return float(number)
        except ValueError:
            print('Ви ввели не число, спробуйте ще ', end='')
            number = input()
    print('Спроби закінчилися, кінець програми ', end='')
    sys.exit()

def main():
    # Виведення користувачу опису програми
    print('Ця програма зчитує два введених числа і повертає їх суму, різницю, добуток та частку, '
        'зчитує інші два числа і обчислює їх добуток')

    # Основне завдання
    # Введення першого числа з клавіатури
    a = parseInput(input('Введіть перше число ')) 

    # Введення другого числа з клавіатури
    b = parseInput(input('Введіть друге число '))

    # Обчислення суми, різниці, добутку
    sum = a + b
    difference = a - b
    product = a * b

    # Обчислення частки за умови що дільник не дорівнює нулю
    quotient = a / b if b != 0 else None

    # Вивід результату додавання, віднімання і множення
    print(f'Сума: {sum:.2f}\nРізниця: {difference:.2f}\nДобуток: {product:.2f}')

    # Вивід результату ділення
    if quotient == None:
        print('Не вдалося обчислити частку оскільки ділення на нуль неможливе')
    else:
        print(f'Частка: {quotient:.2f}')
    print()

    # Індивідуальне завдання
    # Введення першого числа
    multiplicant1 = parseInput(input('Введіть перший множник '))

    # Введення другого числа
    multiplicant2 = parseInput(input('Введіть другий множник '))

    # Запис результату множення у змінну
    mult_result = multiplicant1 * multiplicant2

    # Вивід результату
    print(f'Результат множення двох чисел: {mult_result:.2f}')

if __name__ == '__main__':
    main()
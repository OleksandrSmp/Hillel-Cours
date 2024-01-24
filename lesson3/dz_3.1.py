number_1 = float(input('Введите первое число:'))
action = input('Выполните действие: +, -, *, /, \n')
number_2 = float(input('Введите второе число:'))
if action == '+':
    print(number_1 + number_2)
elif action == '-':
    print(number_1 - number_2)
elif action == '*':
    print(number_1 * number_2)
elif action == '/':
    if number_2 != 0:
        print(number_1 / number_2)
    else:
        print("Неверная операция:")






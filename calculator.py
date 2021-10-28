 # -*- coding: utf-8 -*-
 
print('Калькулятор Запущен')
answer = str(input('Want to work on a calculator? [y], [n]'))
while answer != 'n':
    res1 = int()
    res2 = int()
    res3 = int()
    res4 = int()

    a = int(input('Введите первое значение\n'))
    b = int(input('Введите второе значение\n'))

    c = (input('Исполнить все сразу или по отдельности выбрать действие?\n [1]- Все сразу [2]- По отдельности'))
    if c == '1':
        res1 = a + b
        res2 = a - b
        res3 = a * b
        if b == 0:
            res4 = 'Ошибка'
            print('Деление не возможно')
        else:
            res4 = a / b
        print(res1, res2, res3, res4)
    elif c == '2':
        print("Выберите ваше действие")
        d = (input('(1)- Сложение, (2)- Вычетание, (3)- Умножение, (4)- Деление\n'))
        if d == '1':
            res1 = a + b
            print(res1)
        elif d == '2':
            res2 = a - b
            print(res2)
        elif d == '3':
            res3 = a * b
            print(res3)
        elif d == '4':
            if b == 0:
                print('Ошибка')
            else:
                res4 = a / b
                print(res4)
        else:
            print('Нет такого значения!')
    else:
        print('Такого значения нет!')
    answer = (input('Хотите продолжить работу? "y" or "n" '))

print('Досвидания! Удачи!')

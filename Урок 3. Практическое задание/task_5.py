"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""
import sys


def two_arg_sum(number, summa=0):
    summa += int(number)
    return summa


final_sum = 0
while True:
    input_string = input("Введите числа. Для подсчета промежуточного итога нажмите [Enter]\n"
                         "Получить окончальный результат: введите символ \"^\": ")
    for i in input_string.split():
        if i != "^":
            final_sum = two_arg_sum(i, final_sum)
        else:
            print(final_sum)
            sys.exit(0)
    print(final_sum)

"""
Введите числа. Для подсчета промежуточного итога нажмите [Enter]
Получить окончальный результат: введите символ "^": 1 2 3
6
Введите числа. Для подсчета промежуточного итога нажмите [Enter]
Получить окончальный результат: введите символ "^":  1 2 3 ^
12

Process finished with exit code 0
"""

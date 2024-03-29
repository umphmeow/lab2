"""Натуральные числа, не превышающие 1000000, у которых первые две цифры равны 77. Выводит на экран числа, без этих 7.
Вычисляется среднее число между минимальным и максимальным и выводится прописью. С ПОМОЩЬЮ РЕГУЛЯРНЫХ ВЫРАЖЕНИЙ
"""
import re

dict = {'1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять', '0': 'ноль', '.': 'целых', ',': 'десятых'}
print("Задание: Программа,которая читая файл, распознает, преобразует и выводит на экран числа по определенному правилу. Числа распознаются по законам грамматики русского языка. На ввод даются натуральные числа, не превышающие 1 000 000, у которых первые две цифры равны 77. Программа выводит на экран числа, без этих 7; Вычисляет среднее число между минимальным и максимальным и выводит прописью.")
try:
    with open('text.txt', 'r') as f_in:
        data = f_in.read()
        digits = [d.replace('77', '', 1) for d in re.findall(r'\b77\d*\b', data)]
        d_array = [d for d in digits if d]
        d_arr_int = list(map(int, d_array))

    if not d_array:
        print('Не найдено цифр удовлетворяющих заданию или цифр нет вообще')
    else:
        print('Массив чисел:', d_arr_int)
        max_d = max(d_arr_int)
        min_d = min(d_arr_int)
        print('Максимальное число:', max_d)
        print('Минимальное число:', min_d)
        answer = (max_d + min_d) / 2
        print('Среднее арифметическое:', answer)
        answer_txt = ''
        for digit in str(answer):
            answer_txt += ' ' + dict[digit]
        print('Ответ:', answer_txt, dict[','])
except FileNotFoundError:
    print('Файл text.txt не найден')

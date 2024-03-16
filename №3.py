# -*- coding: utf-8 -*-

def binary_search(mas, low, high):
    """

    :param mas: массив с ценами
    :param low: нижняя граница
    :param high: верхняя граница
    :param l: индекс нижней границы
    :param h: индекс верхней границы
    :return: индексы границ
    """
    l = 0
    h = 0
    for i in range(len(mas)):
        if mas[i] >= low and l == 0:
            l = i
        if mas[i] > high and h == 0:
            h = i
        if l != 0 and h != 0:
            return [l, h]


with open("cars.txt", "r") as a:
    b = list(map(lambda x: x.split("$"), a.readlines()))[1:]
    b = list(sorted(b, key=lambda x: int(x[0])))
    c = list(map(lambda x: int(x[0]), b))
    min_input = int(input())
    max_input = int(input())
    q = binary_search(c, min_input, max_input)
    b = b[q[0]: q[1]]
    if not b:
        print("К сожалению, под ваш бюджет ничего не удалось найти")
    else:
        for i in range(len(b)):
            print(f"""{i + 1} {b[i][2]} {b[i][3]}; Цвет: {b[i][-1][:-1]}; Пробег: {b[i][-2]}; Цена: {b[i][0]}""")
            vvod = input()
            if vvod == "стоп":
                break

# -*- coding: utf-8 -*-

def sort(b):
    """
    сортировка пузырьком
    :param b: массив с машинами
    :return: отсортированный массив
    """
    for i in range(len(b) - 1):
        for j in range(i + 1, len(b)):
            if int(b[i][0]) > int(b[j][0]):
                b[i], b[j] = b[j], b[i]
    return b


with open("cars.txt", "r") as a:
    b = list(map(lambda x: x.split("$"), a.readlines()))[1:]
    b = sort(b)
    for i in range(3):
        print(f"""{b[i][2]} {b[i][3]}; Цвет: {b[i][-1][:-1]}; Пробег: {b[i][-2]}; Цена: {b[i][0]}""")

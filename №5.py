# -*- coding: utf-8 -*-

with open("cars.txt", "r") as a:
    """Описание кода
            b - массив с информацией о машинах вида: price, year, manufacturer, model, odometer, paint_color
            c - словарь с марками
            q - отфильтрованный массив
    """
    b = list(map(lambda x: x.split("$"), a.readlines()))[1:]
    c = {
            'buick': 0,
            "chrysler": 0,
            "volvo": 0,
            "infiniti": 0,
            "lincoln": 0,
            "acura": 0,
            "hyundai": 0,
             "mercedes-benz": 0,
            "audi": 0,
            "bmw": 0
        }

    for i in list(c.keys()):
        q = list(filter(lambda x: x[2] == i, b))
        c[i] = len(q)
        print(i, len(q))
# -*- coding: utf-8 -*-

with open("cars.txt", "r") as a:
    b = list(map(lambda x: x.split("$"), a.readlines()))[1:]
    c = set(map(lambda x: x[-1], b))
    for i in c:
        q = list(filter(lambda x: x[-1] == i, b))
        print(f"""{len(q)} машин цвета {i.replace("\n", "")} есть сегодня в наличии""")

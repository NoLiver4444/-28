with open("cars.txt", "r") as a:
    b = list(map(lambda x: x.split("$"), a.readlines()))[1:]
    f = open("odometer_car.txt", "w", encoding="utf-8")
    check = 0
    for i in b:
        if float(i[4]) < 10000:
            f.write(f"""{i[2]} {i[3]}; Цвет: {i[-1][:-1]}; Пробег: {i[-2]}; Цена: {i[0]}\n""")
            check += 1
        if check == 10:
            break

    f.close()

""" Описание кода
b - массив с информацией о машинах вида: price, year, manufacturer, model, odometer, paint_color
f - новый файл odometer_car.txt
check - проверка количества машин
"""

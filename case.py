from hotel import *

price_list = {1: 2900, 2: 2300, 3: 3200, 4: 4100}
comfort_list = {1: 1.0, 2: 1.2, 3: 1.5}
with open("fund.txt", "r", encoding="UTF-8-sig") as rooms:
    text = rooms.readlines()
    # Обрабатываем и отправляем в класс Room, чтобы сгенерировать объекты (какие номера есть)
    for i in text:
        room1 = i.split()
        number = room1[0], type_ = room1[1], human_quantity = room1[2], comfort_degree = room1[3]
        current_room = Room(number, type_, human_quantity, comfort_degree)
        current_room.count_price(price_list, comfort_list)


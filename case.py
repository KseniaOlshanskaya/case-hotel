from hotel import *

variants_dict = {}
price_list = {1: 2900, 2: 2300, 3: 3200, 4: 4100}
comfort_list = {1: 1.0, 2: 1.2, 3: 1.5}
food_dict = {1: 0.0, 2: 280.0, 3: 1000.0}
big_list = []

with open("fund.txt", "r", encoding="UTF-8-sig") as rooms:
    text = rooms.readlines()
    for i in text:
        room1 = i.split()
        number = room1[0]
        type_ = room1[1]
        human_quantity = room1[2]
        comfort_degree = room1[3]
        current_room = Choice(number, type_, human_quantity, comfort_degree)
        current_room.count_price(price_list, comfort_list)

        for t in range(1, int(current_room.human_quantity)+1):
            for n in range(1, 4):
                room_list = []
                current_room.choose(t, food_dict[n])
                cur_room = Choice(current_room.number,
                                  current_room.type_,
                                  current_room.human_quantity,
                                  current_room.comfort_degree,
                                  current_room.price,
                                  current_room.human_fact,
                                  current_room.nutrition_type)
                room_list.append(current_room.price)
                room_list.append(cur_room)
                big_list.append(room_list)
                current_room.price -= food_dict[n]
            current_room.price /= t
    big_list = sorted(big_list, key=lambda tup: tup[0])
    for i in big_list:
        print(i)






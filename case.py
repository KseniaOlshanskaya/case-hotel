from hotel import *

price_list = {1: 2900, 2: 2300, 3: 3200, 4: 4100}
comfort_list = {1: 1.0, 2: 1.2, 3: 1.5}
food_dict = {1: 0.0, 2: 280.0, 3: 1000.0}
big_list = []
status_dict = {}
counter = 0

with open("fund.txt", "r", encoding="UTF-8-sig") as rooms:
    text = rooms.readlines()
    for i in text:
        counter += 1
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
        status_dict[counter] = cur_room.status  # Это словарь статусов комнат, False - свободна, True - занята

    big_list = sorted(big_list, key=lambda tup: tup[0], reverse=True)
    #for i in big_list:
       # print(i)
    #print(status_dict)

    # Это когда работа с клиентами, чтоб менять статус номера:
    # new_status = cur_room.status_change()
    # status_dict.update({cur_room.number: new_status})


list_visitor = []
with open("booking.txt", "r", encoding="UTF-8-sig") as rooms:
    text = rooms.readlines()
    for i in text:
        visitor_list = []
        guest1 = i.split()

        book = guest1[0], guest_name = guest1[1], guest_name2 = guest1[2]
        guest_name3 = guest1[3]
        how_much = int(guest1[4])
        date_in = guest1[5]
        how_long = int(guest1[6])
        max_price = int(guest1[7])

        day = int(date_in[0:2])
        day = day + how_long
        day = str(day)
        if len(day) == 1:
            a = "0"
            a += day
            day = a
        else:
            pass
        day_out = date_in.replace(date_in[0:2], day)

        visitor = Visitor(book, guest_name, guest_name2, guest_name3, how_much,
                          date_in, how_long, max_price, day_out)
        visitor.count_price()
        visitor_list.append(visitor)



        list_visitor.append(visitor)

#for i in list_visitor:
    #print(i)

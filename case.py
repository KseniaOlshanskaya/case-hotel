from hotel import *

price_list = {1: 2900, 2: 2300, 3: 3200, 4: 4100}
comfort_list = {1: 1.0, 2: 1.2, 3: 1.5}
food_dict = {1: 0.0, 2: 280.0, 3: 1000.0}
big_list = []
status_dict = {}
counter = 0
list_ = []

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
        list_.append(current_room)
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
    dict_ = {}
    counter12 = 1
    for t in list_:
        dict_.update({counter12: t.type_})
        counter12 += 1

visitor_list = []
with open("booking.txt", "r", encoding="UTF-8-sig") as rooms:
    text = rooms.readlines()
    for i in text:

        guest1 = i.split()

        book = guest1[0]
        guest_name = guest1[1]
        guest_name2 = guest1[2]
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

day1 = int(visitor_list[0].date_in[:2])
income = 0
missed_income = 0

for i in visitor_list:
    if int(i.book[:2]) != day1:
        hotel = Hotel(round(income, 2), round(missed_income, 2))
        busy_rooms_list = hotel.busy_(status_dict, b)
        hotel.percentage(list_)
        hotel.categories(busy_rooms_list, dict_)
        print("------" * 100)
        print("Итог за " + b)
        print(hotel)
        print("------" * 100)
        income = 0
        missed_income = 0
    #print("..."*100)
    print('Поступила заявка на бронирование:')
    print(i)
    counter = 0
    for j in big_list:
        if j[1].price > i.max_price_for_all:
            pass
        else:
            if j[1].human_fact != i.how_much:
                pass
            else:
                if j[1].status is False:
                    print('Найден:')
                    print(j[1])
                    a = answer()
                    new_status = j[1].status_change(i.date_in, i.day_out)
                    status_dict.update({int(j[1].number): new_status})
                    counter += 1
                    if a == 0:
                        missed_income += j[1].price
                    elif a == 1:
                        income += j[1].price
                    break
                else:
                    a = int((j[1].status[0])[:2])
                    b = int((j[1].status[1])[:2])
                    c = int(i.date_in[0:2])
                    d = int(i.day_out[0:2])
                    if d < a:
                        print('Найден:')
                        print(j[1])
                        a = answer()
                        new_status = j[1].status_change(i.date_in, j[1].status[1])
                        status_dict.update({int(j[1].number): new_status})
                        counter += 1
                        if a == 0:
                            missed_income += j[1].price
                        elif a == 1:
                            income += j[1].price
                        break
                    elif b < c:
                        print('Найден:')
                        print(j[1])
                        a = answer()
                        new_status = j[1].status_change(j[1].status[0], i.day_out)
                        status_dict.update({int(j[1].number): new_status})
                        counter += 1
                        if a == 0:
                            missed_income += j[1].price
                        elif a == 1:
                            income += j[1].price

                        break
                    else:
                        pass

    if counter == 0:
        print('Предложений по данному запросу нет. В бронировании отказано. \n')
        missed_income += i.max_price_for_all
    b = i.book
    day1 = int(i.book[:2])
hotel = Hotel(round(income, 2), round(missed_income, 2))
busy_rooms_list = hotel.busy_(status_dict, b)
hotel.percentage(list_)
hotel.categories(busy_rooms_list, dict_)
print("------" * 100)
print("Итог за " + b)
print(hotel)
print("------" * 100)
income = 0
missed_income = 0

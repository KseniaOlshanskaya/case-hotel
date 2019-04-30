from random import randint


class Room:
    def __init__(self, number, type_, human_quantity, comfort_degree, price=0):
        self.number = number
        self.type_ = type_
        self.human_quantity = human_quantity
        self.comfort_degree = comfort_degree
        self.price = price

    def __str__(self):
        s = str(self.number)
        s += " " + self.type_
        s += " " + str(self.human_quantity)
        s += " " + self.comfort_degree
        s += " " + str(self.price)
        return s

    def __repr__(self):
        return self.__str__()

    def count_price(self, price_list, comfort_list):
        if self.type_ == "одноместный":
            self.price = price_list[1]
        elif self.type_ == "двухместный":
            self.price = price_list[2]
        elif self.type_ == "полулюкс":
            self.price = price_list[3]
        else:
            self.price = price_list[4]
        if self.comfort_degree == "стандарт":
            pass
        elif self.comfort_degree == "стандарт_улучшеный":
            self.price *= comfort_list[2]
        else:
            self.price *= comfort_list[3]


class Choice(Room):
    def __init__(self, number, type_, human_quantity, comfort_degree, price=0, human_fact=0, nutrition_type=0,
                 status=False):
        super().__init__(number, type_, human_quantity, comfort_degree, price)
        self.human_fact = human_fact
        self.nutrition_type = nutrition_type
        self.status = status    # Если статус False, значит номер не занят, ниже есть функция,
                                # которая меняет статус

    def __str__(self):
        s = "номер " + str(self.number) + " " + self.type_ + " " + self.comfort_degree
        s += " рассчитан на " + str(self.human_quantity) + " человек "
        s += "фактически " + str(self.human_fact) + " чел. " + str(self.nutrition_type)
        s += " стоимость " + str(self.price) + " руб./сутки"
        return s

    def __repr__(self):
        return self.__str__()

    def status_change(self, a = False, b = False):
        if self.status is False:
            self.status = [a, b]
        else:
            self.status = False
        return self.status

    def choose(self, t, food_type):
        self.human_fact = t
        self.nutrition_type = food_type
        self.price += self.nutrition_type
        self.price *= self.human_fact
        if int(self.human_quantity) > t:
            self.price *= 0.7
        self.price = round(self.price, 2)
        return self.price


class Hotel:
    def __init__(self, income, missed_income):
        self.busy = 0
        self.free = 0
        self.load_percentage = 0
        self.percentage1 = 0
        self.percentage2 = 0
        self.percentage3 = 0
        self.percentage4 = 0
        self.income = income
        self.missed_income = missed_income

    def __str__(self):
        s = "Количество занятых номеров: " + str(self.busy) + "\n"
        s += "Количество свободных номеров: " + str(self.free) + "\n"
        s += "Занятость по категориям:\n"
        s += "Одноместных: " + str(self.percentage1) + "\n"
        s += "Двухместных: : " + str(self.percentage2) + "\n"
        s += "Полулюкс: " + str(self.percentage3) + "\n"
        s += "Люкс: : " + str(self.percentage4) + "\n"
        s += "Процент загруженности гостинницы: " + str(self.load_percentage) + "\n"
        s += "Доход за день: " + str(self.income) + "\n"
        s += "Упущенный доход: " + str(self.missed_income) + "\n"
        return s

    def __repr__(self):
        return self.__str__()

    def busy_(self, status_dict, b):
        busy_rooms = []
        for i in status_dict:
            if status_dict[i] is not False:
                a = status_dict[i]
                c = int((a[0])[:2])
                d = int((a[1])[:2])
                if c > int(b[:2]):
                    self.free += 1
                elif int(b[:2]) > d:
                    self.free += 1
                else:
                    self.busy += 1
                    busy_rooms.append(i)
            else:
                self.free += 1
        return busy_rooms

    def percentage(self, text):
        self.load_percentage = round((100 * self.busy) / len(text), 2)
        return self.load_percentage

    def categories(self, busy_rooms_list, dict_):
        for i in busy_rooms_list:
            if dict_[i] == "одноместный":
                self.percentage1 += 1
            elif dict_[i] == "двухместный":
                self.percentage2 += 1
            elif dict_[i] == "полулюкс":
                self.percentage3 += 1
            else:
                self.percentage4 += 1


class Visitor:
    def __init__(self, book, guest_name, guest_name2, guest_name3, how_much,
                date_in, how_long, max_price, day_out):
        self.book = book
        self.guest_name = guest_name
        self.guest_name2 = guest_name2
        self.guest_name3 = guest_name3
        self.how_much = how_much
        self.date_in = date_in
        self.how_long = how_long
        self.max_price = max_price
        self.day_out = day_out
        self.max_price_for_all = 0

    def __str__(self):
        s = self.book + " "
        s += self.guest_name + " " + self.guest_name2 + " " + self.guest_name3 + " "
        s += str(self.how_much) + " "
        s += self.date_in + " "
        s += str(self.how_long) + " "
        s += str(self.max_price)
        return s

    def __repr__(self):
        return self.__str__()

    def count_price(self):
        self.max_price_for_all = self.max_price * self.how_much
        return self.max_price_for_all


def answer():
    a = randint(1, 4)
    if a == 1:
        print('Клиент отказался от бронирования. \n')
        print("..." * 100)
        return 0
    else:
        print('Клиент согласен. Номер забронирован. \n')
        print("..." * 100)
        return 1

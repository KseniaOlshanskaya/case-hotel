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

    def status_change(self):
        if self.status is False:
            self.status = True
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
    pass    # Класс занятости номеров
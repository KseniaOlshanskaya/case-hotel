class Room:
    def __init__(self, number, type_, human_quantity, comfort_degree):
        self.number = number
        self.type_ = type_
        self.human_quantity = human_quantity
        self.comfort_degree = comfort_degree

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
            self.price = int(self.human_quantity) * price_list[1]
        elif self.type_ == "двухместный":
            self.price = int(self.human_quantity) * price_list[2]
        elif self.type_ == "полулюкс":
            self.price = int(self.human_quantity) * price_list[3]
        else:
            self.price = int(self.human_quantity) * price_list[4]
        if self.comfort_degree == "стандарт":
            pass
        elif self.comfort_degree == "стандарт_улучшеный":
            self.price *= comfort_list[2]
        else:
            self.price *= comfort_list[3]


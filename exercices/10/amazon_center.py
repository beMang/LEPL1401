class Command:
    __total_number_command = 0
    __total_price = 0

    @classmethod
    def get_number_total_command(cls):
        return cls.__total_number_command

    @classmethod
    def get_total_price(cls):
        return cls.__total_price

    def __init__(self, id_buyer, id_item, quantity_item, price_item) -> None:
        self.__id_buyer = id_buyer
        self.__id_item = id_item
        self.__quantity_item = quantity_item
        self.__price_item = price_item

        Command.__total_number_command += 1
        Command.__total_price += self.get_price()

    def get_price(self):
        return self.__quantity_item*self.__price_item

    def __str__(self) -> str:
        return "{}, {} : {} * {} = {}".format(self.__id_buyer, self.__id_item, self.__price_item, self.__quantity_item, self.get_price())

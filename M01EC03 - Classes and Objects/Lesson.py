"test"


class Y:
    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_month(self):
        return self.__month

    def set_month(self, month):
        self.__month = month

    def get_day(self):
        return self.__day

    def set_day(self, day):
        self.__day = day

    def describe(self):
        print(self.__year)


d = Y(2000, 1, 2)
print(d.get_year())

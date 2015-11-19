__author__ = 'Hunor Czaka'
"""
Currently supported currency types:
    'EUR',
    'USD',
    'SGD',
    'TWD'
"""


CURRENCIES = [
    'EUR',
    'USD',
    'SGD',
    'TWD'
]


class Currency:
    def __init__(self, amount, curr) -> None:
        """
            :rtype : None
            :param amount: amount field
            :type amount: float
            :param curr: currency type
            :type curr: str
            """
        self.__curr = 'NOT DEFINED'
        self.amount = 0.0
        if curr in CURRENCIES:
            self.__curr = curr
            self.amount += amount
        else:
            # TODO Exception Handling if the Currency type is not supported
            print('The selected type of currency %s is not in the supported types!' % curr)
            print('Please check the supported currency types in the module documentation first.')

    def get_currency(self):
        return self.__curr

    def __str__(self):
        return str(self.amount) + ' ' + self.__curr

    def __add__(self, other):
        """
        :param other: an instance of Currency
        :type other: Currency
        :returns: amount in case of same currency type, x1 + x2
        :rtype: Currency
        """
        if self.__curr == other.get_currency():
            return Currency(self.amount + other.amount, self.__curr)
        else:
            # TODO Handling if the currency type is not compatible in case of addition (e.g. automatically convert)
            print('Currency type of the two amounts are different. Please check it!')

    def __sub__(self, other):
        """
        :param other: an instance of Currency
        :type other: Currency
        :returns: amount in case of same currency type, x1 - x2
        :rtype: Currency
        """
        if self.__curr == other.get_currency():
            return Currency(self.amount - other.amount, self.__curr)
        else:
            # TODO Handling if the currency type is not compatible in case of addition (e.g. automatically convert)
            print('Currency type of the two amounts are different. Please check it!')


if __name__ == "__main__":
    usd1 = Currency(50, 'USD')
    usd1.amount = 155.0
    print(usd1)
    usd2 = Currency(270, 'USD')
    print(usd2)
    usd2 = usd1 + usd2
    print(usd2)
    print(usd2 - usd1)

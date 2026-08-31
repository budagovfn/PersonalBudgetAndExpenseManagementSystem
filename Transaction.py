class Transaction:
    def __init__(self, amount, description, sender, addressee, date):
        self.__amount = amount
        self.__description = description

        self.__sender = sender
        self.__addressee = addressee
        self.__date = date

    @property
    def amount(self):
        return self.__amount

    @property
    def description(self):
        return self.__description

    @property
    def sender(self):
        return self.__sender

    @property
    def addressee(self):
        return self.__addressee

    @property
    def date(self):
        return self.__date



class Transaction:
    def __init__(self, amount, currency, description, sender, addressee):
        self.__amount = amount
        self.__currency = currency
        self.__description = description

        self.__sender = sender
        self.__addressee = addressee

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency

    @property
    def description(self):
        return self.__description

    @property
    def sender(self):
        return self.__sender

    @property
    def addressee(self):
        return self.__addressee



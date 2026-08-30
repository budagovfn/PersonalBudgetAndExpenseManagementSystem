class BudgetManager:
    def __init__(self, id, amount, transactions):
        self.__id = id
        self.__amount = amount
        # maybe the password will be added here
        self.__transactions = transactions


    @property
    def id(self):
        return self.__id

    @property
    def amount(self):
        return self.__amount

    @property
    def transactions(self):
        return self.__transactions

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @transactions.setter
    def transactions(self, transactions):
        self.__transactions = transactions



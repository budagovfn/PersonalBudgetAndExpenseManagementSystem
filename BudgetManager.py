from Transaction import Transaction
from Utils import *
from datetime import datetime

class BudgetManager:
    def __init__(self, id, amount, transactions=[]):
        self.__id = id
        self.__amount = amount
        # maybe the password will be added here
        self.__transactions = transactions if transactions is not None else []

    @classmethod
    def create_account(cls, id: int, initial_amount: float) -> 'BudgetManager':
        """Creates a new account with file on the disk and an object in Python memory"""
        create_budget_files(id, initial_amount)

        return cls(id, initial_amount)

    @classmethod
    def load_account(cls, id: int) -> "BudgetManager":
        """Loads an already registered account from disk"""
        amount = show_budget(id)
        transactions = read_transactions(id)
        return cls(id, amount, transactions)



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


    def transfer(self, amount: float, addressee: 'BudgetManager', description=None) -> 'Transaction':
        date_record = datetime.now().replace(microsecond=0)

        if amount <= 0:
            print('invalid amount.')
            return None
        if amount > self.amount:
            print('not enough balace.')
            return None

        self.amount -= amount
        addressee.amount += amount

        transaction = Transaction(amount, description, self.id, addressee.id, date_record)
        self.__transactions.append(transaction)

        addressee.transactions.append(transaction)

        renew_budget_files(transaction)

        add_new_transaction(transaction, self.id)
        add_new_transaction(transaction, addressee.id)
        return transaction



if '__main__' == __name__:
    my_budget = BudgetManager.create_account(id=5, initial_amount=1000.0)

    my_new_budget = BudgetManager.create_account(id=6, initial_amount=500.0)

    budget1 = BudgetManager.load_account(1)
    budget2 = BudgetManager.load_account(2)

    budget1.transfer(10, budget2)










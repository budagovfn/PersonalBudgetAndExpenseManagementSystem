from Transaction import Transaction
from Utils import *


class BudgetManager:
    def __init__(self, id, amount, transactions):
        self.__id = id
        self.__amount = amount
        # maybe the password will be added here
        self.__transactions = transactions

    @classmethod
    def create_account(cls, id: int, initial_amount: float) -> 'BudgetManager':
        """Creates a new account with file on the disk and an object in Python memory"""
        create_budget_files(id, initial_amount)
        return cls(id, initial_amount)

    @classmethod
    def load_account(cls, id: int) -> 'BudgetManager':
        """Loads an already registered account from disk"""
        amount = show_budget(id)



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


    def transfer(self, amount: float, addressee: 'BudgetManager') -> 'Transaction':
        if amount <= 0:
            print('invalid amount.')
            return None
        if amount > self.amount:
            print('not enough balace.')
            return None

        self.amount -= amount
        addressee.amount += amount

        description = f"User {self.id} transfered to user {addressee.id} "

        return Transaction(amount, addressee)






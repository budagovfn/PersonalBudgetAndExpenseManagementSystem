'''
THE STRUCTURE OF CSV FILE WITH TRANSACTIONS:
| Datetime | ID of Addressee/Sender | Sent/Received | Amount (negative if sent) | Description |
'''

import os

from Transaction import Transaction

GLOBAL_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(GLOBAL_DIR, 'data')
# the path of core directory in which all clients data stored

def create_budget_files(id: int, initial_amount: float) -> None:
    dir_path = os.path.join(DATA_DIR, str(id))
    os.makedirs(dir_path, exist_ok=True)
    f_data = f"{id}_data.txt"
    f_transactions = f"{id}_transactions.csv"

    with open(os.path.join(dir_path, f_data), 'w') as file:
        file.write(f"funds: {initial_amount}\n")

    with open(os.path.join(dir_path, f_transactions), 'w') as file:
        pass
        # nothing to write. just create a file

def renew_budget_files(id: int, transaction: Transaction) -> None:
    dir_path = os.path.join(DATA_DIR, str(id))
    f_data = f"{id}_data.txt"
    f_transactions = f"{id}_transactions.csv"

    # to store information, we need to know whether we receive or send:
    client = transaction.addressee if id == transaction.sender else transaction.sender
    amount = -transaction.amount if id == transaction.sender else transaction.amount

    with open(os.path.join(dir_path, f_data), 'w') as file:
        curr_amount = 0
        new_amount = 0 # TODO!
        file.write(f"funds: {new_amount}\n")

    with open(os.path.join(dir_path, f_transactions), 'a') as file:
        new_entry = f"{transaction.date},{client}" # TODO!
    pass

if __name__ == "__main__":
    create_budget_files(1, 100)


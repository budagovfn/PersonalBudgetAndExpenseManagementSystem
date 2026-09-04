'''
    NEW CSV STRUCTURE:
    | Datetime | Sender ID | Addressee ID | Amount | Description |
    '''

import os
from typing import List
from Transaction import Transaction

GLOBAL_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(GLOBAL_DIR, 'data')
# the path of core directory in which all clients data stored

def create_budget_files(id: int, initial_amount: float) -> None:
    global DATA_DIR
    dir_path = os.path.join(DATA_DIR, str(id))
    os.makedirs(dir_path, exist_ok=True)
    f_data = f"{id}_data.txt"
    f_transactions = f"{id}_transactions.csv"

    with open(os.path.join(dir_path, f_data), 'w') as file:
        file.write(f"funds: {initial_amount}\n")

    with open(os.path.join(dir_path, f_transactions), 'w') as file:
        pass
        # nothing to write. just create a file

def renew_budget_files(transaction: Transaction) -> None:
    global DATA_DIR

    sender_id = transaction.sender
    addressee_id = transaction.addressee
    amount = transaction.amount

    # 1. Renew the sender's data
    sender_current_funds = show_budget(sender_id)
    sender_updated_funds = sender_current_funds - amount # from other files we specified that one cannot transmit funds if he has not have enough, so there is no need for specification here.
    update_budget(sender_id, sender_updated_funds)


    # 2. Renew the addresse's data
    addressee_current_funds = show_budget(addressee_id)
    addressee_updataed_funds = addressee_current_funds + amount
    update_budget(addressee_id, addressee_updataed_funds)



def show_budget(id: int) -> float:
    ''' If we need to get amount of funds of some account'''
    global DATA_DIR
    dir_path = os.path.join(DATA_DIR, str(id))
    if not os.path.exists(dir_path):
        raise ValueError(f"User {id} does not exist.")

    f_data = f"{id}_data.txt"
    with open(os.path.join(dir_path, f_data), 'r') as file:
       string = file.read()
    string = string[7:]
    return float(string)

def update_budget(id: int, amount: float) -> None:
    ''' If we need to update amount of funds of some account'''
    global DATA_DIR
    dir_path = os.path.join(DATA_DIR, str(id))

    f_data = f"{id}_data.txt"
    with open(os.path.join(dir_path, f_data), 'w') as file:
        file.write(f"funds: {amount}\n")

def read_transactions(id: int) -> List[Transaction]:
    global DATA_DIR
    dir_path = os.path.join(DATA_DIR, str(id))
    f_transactions = f"{id}_transactions.csv"
    transactions = []

    if not os.path.exists(dir_path):
        raise ValueError(f"User {id} does not exist.")

    with open(os.path.join(dir_path, f_transactions), 'r') as file:
        for line in file:
            entry = line.strip()
            if not entry:
                continue # skip empty stirngs
            # TODO here something preprocesses the entry and returns it as several variables for transaction creation
            new_transaction = preprocess_line_to_transaction(entry)
            transactions.append(new_transaction)
    return transactions


def preprocess_line_to_transaction(line: str) -> Transaction:
    '''
    NEW CSV STRUCTURE:
    | Datetime | Sender ID | Addressee ID | Amount | Description |
    '''
    datetime, sender_id, addressee_id, amount, description = line.split(',')
    return Transaction(float(amount), description, sender_id, addressee_id, datetime)



if __name__ == "__main__":
    create_budget_files(1, 130)
    update_budget(1, 148)

    create_budget_files(2, 130)

    print(show_budget(1))



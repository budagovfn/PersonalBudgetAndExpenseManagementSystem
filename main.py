import time
import random
import os
import shutil # to delete files and folders
from datetime import datetime

from BudgetManager import BudgetManager

CAPTURE = '''  ____            _            _     __  __                                   
 | __ ) _   _  __| | __ _  ___| |_  |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
 |  _ \| | | |/ _` |/ _` |/ _ \ __| | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |_) | |_| | (_| | (_| |  __/ |_  | |  | | (_| | | | | (_| | (_| |  __/ |   
 |____/ \__,_|\__,_|\__, |\___|\__| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                    |___/                                     |___/           '''
AUTHOR_NAME = "\t\t\t\t\t\t\t\t\t\t\t\t\tdeveloped by Farhad Budagov."
INSTRUCTIONS = """\t\tWelcome to BudgetManager console app — a project made for AI Academy. Here the instructions"
    PRESS FOLLOWING KEYS TO PROCEED WITH OPERATIONS:
                (1) — Create new budget
                (2) — Load already existing budget
                (3) — Transfer the fee from one budget to another
                (4) — Delete Budget account (must be 0 funds)
                (5) — Filter Transactions w.r.t. date
                
                (*) — Terminate and close
                """

def get_id_from_user():
    while True:
        try:
            budget = int(input("> Please enter the id"))
            return budget
        except ValueError:
            print(">Please enter a numeric value.")


def option_1():
    # new id creation. Every new id is just preious plus one
    path = "./data"

    # If there is no folder, deploy it
    if not os.path.exists(path):
        os.makedirs(path)

    ids = [int(f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f)) and f.isdigit()]
    if len(ids) == 0:
        id = 0
    else:
        id = max(ids) + 1

    while True:
        try:
            initial_amount = float(input("> Please enter the initial amount: "))
            if initial_amount <= 0:
                raise ValueError("Amount must be positive.")
            break
        except ValueError:
            print(">Please enter a numeric value.")


    new_budget = BudgetManager.create_account(id, initial_amount)
    print('Budget created successfully! ID: ' + str(new_budget.id))

def option_2():
    path = "./data"
    if not os.path.exists(path):
        print("> Data directory does not exist. Returning to main menu.")
        return
    budget_id = get_id_from_user()
    budget_path = os.path.join(path, str(budget_id))

    if not os.path.exists(budget_path):
        print("> Budget with this ID does not exist. Returning to main menu.")
        return

    try:
        budget = BudgetManager.load_account(budget_id)
        print(f"ID: {budget.id}")
        print(f"Budget amount: {budget.amount}")
        print(f"number of transactions: {len(budget.transactions)}")
    except Exception as e:
        print(f"> Error loading budget: {e}")


def option_3():
    path = "./data"
    print("Please select the budget")
    sender_id = get_id_from_user()
    print("Please enter the budget you want to transfer")
    addresee_id = get_id_from_user()

    try:
        sender = BudgetManager.load_account(sender_id)
        addressee = BudgetManager.load_account(addresee_id)
    except Exception as e:
        print(f"> Error loading budget: {e}")
        return

    while True:
        try:
            budget = float(input("> Please enter the amount of money to transfer: "))
            break
        except ValueError:
            print(">Please enter a numeric value.")

    description = input("> Enter the description").replace(",", "") # I use csv so delete commas


    transaction = sender.transfer(budget, addressee, description if description else "")
    if transaction is None:
        print("> Transaction failed. Not enough balance. Returning to main menu.")
    else:
        print("> Transaction successful.")






def option_4():
    path = "./data"
    if not os.path.exists(path):
        print("> Data directory does not exist.")
        return

    while True:
        try:
            budget_id = int(input("> Please enter the ID of the budget to delete: "))
            break
        except ValueError:
            print("> Please enter a numeric value.")

    budget_path = os.path.join(path, str(budget_id))
    if not os.path.exists(budget_path):
        print("> Budget with this ID does not exist.")
        return

    try:
        budget = BudgetManager.load_account(budget_id)
        if budget.amount == 0:
            shutil.rmtree(budget_path)
            print(f"> Budget {budget_id} successfully deleted.")
        else:
            print(f"> Cannot delete. Budget balance is {budget.amount}, must be 0.")
    except Exception as e:
        print(f"> Error deleting budget: {e}")


def option_5():
    path = "./data"
    if not os.path.exists(path):
        print("> Data directory does not exist.")
        return

    budget_id = get_id_from_user()
    budget_path = os.path.join(path, str(budget_id))
    if not os.path.exists(budget_path):
        print("> Budget with this ID does not exist.")
        return

    try:
        budget = BudgetManager.load_account(budget_id)
        if not budget.transactions:
            print("> No transactions found for this budget.")
            return
    except Exception as e:
        print(f"> Error loading budget: {e}")
        return

    print("> Enter date range for filtering (Format: YYYY-MM-DD)")
    start_date_str = input("> Enter start date (or leave empty for no lower limit): ").strip()
    end_date_str = input("> Enter end date (or leave empty for no upper limit): ").strip()

    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d") if start_date_str else datetime.min
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d") if end_date_str else datetime.max
        # if only date of finish without time, take all day till the end
        if end_date_str:
            end_date = end_date.replace(hour=23, minute=59, second=59)
    except ValueError:
        print("> Invalid date format. Please use YYYY-MM-DD.")
        return

    print(
        f"\nTransactions for Budget {budget_id} from {start_date_str or 'beginning'} to {end_date_str or 'now'} ---")

    count = 0
    for tx in budget.transactions:
        # lead to datetime for correct comparison
        tx_date_val = tx.date
        if isinstance(tx_date_val, str):
            try:
                tx_date = datetime.strptime(tx_date_val.split('.')[0], "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    tx_date = datetime.strptime(tx_date_val, "%Y-%m-%d")
                except ValueError:
                    continue
        else:
            tx_date = tx_date_val

        if start_date <= tx_date <= end_date:
            print(
                f"Date: {tx.date} | Sender: {tx.sender} | Addressee: {tx.addressee} | Amount: {tx.amount} | Desc: {tx.description}")
            count += 1

    print(f"Total filtered transactions: {count}\n")

print(random.sample(range(0, 9), 6))
print(CAPTURE)
print("\t\t\t\t\t\t\t\t\t\t\t\t\tdeveloped by Farhad Budagov.")
print(INSTRUCTIONS)

while True:
    inp = input()

    if inp == "1":
        option_1()
        continue

    elif inp == "2":
        option_2()
        continue

    elif inp == "3":
        option_3()

    elif inp == "4":
        option_4()

    elif inp == "5":
        option_5()

    elif inp == "*":
        print(">See you again!")
        time.sleep(3)
        break


    else:
        print(">Invalid Input.")



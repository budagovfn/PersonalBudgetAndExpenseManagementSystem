import time

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
                
                (*) — Terminate and close
                """

print(CAPTURE)
print("\t\t\t\t\t\t\t\t\t\t\t\t\tdeveloped by Farhad Budagov.")
print(INSTRUCTIONS)


while True:
    inp = input()

    if inp == "1":
        continue

    elif inp == "2":
        continue

    elif inp == "3":
        continue

    elif inp == "*":
        print(">See you again!")
        time.sleep(3)
        break

    else:
        print(">Invalid Input.")
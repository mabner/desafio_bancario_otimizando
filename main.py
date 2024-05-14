"""Challenge: Creating a banking system"""


def menu():
    menu = """
    ========== Choose an option ==========
    [d] Deposit
    [w] Withdraw
    [s] Bank Statement
    [u] New user 
    [n] New account
    [a] List accounts
    [c] Close
    => """
    return input(menu)

# positional only parameters


def deposit(balance, amount, bank_statement, /):
    if amount > 0:
        balance += amount
        # adds transaction to bank statement
        bank_statement += f"Deposit: R$ {amount:.2f}\n"
        print(f"Deposit successful. Your new balance is R$ {balance:.2f}")
    else:
        print("Operation failed! Invalid amount.")

    return balance, bank_statement

# keyword only parameters


def withdraw(*, balance, amount, bank_statement, limit, withdraw_count, withdraw_count_limit):
    exceeded_balance = amount > balance

    exceeded_limit = amount > limit

    exceeded_withdrawals = withdraw_count >= withdraw_count_limit

    if exceeded_balance:
        print("Operation failed! Not enough balance.")

    elif exceeded_limit:
        print("Operation failed! Withdraw amount exceeds the limit.")

    elif exceeded_withdrawals:
        print("Operation failed! Daily withdrawals exceeded.")

    elif amount > 0:
        balance -= amount

        # adds transaction to bank statement
        bank_statement += f"Withdraw: R$ {amount:.2f}\n"
        withdraw_count += 1
        print(f"You have successfully withdrawn R$ {
              amount:.2f} from your account.")

    else:
        print("Operation failed! Invalid amount.")

    return balance, bank_statement


def show_bank_statement(balance, /, *, bank_statement):
    print("\n================ BANK STATEMENT ================")
    print("No transactions found." if not bank_statement else bank_statement)
    print(f"\nBalance: R$ {balance:.2f}")
    print("==================================================")


def create_user(users):
    cpf = input("Please type you CPF *numbers only*: ")
    user = find_user(cpf, users)

    if user:  # if user exists, error message, if not, continue
        print("CPF already in use.")
        return

    name = input("Please type yor full name: ")
    birth_date = input("Please type your date of birth *dd-mm-yyyy*: ")
    address = input(
        "Please type your full address *street, house n° - borough - city/state*: ")

    users.append({"name": name, "birth_date": birth_date,
                 "cpf": cpf, "address": address})

    print(f"User '{name}' create with success.")


def find_user(cpf, users):
    users_found = [user for user in users if user["cpf"] == cpf]
    return users_found[0] if users_found else None


def create_account(branch, account_number, users):
    cpf = input("Please type the user CPF: ")
    user = find_user(cpf, users)

    if user:
        print("Account created with success.")
        # user key to make sure an account only has one user
        return {"branch": branch, "account_number": account_number, "user": user}

    print(f"User with CPF {cpf} not found.")


def list_accounts(accounts):
    for account in accounts:
        line = f"""
            Branch: {account['branch']}
            Account: {account['account_number']}
            Account holder: {account['user']['name']}
        """

        print(line)


def main():
    WITHDRAW_COUNT_LIMIT = 3
    LIMIT = 500
    BRANCH = "0001"

    balance = 0.00
    bank_statement = ""
    withdraw_count = 0
    users = []
    accounts = []

    while True:

        option = menu()

        if option == "d":
            amount = float(input("Insert the amount to deposit: "))

            balance, bank_statement = deposit(balance, amount, bank_statement)

        elif option == "w":
            amount = float(input("Inform the amount to withdraw: "))

            balance, bank_statement = withdraw(
                balance=balance,
                amount=amount,
                bank_statement=bank_statement,
                limit=LIMIT,
                withdraw_count=withdraw_count,
                withdraw_count_limit=WITHDRAW_COUNT_LIMIT,
            )

        elif option == "s":
            show_bank_statement(balance, bank_statement=bank_statement)

        elif option == "u":
            create_user(users)

        elif option == "n":
            account_number = len(accounts) + 1
            account = create_account(BRANCH, account_number, users)

            if account:
                accounts.append(account)

        elif option == "a":
            list_accounts(accounts)

        elif option == "c":
            break

        else:
            print("Please select a valid option.")


main()

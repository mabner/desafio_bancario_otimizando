"""Challenge: Creating a banking system"""


def menu():
    menu = """
    ========== Choose an option ==========
    [d] Deposit
    [w] Withdraw
    [s] Bank Statement
    [n] New account
    [a] List accounts
    [u] New user 
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
    pass


def create_user(users):
    pass


def list_user(cpf, users):
    pass


def create_account(branch, account_number, users):
    pass


def list_accounts(accounts):
    pass


def main():
    WITHDRAW_COUNT_LIMIT = 3
    balance = 0.00
    LIMIT = 500
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
            print("\n================ BANK STATEMENT ================")
            print("No transactions found." if not bank_statement else bank_statement)
            print(f"\nBalance: R$ {balance:.2f}")
            print("==================================================")

        elif option == "c":
            break

        else:
            print("Please select a valid option.")


main()

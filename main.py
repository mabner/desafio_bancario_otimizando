menu = """

[d] Deposit
[w] Withdraw
[s] Bank Statement
[c] Close

=> """

balance = 0
limit = 500
bank_statement = ""
withdraw_count = 0
WITHDRAW_COUNT_LIMIT = 3

while True:

    option = input(menu)

    if option == "d":
        amount = float(input("Insert the amount do deposit: "))

        if amount > 0:
            balance += amount
            bank_statement += f"Deposit: R$ {amount:.2f}\n"

        else:
            print("The operation failed! The informed amount is invalid.")

    elif option == "w":
        amount = float(input("Inform the amount to withdraw: "))

        exceeded_balance = amount > balance

        exceeded_limit = amount > limit

        exceeded_withdrawals = withdraw_count >= WITHDRAW_COUNT_LIMIT

        if exceeded_balance:
            print("The operation failed! You don't have enough balance.")

        elif exceeded_limit:
            print("The operation failed! The withdraw amount exceeds the limit.")

        elif exceeded_withdrawals:
            print("The operation failed! Number of daily withdrawals exceeded.")

        elif amount > 0:
            balance -= amount
            bank_statement += f"Withdraw: R$ {amount:.2f}\n"
            withdraw_count += 1

        else:
            print("The operation failed! The informed amount is invalid.")

    elif option == "s":
        print("\n================ BANK STATEMENT ================")
        print("No transactions." if not bank_statement else bank_statement)
        print(f"\nBalance: R$ {balance:.2f}")
        print("==========================================")

    elif option == "c":
        break

    else:
        print("Invalid option, please choose again from the menu.")

menu = """

[d] Deposit
[w] Withdraw
[s] Bank Statement
[c] Close

=> """

balance = 0.00
limit = 500
bank_statement = ""
withdraw_count = 0
WITHDRAW_COUNT_LIMIT = 3

while True:

    option = input(menu)

    if option == "d":
        amount = float(input("Insert the amount to deposit: "))

        if amount > 0:
            balance += amount

            # adds transaction to bank statement
            bank_statement += f"Deposit: R$ {amount:.2f}\n"

        else:
            print("Operation failed! Invalid amount.")

    elif option == "w":
        amount = float(input("Inform the amount to withdraw: "))

        exceeded_balance = amount > balance

        exceeded_limit = amount > limit

        exceeded_withdrawals = withdraw_count >= WITHDRAW_COUNT_LIMIT

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

        else:
            print("Operation failed! Invalid amount.")

    elif option == "s":
        print("\n================ BANK STATEMENT ================")
        print("No transactions found." if not bank_statement else bank_statement)
        print(f"\nBalance: R$ {balance:.2f}")
        print("==================================================")

    elif option == "c":
        break

    else:
        print("Please select a valid option.")

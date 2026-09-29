# Bank Account Simulator
# 1st Semester Python Project
# Concepts used: variables, input/output, operators, type conversion,
# lists/dictionaries, if-else, loops, functions and a simple module.

import random


def create_account():
    print("\n----- Create Bank Account -----")
    name = input("Enter your name: ")
    pin = input("Set a 4-digit PIN: ")

    while len(pin) != 4 or not pin.isdigit():
        print("PIN should contain exactly 4 digits.")
        pin = input("Set a 4-digit PIN: ")

    account_number = random.randint(10000, 99999)

    account = {
        "name": name,
        "pin": pin,
        "account_number": account_number,
        "balance": 0.0,
        "transactions": []
    }

    print("\nAccount created successfully!")
    print("Your account number is:", account_number)
    return account


def login(account):
    print("\n----- Login -----")
    entered_account = input("Enter account number: ")
    entered_pin = input("Enter PIN: ")

    if entered_account == str(account["account_number"]) and entered_pin == account["pin"]:
        print("Login successful.")
        return True
    else:
        print("Wrong account number or PIN.")
        return False


def deposit(account):
    print("\n----- Deposit Money -----")

    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Amount should be greater than 0.")
        else:
            account["balance"] += amount
            account["transactions"].append("Deposited Rs. " + str(amount))
            print("Money deposited successfully.")
            print("Current balance: Rs.", account["balance"])

    except ValueError:
        print("Please enter a valid number.")


def withdraw(account):
    print("\n----- Withdraw Money -----")

    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Amount should be greater than 0.")
        elif amount > account["balance"]:
            print("Not enough balance.")
        else:
            account["balance"] -= amount
            account["transactions"].append("Withdrawn Rs. " + str(amount))
            print("Please collect your money.")
            print("Current balance: Rs.", account["balance"])

    except ValueError:
        print("Please enter a valid number.")


def check_balance(account):
    print("\n----- Account Balance -----")
    print("Account Holder:", account["name"])
    print("Account Number:", account["account_number"])
    print("Balance: Rs.", account["balance"])


def show_transactions(account):
    print("\n----- Transaction History -----")

    if len(account["transactions"]) == 0:
        print("No transactions yet.")
    else:
        for transaction in account["transactions"]:
            print("-", transaction)


def bank_menu(account):
    while True:
        print("\n========== BANK MENU ==========")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Logout")
        print("===============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            deposit(account)
        elif choice == "2":
            withdraw(account)
        elif choice == "3":
            check_balance(account)
        elif choice == "4":
            show_transactions(account)
        elif choice == "5":
            print("You have been logged out.")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    print("================================")
    print("       SIMPLE BANK SYSTEM")
    print("================================")

    account = None

    while True:
        print("\n----- Main Menu -----")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if account is None:
                account = create_account()
            else:
                print("An account has already been created.")

        elif choice == "2":
            if account is None:
                print("Please create an account first.")
            else:
                if login(account):
                    bank_menu(account)

        elif choice == "3":
            print("Thank you for using the Simple Bank System.")
            break

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


main()
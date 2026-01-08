
# banking_system_interactive.py

accounts = {}

# ---------------- ACCOUNT CREATION ----------------
def create_account():
    acc_num = input("Enter account number: ")
    name = input("Enter account holder name: ")
    pin = input("Set 4-digit PIN: ")
    balance = float(input("Enter initial balance: "))

    if acc_num in accounts:
        print("Account already exists!\n")
    else:
        accounts[acc_num] = {
            "name": name,
            "pin": pin,
            "balance": balance,
            "transactions": [f"Account created with balance {balance}"]
        }
        print(f"Account for {name} created successfully!\n")

# ---------------- PIN VERIFICATION ----------------
def verify_pin(acc_num):
    pin = input("Enter PIN: ")
    return accounts[acc_num]["pin"] == pin

# ---------------- CHANGE PIN ----------------
def change_pin():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        if verify_pin(acc_num):
            new_pin = input("Enter new PIN: ")
            confirm_pin = input("Confirm new PIN: ")

            if new_pin == confirm_pin:
                accounts[acc_num]["pin"] = new_pin
                accounts[acc_num]["transactions"].append("PIN changed successfully")
                print("PIN changed successfully!\n")
            else:
                print("PIN mismatch!\n")
        else:
            print("Incorrect PIN!\n")
    else:
        print("Account not found!\n")

# ---------------- DEPOSIT ----------------
def deposit():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        if verify_pin(acc_num):
            amount = float(input("Enter amount to deposit: "))
            accounts[acc_num]["balance"] += amount
            accounts[acc_num]["transactions"].append(f"Deposited {amount}")
            print(f"Deposited {amount}. New balance: {accounts[acc_num]['balance']}\n")
        else:
            print("Incorrect PIN!\n")
    else:
        print("Account not found!\n")

# ---------------- WITHDRAW ----------------
def withdraw():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        if verify_pin(acc_num):
            amount = float(input("Enter amount to withdraw: "))
            if accounts[acc_num]["balance"] >= amount:
                accounts[acc_num]["balance"] -= amount
                accounts[acc_num]["transactions"].append(f"Withdrew {amount}")
                print(f"Withdrawn {amount}. New balance: {accounts[acc_num]['balance']}\n")
            else:
                print("Insufficient balance!\n")
        else:
            print("Incorrect PIN!\n")
    else:
        print("Account not found!\n")

# ---------------- DISPLAY ACCOUNTS ----------------
def display_accounts():
    if not accounts:
        print("No accounts available.\n")
    else:
        print("\nAll Accounts:")
        for acc_num, info in accounts.items():
            print(f"Account No: {acc_num}, Name: {info['name']}, Balance: {info['balance']}")
        print()

# ---------------- TRANSACTION HISTORY ----------------
def show_transaction_history():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        if verify_pin(acc_num):
            print("\nTransaction History:")
            for txn in accounts[acc_num]["transactions"]:
                print("-", txn)
            print()
        else:
            print("Incorrect PIN!\n")
    else:
        print("Account not found!\n")

# ---------------- TRANSFER MONEY ----------------
def transfer_money():
    sender = input("Enter sender account number: ")
    receiver = input("Enter receiver account number: ")

    if sender in accounts and receiver in accounts:
        if verify_pin(sender):
            amount = float(input("Enter amount to transfer: "))
            if accounts[sender]["balance"] >= amount:
                accounts[sender]["balance"] -= amount
                accounts[receiver]["balance"] += amount

                accounts[sender]["transactions"].append(
                    f"Transferred {amount} to {receiver}"
                )
                accounts[receiver]["transactions"].append(
                    f"Received {amount} from {sender}"
                )

                print("\nTransfer Successful")
                print("Sender Balance:", accounts[sender]["balance"])
                print("Receiver Balance:", accounts[receiver]["balance"])
            else:
                print("\nInsufficient Balance")
        else:
            print("\nIncorrect PIN")
    else:
        print("\nInvalid Account Number")

# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("=== Banking System Menu ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Accounts")
        print("5. Transaction History")
        print("6. Transfer Money")
        print("7. Change PIN")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            display_accounts()
        elif choice == "5":
            show_transaction_history()
        elif choice == "6":
            transfer_money()
        elif choice == "7":
            change_pin()
        elif choice == "8":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.\n")

# ---------------- RUN PROGRAM ----------------
if __name__ == "__main__":
    main()


# banking_system_interactive.py

# Dictionary to store account info
accounts = {}

# Function to create a new account
def create_account():
    acc_num = input("Enter account number: ")
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    
    if acc_num in accounts:
        print("Account already exists!\n")
    else:
        accounts[acc_num] = {
            "name": name,
            "balance": balance,
            "transactions": [f"Account created with balance {balance}"]
        }
        print(f"Account for {name} created successfully!\n")

# Function to deposit money
def deposit():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_num]["balance"] += amount
        accounts[acc_num]["transactions"].append(f"Deposited {amount}")
        print(f"Deposited {amount}. New balance: {accounts[acc_num]['balance']}\n")
    else:
        print("Account not found!\n")

# Function to withdraw money
def withdraw():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if accounts[acc_num]["balance"] >= amount:
            accounts[acc_num]["balance"] -= amount
            accounts[acc_num]["transactions"].append(f"Withdrew {amount}")
            print(f"Withdrawn {amount}. New balance: {accounts[acc_num]['balance']}\n")
        else:
            print("Insufficient balance!\n")
    else:
        print("Account not found!\n")

# Function to display all accounts
def display_accounts():
    if not accounts:
        print("No accounts available.\n")
    else:
        print("\nAll Accounts:")
        for acc_num, info in accounts.items():
            print(f"Account No: {acc_num}, Name: {info['name']}, Balance: {info['balance']}")
        print()

# Function to display transaction history
def show_transaction_history():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        print("\nTransaction History:")
        for txn in accounts[acc_num]["transactions"]:
            print("-", txn)
        print()
    else:
        print("Account not found!\n")

# Function to transfer money between accounts
def transfer_money():
    sender = input("Enter sender account number: ")
    receiver = input("Enter receiver account number: ")
    amount = float(input("Enter amount to transfer: "))

    if sender in accounts and receiver in accounts:
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
        print("\nInvalid Account Number")

# Function to check balance
def check_balance():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        print(f"Account Balance for {accounts[acc_num]['name']}: {accounts[acc_num]['balance']}\n")
    else:
        print("Account not found!\n")

# MAIN MENU
def main():
    while True:
        print("=== Banking System Menu ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Accounts")
        print("5. Transaction History")
        print("6. Transfer Money")
        print("7. Exit")
        print("8. Check Balance")  # New feature
        
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
            print("Exiting... Thank you!")
            break
        elif choice == "8":
            check_balance()
        else:
            print("Invalid choice! Try again.\n")

# Run the program
if __name__ == "__main__":
    main()

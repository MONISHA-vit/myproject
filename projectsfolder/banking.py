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
        accounts[acc_num] = {"name": name, "balance": balance}
        print(f"Account for {name} created successfully!\n")

# Function to deposit money
def deposit():
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_num]["balance"] += amount
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

# Main menu
def main():
    while True:
        print("=== Banking System Menu ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Accounts")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            display_accounts()
        elif choice == "5":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run the program
if __name__ == "__main__":
    main()

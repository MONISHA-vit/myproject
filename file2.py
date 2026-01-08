class BankAccount:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("\n--- Account Details ---")
        print("Name:", self.name)
        print("Account Number:", self.acc_no)
        print("Current Balance: ₹", self.balance)


# Main Program
name = input("Enter account holder name: ")
acc_no = input("Enter account number: ")

account = BankAccount(name, acc_no)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)

    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)

    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        print("Thank you for using our banking system.")
        break

    else:
        print("Invalid choice. Try again.")


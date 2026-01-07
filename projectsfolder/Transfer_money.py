class Bank:
    def __init__(self):
        self.accounts = {
            1001: {"name": "Monisha", "balance": 9000},
            1002: {"name": "Likitha", "balance": 7000},
            1003: {"name": "Tejasree", "balance": 12000},
            1004: {"name": "Kavya", "balance": 6000},
            1005: {"name": "Monica", "balance": 10000}
        }

    def show_accounts(self):
        print("\nAccount Details:")
        for acc, data in self.accounts.items():
            print(acc, data["name"], data["balance"])

    def transfer_money(self):
        sender = int(input("\nEnter sender account number: "))
        receiver = int(input("Enter receiver account number: "))
        amount = float(input("Enter amount to transfer: "))

        if sender in self.accounts and receiver in self.accounts:
            if self.accounts[sender]["balance"] >= amount:
                self.accounts[sender]["balance"] -= amount
                self.accounts[receiver]["balance"] += amount
                print("\nTransfer Successful")
                print("Sender Balance:", self.accounts[sender]["balance"])
                print("Receiver Balance:", self.accounts[receiver]["balance"])
            else:
                print("\nInsufficient Balance")
        else:
            print("\nInvalid Account Number")

    def menu(self):
        while True:
            print("\n--- Bank Menu ---")
            print("1. View Accounts")
            print("2. Transfer Money")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.show_accounts()
            elif choice == '2':
                self.transfer_money()
            elif choice == '3':
                print("Thank You")
                break
            else:
                print("Invalid Choice")


bank = Bank()
bank.menu()

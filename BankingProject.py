class BankAccount:
    def __init__(self, account_number, pin, balance=0.0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def login(self, account_number, pin):
        if self.account_number == account_number and self.pin == pin:
            print("Login successful!")
            return True
        else:
            print("Invalid account number or PIN.")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
            self.show_balance()
        else:
            print("Invalid amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Amount withdrawn successfully.")
                self.show_balance()
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount. Please enter a positive value.")

    def show_balance(self):
        print("Current balance: $", self.balance)


# Create a bank account
account = BankAccount("123456789", "1234", 1000.0)

# Login to the account
account_number = input("Enter account number: ")
pin = input("Enter PIN: ")
if account.login(account_number, pin):
    while True:
        print("\nBanking Options:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.show_balance()
        elif choice == "4":
            print("Thank you for using our banking system.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

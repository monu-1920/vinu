class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}.")

    def show_transaction_history(self):
        print("Transaction History:")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for transaction in self.transaction_history:
                print(transaction)

def main():
    print("Welcome to the Bank!")
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder's name: ")
    account = BankAccount(account_number, account_holder)

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Show Transaction History")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            account.show_transaction_history()
        elif choice == '5':
            print("Thank you for using the bank system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

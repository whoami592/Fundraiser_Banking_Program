# Fundraiser Banking Program
# Coded by Pakistani Ethical Hacker Mr Sabaz Ali Khan
# A simple Python program for managing fundraiser accounts with basic banking features

import os
import pickle
from datetime import datetime

class FundraiserBank:
    def __init__(self):
        self.accounts = {}
        self.filename = "fundraiser_accounts.pkl"
        self.load_accounts()

    def load_accounts(self):
        """Load accounts from file if it exists"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'rb') as file:
                    self.accounts = pickle.load(file)
            except:
                print("Error loading accounts. Starting fresh.")

    def save_accounts(self):
        """Save accounts to file"""
        try:
            with open(self.filename, 'wb') as file:
                pickle.dump(self.accounts, file)
        except:
            print("Error saving accounts.")

    def create_account(self, name, initial_donation=0):
        """Create a new account with an initial donation"""
        if name in self.accounts:
            print("Account already exists!")
            return
        if initial_donation < 0:
            print("Initial donation cannot be negative!")
            return
        account_id = len(self.accounts) + 1
        self.accounts[name] = {
            'id': account_id,
            'balance': initial_donation,
            'transactions': [(datetime.now(), "Initial Donation", initial_donation)]
        }
        self.save_accounts()
        print(f"Account created for {name} with ID {account_id} and initial donation of ${initial_donation}")

    def deposit(self, name, amount):
        """Deposit money into an account"""
        if name not in self.accounts:
            print("Account not found!")
            return
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.accounts[name]['balance'] += amount
        self.accounts[name]['transactions'].append((datetime.now(), "Deposit", amount))
        self.save_accounts()
        print(f"Deposited ${amount} to {name}'s account. New balance: ${self.accounts[name]['balance']}")

    def withdraw(self, name, amount):
        """Withdraw money from an account"""
        if name not in self.accounts:
            print("Account not found!")
            return
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if self.accounts[name]['balance'] < amount:
            print("Insufficient funds!")
            return
        self.accounts[name]['balance'] -= amount
        self.accounts[name]['transactions'].append((datetime.now(), "Withdrawal", -amount))
        self.save_accounts()
        print(f"Withdrew ${amount} from {name}'s account. New balance: ${self.accounts[name]['balance']}")

    def check_balance(self, name):
        """Check the balance of an account"""
        if name not in self.accounts:
            print("Account not found!")
            return
        print(f"Balance for {name}: ${self.accounts[name]['balance']}")

    def view_transactions(self, name):
        """View transaction history for an account"""
        if name not in self.accounts:
            print("Account not found!")
            return
        print(f"Transaction history for {name}:")
        for date, type, amount in self.accounts[name]['transactions']:
            print(f"{date.strftime('%Y-%m-%d %H:%M:%S')} | {type} | ${amount}")

def main():
    bank = FundraiserBank()
    print("Welcome to the Fundraiser Banking Program by Mr Sabaz Ali Khan")
    
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit Donation")
        print("3. Withdraw Donation")
        print("4. Check Balance")
        print("5. View Transactions")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter donor name: ")
            try:
                initial_donation = float(input("Enter initial donation amount (0 or more): "))
                bank.create_account(name, initial_donation)
            except ValueError:
                print("Invalid amount! Please enter a number.")
                
        elif choice == '2':
            name = input("Enter donor name: ")
            try:
                amount = float(input("Enter deposit amount: "))
                bank.deposit(name, amount)
            except ValueError:
                print("Invalid amount! Please enter a number.")
                
        elif choice == '3':
            name = input("Enter donor name: ")
            try:
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw(name, amount)
            except ValueError:
                print("Invalid amount! Please enter a number.")
                
        elif choice == '4':
            name = input("Enter donor name: ")
            bank.check_balance(name)
            
        elif choice == '5':
            name = input("Enter donor name: ")
            bank.view_transactions(name)
            
        elif choice == '6':
            print("Thank you for using the Fundraiser Banking Program!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
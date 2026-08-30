# Bank Management Project

import json
import random
import string
from pathlib import Path


class Bank:

    database = "Data.json"
    data = []

    # Load data from JSON file
    @classmethod
    def loadData(cls):
        try:
            if Path(cls.database).exists():
                with open(cls.database, "r") as fs:
                    content = fs.read()

                    if content.strip():
                        cls.data = json.loads(content)
                    else:
                        cls.data = []

            else:
                cls.data = []
                with open(cls.database, "w") as fs:
                    json.dump(cls.data, fs)

        except Exception as err:
            print(f"Error while loading data: {err}")
            cls.data = []

    # Save data into JSON file
    @classmethod
    def update(cls):
        try:
            with open(cls.database, "w") as fs:
                json.dump(cls.data, fs, indent=4)

        except Exception as err:
            print(f"Error while saving data: {err}")

    # Generate account number
    @classmethod
    def accountGenerate(cls):

        alpha = random.choices(string.ascii_uppercase, k=3)
        num = random.choices(string.digits, k=5)

        accountNumber = alpha + num

        random.shuffle(accountNumber)

        return "".join(accountNumber)

    # Create Account
    def createAccount(self):

        try:
            name = input("Tell your name: ").strip()
            age = int(input("Tell your age: "))
            email = input("Tell your email: ").strip()
            pin = input("Tell your 4 digit PIN: ").strip()

            if age < 18:
                print("You must be 18 or above to create an account.")
                return

            if len(pin) != 4 or not pin.isdigit():
                print("PIN must contain exactly 4 digits.")
                return

            accountNumber = Bank.accountGenerate()

            info = {
                "name": name,
                "age": age,
                "email": email,
                "pin": int(pin),
                "accountNumber": accountNumber,
                "balance": 0
            }

            Bank.data.append(info)
            Bank.update()

            print("\nAccount created successfully!")

            print("\nYour Account Details:")

            for key, value in info.items():
                print(f"{key}: {value}")

            print("\nPlease note down your account number!")

        except ValueError:
            print("Please enter valid input.")

        except Exception as err:
            print(f"An error occurred: {err}")

    # Deposit Money
    def depositMoney(self):

        try:
            accnumber = input("Enter your account number: ").strip()
            pin = int(input("Enter your PIN: "))

            userData = [
                user for user in Bank.data
                if user["accountNumber"] == accnumber
                and user["pin"] == pin
            ]

            if not userData:
                print("Sorry, account not found.")
                return

            amount = int(input("How much money do you want to deposit: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                return

            if amount > 10000:
                print("You can deposit a maximum of 10,000 at once.")
                return

            userData[0]["balance"] += amount

            Bank.update()

            print("Amount deposited successfully!")
            print(f"Current Balance: {userData[0]['balance']}")

        except ValueError:
            print("Please enter valid numbers.")

        except Exception as err:
            print(f"An error occurred: {err}")

    # Withdraw Money
    def withdraw(self):

        try:
            accnumber = input("Enter your account number: ").strip()
            pin = int(input("Enter your PIN: "))

            userData = [
                user for user in Bank.data
                if user["accountNumber"] == accnumber
                and user["pin"] == pin
            ]

            if not userData:
                print("Sorry, account not found.")
                return

            amount = int(input("How much money do you want to withdraw: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                return

            if userData[0]["balance"] < amount:
                print("Insufficient balance.")
                return

            userData[0]["balance"] -= amount

            Bank.update()

            print("Amount withdrawn successfully!")
            print(f"Current Balance: {userData[0]['balance']}")

        except ValueError:
            print("Please enter valid numbers.")

        except Exception as err:
            print(f"An error occurred: {err}")

    # Show Details
    def showDetails(self):

        try:
            accnumber = input("Enter your account number: ").strip()
            pin = int(input("Enter your PIN: "))

            userData = [
                user for user in Bank.data
                if user["accountNumber"] == accnumber
                and user["pin"] == pin
            ]

            if not userData:
                print("No such user found.")
                return

            print("\n----- YOUR ACCOUNT DETAILS -----")

            for key, value in userData[0].items():

                if key == "pin":
                    print(f"{key}: ****")
                else:
                    print(f"{key}: {value}")

        except ValueError:
            print("Please enter a valid PIN.")

        except Exception as err:
            print(f"An error occurred: {err}")

    # Update Details
    def updateDetails(self):

        try:
            accnumber = input("Enter your account number: ").strip()
            pin = int(input("Enter your PIN: "))

            userData = [
                user for user in Bank.data
                if user["accountNumber"] == accnumber
                and user["pin"] == pin
            ]

            if not userData:
                print("No such user found.")
                return

            user = userData[0]

            print("\nYou cannot change:")
            print("Age, Account Number and Balance")

            print("\nLeave empty if you don't want to change anything.")

            newName = input("Enter new name: ").strip()
            newEmail = input("Enter new email: ").strip()
            newPin = input("Enter new PIN: ").strip()

            if newName:
                user["name"] = newName

            if newEmail:
                user["email"] = newEmail

            if newPin:

                if len(newPin) != 4 or not newPin.isdigit():
                    print("PIN must contain exactly 4 digits.")
                    return

                user["pin"] = int(newPin)

            Bank.update()

            print("Details updated successfully!")

        except ValueError:
            print("Please enter valid input.")

        except Exception as err:
            print(f"An error occurred: {err}")

    # Delete Account
    def deleteAccount(self):

        try:
            accnumber = input("Enter your account number: ").strip()
            pin = int(input("Enter your PIN: "))

            userData = [
                user for user in Bank.data
                if user["accountNumber"] == accnumber
                and user["pin"] == pin
            ]

            if not userData:
                print("No such user found.")
                return

            check = input(
                "Press Y to confirm account deletion or N to cancel: "
            ).strip().lower()

            if check == "y":

                Bank.data.remove(userData[0])

                Bank.update()

                print("Account deleted successfully!")

            else:
                print("Account deletion cancelled.")

        except ValueError:
            print("Please enter a valid PIN.")

        except Exception as err:
            print(f"An error occurred: {err}")


# Load existing data
Bank.loadData()

user = Bank()


# Main Program
while True:

    print("\n========== BANK MANAGEMENT SYSTEM ==========")

    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Show Details")
    print("5. Update Details")
    print("6. Delete Account")
    print("7. Exit")

    try:

        check = int(input("\nEnter your response: "))

        if check == 1:
            user.createAccount()

        elif check == 2:
            user.depositMoney()

        elif check == 3:
            user.withdraw()

        elif check == 4:
            user.showDetails()

        elif check == 5:
            user.updateDetails()

        elif check == 6:
            user.deleteAccount()

        elif check == 7:
            print("Thank you for using Bank Management System!")
            break

        else:
            print("Invalid option. Please choose between 1 and 7.")

    except ValueError:
        print("Please enter a valid number.")
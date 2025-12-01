balance = 5000
pin = int(input("Create pin:"))
attempts = 3
print("---Welcome To ATM---")
while attempts > 0:
    enter_pin = int(input("Enput your pin: "))
    if enter_pin == pin:
        print("\n/Login Successfull!")
        break
    else:
        attempts -= 1
        print("Incorrect PIN! Attempts left:", attempts)

        if attempts == 0:
            print("Card Blocked Due To 3 Wrong Attempts!")
            exit()
while True:
    print("""
    1. Check Balance
    2. Deposit Money
    3. Cash Withraw
    4. UPI Transaction
    5. Exit
    """)
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        print("Your Balance Is: ", balance)
    elif choice == "2":
        amount = float(input("Enter Amount To Deposit: "))
        balance += amount
        print("Amount Deposited Successfully")
        print("Updated Balance: ", balance)
    elif choice == "3":
        amount = float(input("Enter Amount To Withraw: "))
        if amount > balance:
            print("Insufficient Balance!")
        else:
            balance -= amount
            print("Amount Withdrawn Successfully!")
            print("Remaining Balance:", balance)
    elif choice == "4":
        print("\n----- Transfer Money -----")
        print("UPI Transfer")
        amount = float(input("Enter amount to transfer: "))
        if amount > balance:
            print("Insufficient Balance!")
        else:
            upi = input("Enter UPI ID: ")
            balance -= amount
            print(f"Successfully transferred ₹{amount} to {upi} via UPI!")
            print("Remaining Balance:", balance)
    elif choice == "5":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")

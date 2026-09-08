balance = 0


def deposit(amount):
    global balance

    if amount > 0:
        balance += amount
        print("Deposit successful")
    else:
        print("Invalid amount")


def withdraw(amount):
    global balance

    if amount <= 0:
        print("Invalid amount")

    elif amount <= balance:
        balance -= amount
        print("Withdrawal successful")

    else:
        print("Insufficient balance")


def check_balance():
    print("Balance:", balance)
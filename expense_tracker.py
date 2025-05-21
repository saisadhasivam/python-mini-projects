"""
Expense Tracker - A command-line budget tracker using a dictionary.

Allows users to add expenses by category and view total spending.
"""

# Dictionary to store expenses by category
expenses = {}

# App menu loop
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses by Category")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        category = input("Enter category (e.g., Food, Rent): ")
        try:
            amount = float(input("Enter amount: ₹"))
            if category in expenses:
                expenses[category] += amount
            else:
                expenses[category] = amount
            print("Expense recorded.")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    elif choice == "2":
        print("\nExpenses by Category:")
        if not expenses:
            print("No expenses recorded yet.")
        else:
            for category, amount in expenses.items():
                print(f"{category}: ₹{amount:.2f}")

    elif choice == "3":
        total = sum(expenses.values())
        print(f"\nTotal Expenses: ₹{total:.2f}")

    elif choice == "4":
        print("Exiting Expense Tracker.")
        break

    else:
        print("Invalid choice. Try again.")

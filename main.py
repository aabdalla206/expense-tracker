from expense_tracker import add_expense, view_expenses, edit_expense, delete_expense
import database

def main():
    database.setup_database()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            add_expense(amount, category, date, description)
            print("Expense added!")

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            expense_id = int(input("Enter the expense ID to edit: "))
            new_amount = float(input("Enter new amount: "))
            new_category = input("Enter new category: ")
            new_date = input("Enter new date (YYYY-MM-DD): ")
            new_description = input("Enter new description: ")
            edit_expense(expense_id, new_amount, new_category, new_date, new_description)
            print("Expense updated!")

        elif choice == '4':
            expense_id = int(input("Enter the expense ID to delete: "))
            delete_expense(expense_id)
            print("Expense deleted!")

        elif choice == '5':
            break

        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
    database.close_connection()

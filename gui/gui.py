import tkinter as tk
from expense_tracker import add_expense, view_expenses

# Function to add expense from GUI input
def add_expense_gui():
    amount = float(amount_entry.get())
    category = category_entry.get()
    date = date_entry.get()
    description = description_entry.get()
    add_expense(amount, category, date, description)
    print("Expense added!")
    clear_entries()

# Function to clear entry fields
def clear_entries():
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

# Setting up the main window
root = tk.Tk()
root.title("Expense Tracker")

# Creating input fields
tk.Label(root, text="Amount").grid(row=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="Category").grid(row=1)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=2)
date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1)

tk.Label(root, text="Description").grid(row=3)
description_entry = tk.Entry(root)
description_entry.grid(row=3, column=1)

# Adding buttons
tk.Button(root, text='Add Expense', command=add_expense_gui).grid(row=4, column=0, pady=4)
tk.Button(root, text='Quit', command=root.quit).grid(row=4, column=1, pady=4)

# Starting the main loop
root.mainloop()
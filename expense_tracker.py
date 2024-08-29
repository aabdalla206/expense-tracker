import database

def add_expense(amount, category, date, description):
    query = '''
    INSERT INTO expenses (amount, category, date, description)
    VALUES (?, ?, ?, ?)
    '''
    params = (amount, category, date, description)
    database.execute_query(query, params)

def view_expenses():
    query = 'SELECT * FROM expenses'
    expenses = database.fetch_all(query)
    for expense in expenses:
        print(expense)

def edit_expense(expense_id, new_amount, new_category, new_date, new_description):
    query = '''
    UPDATE expenses
    SET amount = ?, category = ?, date = ?, description = ?
    WHERE id = ?
    '''
    params = (new_amount, new_category, new_date, new_description, expense_id)
    database.execute_query(query, params)

def delete_expense(expense_id):
    query = 'DELETE FROM expenses WHERE id = ?'
    params = (expense_id,)
    database.execute_query(query, params)

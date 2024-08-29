import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

def setup_database():
    # Create table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        amount REAL,
        category TEXT,
        date TEXT,
        description TEXT
    )
    ''')
    conn.commit()

def execute_query(query, params=()):
    cursor.execute(query, params)
    conn.commit()

def fetch_all(query, params=()):
    cursor.execute(query, params)
    return cursor.fetchall()

def close_connection():
    conn.close()

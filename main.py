import sqlite3

# Initialize database
con = sqlite3.connect("task_manager.db")
cur = con.cursor()

# Create table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS expense_tracker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,          -- Name of the transaction (Income or Expense)
    category TEXT,               -- Category of the expense (optional for income)
    income DECIMAL DEFAULT 0.0,
    amount DECIMAL DEFAULT 0.0,  -- Amount of income (for income entries)
    expenses DECIMAL DEFAULT 0.0, -- Expense 
    description TEXT,   -- Description of the transaction
    date DATE -- Date of the transaction
);

""")


def menu():
    print('\n==================')
    print(' Expense Tracker')
    print('==================\n')
    print('1. Add data')
    print('2. Display Records')    
    user_input = input("Choose an option: ")

    if not user_input.isdigit() or int(user_input) not in range(1, 4):
        print('Invalid option, Please choose a number between 1 and 3.')
    else:
        process_input(int(user_input))



def process_input(user_input):
    if user_input == 1:
        add_data()
    elif user_input == 2:
        display_income()



def add_data():
    type_ = input('Enter category (Income / Expense): ').strip().capitalize()
    
    if type_ not in ['Income', 'Expense']:
        print("Invalid category. Please enter 'Income' or 'Expense'.")
        return

    amount = input('Enter amount: ').strip()
    if not amount.isdigit():
        print("Invalid amount. Please enter a numeric value.")
        return

    category = input(f'Enter category - e.g., {"Salary" if type_ == "Income" else "Utilities"}: ').strip()
    description = input('Description: ').strip()
    date = input('Enter the date (YYYY-MM-DD) or press Enter to use the current date: ').strip()

    # Validate and set date to current date if not provided
    if not date:
        from datetime import datetime
        date = datetime.now().strftime('%Y-%m-%d')

    try:
        if type_ == 'Income':
            # Insert income data
            cur.execute('INSERT INTO expense_tracker (income, category, description, date) VALUES (?, ?, ?, ?)', 
                        (float(amount), category, description, date))
        else:  # Expense
            # Insert expense data
            cur.execute('INSERT INTO expense_tracker (expenses, category, description, date) VALUES (?, ?, ?, ?)', 
                        (float(amount), category, description, date))
        
        con.commit()
        print(f"{type_} added successfully!\n")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


 

def display_income():
    try:
        # Query the database to fetch only income records (where income > 0)
        cur.execute("SELECT id, income, category, description, date FROM expense_tracker WHERE income > 0")
        rows = cur.fetchall()

        # Check if there are any income records
        if rows:
            print("\nID | Amount   | Category      | Date          | Description")
            print("-" * 70)  # Line to separate the header from the data

            for row in rows: # Loop through each row and display in the desired format
                print(f"{row[0]:<3}| €{row[1]:<8}| {row[2]:<11}   | {row[4]:<12}  | {row[3]}")

        else:
            print("No income records found.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    



def main():
    while True:
        menu() 

if __name__ == '__main__':
    main()


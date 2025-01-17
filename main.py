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
    income DECIMAL DEFAULT 0.0,  -- Amount of income (for income entries)
    expenses DECIMAL DEFAULT 0.0, -- Expense 
    description TEXT,   -- Description of the transaction
    date DATE -- Date of the transaction
);

""")


def menu():
    print('\n==================')
    print(' Expense Tracker')
    print('==================\n')
    print('1. Add income')
    print('2. Add expenses')
    print('3. Display income')    
    user_input = input("Choose an option: ")

    if not user_input.isdigit() or int(user_input) not in range(1, 4):
        print('Invalid option, Please choose a number between 1 and 3.')
    else:
        process_input(int(user_input))



def process_input(user_input):
    if user_input == 1:
        add_income()
    elif user_input == 2:
        add_expenses()
    elif user_input == 3: 
        display_income()



def add_income():
    income = input('Enter amount: ')
    category = "Income"  # Hard-coded category value
    description = input('Description: ') 
    date = input('Enter the date (YYYY-MM-DD)')

    try:
        # Insert income data into the table
        cur.execute('INSERT INTO expense_tracker (income, category, description, date) VALUES (?, ?, ?, ? )', 
                    (float(income), category, description, date))
        con.commit()
        print("Income added successfully!\n")
        
        
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")



def display_income():
    try:
        # Query the database to fetch only income records (where income > 0)
        cur.execute("SELECT id, income, category, description, date FROM expense_tracker WHERE income > 0")
        rows = cur.fetchall()

        # Check if there are any income records
        if rows:
            print("\nID | Amount | Category  | Date            | Description")
            print("-" * 70)  # Line to separate the header from the data

            for row in rows: # Loop through each row and display in the desired format
                print(f"{row[0]:<3}  €{row[1]:<6}  {row[2]:<9}   {row[4]}        {row[3]}")
        else:
            print("No income records found.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    

def add_expenses():
    pass

 

def main():
    while True:
        menu() 

if __name__ == '__main__':
    main()



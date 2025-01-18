import sqlite3
import textwrap

# Initialize database
con = sqlite3.connect("task_manager.db")
cur = con.cursor()

# Create table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS expense_tracker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_type TEXT NOT NULL, -- 'Income' or 'Expense'
    subcategory TEXT,              -- Specific category, e.g., 'Salary', 'Groceries'
    amount DECIMAL NOT NULL,       -- Amount of the transaction
    description TEXT,              -- Description of the transaction
    date DATE NOT NULL             -- Date of the transaction
);

""")

# Prints menu function
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


# process the data entered by the user to call he right function
def process_input(user_input):
    if user_input == 1:
        add_data()
    elif user_input == 2:
        display_records()


# Function that asks the user for the infomration and adds the data to the database 
def add_data():
    transaction_type = input('Enter type (Income / Expense): ').strip().capitalize()
    if transaction_type not in ['Income', 'Expense']:
        print("Invalid category. Please enter 'Income' or 'Expense'.")
        return
    try:    # validate the input 
        amount = float(input('Enter amount: ').strip()) # converts the user input to a float and removes space
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    # prompts user to enter information
    subcategory = input(f'Enter subcategory  - e.g., {"Salary" if transaction_type == "Income" else "Utilities"}: ').strip()
    description = input('Description: ').strip()
    date = input('Enter the date (YYYY-MM-DD) or press Enter to use the current date: ').strip()

    # Validate and set date to current date if not provided
    if not date:
        from datetime import datetime
        date = datetime.now().strftime('%Y-%m-%d')
    
    # Stores data in a list
    data = [transaction_type, subcategory, amount, description, date]
    
    # insert into the database
    try:
        query = ''' INSERT INTO expense_tracker (transaction_type, subcategory, amount, description, date) VALUES (?,?,?,?,?)'''
        cur.execute(query, data)
        con.commit()
        print(f"{transaction_type} added successfully!\n")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


 

def display_records():
    try:
        # Query the database to fetch only income records
        cur.execute("SELECT id, transaction_type, subcategory, amount, date, description FROM expense_tracker")
        rows = cur.fetchall()

       # Check if there are any records to display
        if rows:
            # Print the header
            print("\nID | Transaction Type  | Subcategory     | Amount      | Date       | Description")
            print("-" * 80)

            # Loop through and display each record
            for row in rows:
                # Wrapping the description text to fit within a certain width
                wrapped_description = textwrap.fill(row[5], width=30)  # Wrap description to 30 characters

                # Print each row with proper alignment
                print(f"{row[0]:<3} | {row[1]:<16} | {row[2]:<15} | €{row[3]:<10.2f} | {row[4]:<10} | {wrapped_description}")

        else:
            print("No records found.")


    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    

def main():
    while True:
        menu() 

if __name__ == '__main__':
    main()


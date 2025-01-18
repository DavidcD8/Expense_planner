# Expense Tracker

An expense tracker application built with Python and SQLite to help you manage and track your income and expenses efficiently.

## Features

- Add and track **income** (e.g., salary, freelance work).
- Add and track **expenses** (e.g., utilities, groceries).
- Display all records of income and expenses in a neatly formatted table.
- Store data persistently using SQLite.
Use of textwrap for wrapping long descriptions in the display.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DavidcD8/Expense_planner.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Expense_planner
   ```
3. Run the application:
   ```bash
   python main.py
   ```
## Table Schema

The `expense_tracker` table is used to store transaction data:

| Column Name       | Data Type | Description                                    |
|-------------------|-----------|------------------------------------------------|
| `id`              | INTEGER   | Primary key, auto-incremented.                 |
| `transaction_type`| TEXT      | Name of the transaction (Income or Expense).   |
| `subcategory`     | TEXT      | Specific category, e.g., Salary, Utilities.    |
| `amount`          | DECIMAL   | Amount of the transaction.                     |
| `description`     | TEXT      | Description of the transaction.                |
| `date`            | DATE      | Date of the transaction.                       |

## Usage

### Menu Options

When you run the application, you will see the following menu:

```
==================
 Expense Tracker
==================
1. Add income
2. Display Records
Choose an option:
```

### Adding Data

1. Select `1` from the menu.
2. Enter the following details:
    - **Transaction Type:** Either "Income" or "Expense".
    - **Amount:** The amount of the transaction.
    - **Subcategory:** The subcategory related to the transaction (e.g., Salary for Income, Utilities for Expenses).
    - **Description:** A brief description of the transaction.
    - **Date:** The date of the transaction in YYYY-MM-DD format. If left empty, the current date will be used.


### Displaying Records
1. Select 2 from the menu to view all income and expense records in a formatted table:

ID | Transaction Type  | Subcategory     | Amount      | Date       | Description
-----------------------------------------------------------------------------
1  | Income            | Salary          | €2000.00    | 2025-01-18 | January paycheck
2  | Expense           | Utilities       | €150.00     | 2025-01-18 | January electricity bill


## Error Handling & Fixes
The following errors were identified and fixed:

1. Invalid Category Input
Problem: If the user entered an invalid category (e.g., not "Income" or "Expense"), the program would not accept it.
Fix: The program now checks for valid input and prompts the user to enter either "Income" or "Expense".

2. Non-Numeric Amount Input
Problem: If the user entered a non-numeric value for the amount, the program would crash.
Fix: The program now ensures that the amount is a valid numeric value, and displays an error message if not.

3. Date Formatting
Problem: If the user left the date empty, it caused issues with inserting data.
Fix: The program now defaults to the current date if the user does not enter a date.

4. Display Formatting Issues
Problem: Long descriptions would overflow the display table.
Fix: The description is now wrapped using textwrap.fill() to ensure it fits within a 30-character width and does not overflow.

## Contributing

Contributions are welcome! If you find a bug or want to suggest a feature, feel free to open an issue or submit a pull request.


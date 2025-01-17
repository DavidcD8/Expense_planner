# Expense Tracker

An expense tracker application built with Python and SQLite to help you manage and track your income and expenses efficiently.

## Features

- Add and track **income** (e.g., salary, freelance work).
- Add and track **expenses** (e.g., utilities, groceries).
- Display all records of income and expenses in a neatly formatted table.
- Store data persistently using SQLite.

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

| Column Name | Data Type | Description                                     |
|-------------|-----------|-------------------------------------------------|
| `id`        | INTEGER   | Primary key, auto-incremented.                 |
| `name`      | TEXT      | Name of the transaction (Income or Expense).   |
| `category`  | TEXT      | Category of the transaction (e.g., Salary).    |
| `income`    | DECIMAL   | Income amount (default: `0.0`).                |
| `expenses`  | DECIMAL   | Expense amount (default: `0.0`).               |
| `description`| TEXT     | Description of the transaction.                |
| `date`      | DATE      | Date of the transaction.                       |

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

### Adding Income

1. Select `1` from the menu.
2. Enter the following details:
   - **Amount**: The amount of income.
   - **Category**: The source of income (e.g., Salary).
   - **Description**: A brief description (e.g., January paycheck).
   - **Date**: The date of the transaction (format: `YYYY-MM-DD`).

### Adding Expenses

1. Select `1` from the menu.
2. Enter the following details:
   - **Amount**: The amount of expense.
   - **Category**: The category of expense (e.g., Utilities).
   - **Description**: A brief description (e.g., January electricity bill).
   - **Date**: The date of the transaction (format: `YYYY-MM-DD`).

### Display Records

1. Select `2` from the menu to view all income and expense records in a formatted table:
   ```
   ID | Amount | Category  | Date       | Description
   --------------------------------------------------
   1  | €2000  | Salary    | 2025-01-17 | January paycheck
   2  | €500   | Freelance | 2025-01-18 | Web design project
   ```

## Error Handling

The application handles invalid inputs and database errors gracefully, ensuring a smooth user experience.

## Contributing

Contributions are welcome! If you find a bug or want to suggest a feature, feel free to open an issue or submit a pull request.


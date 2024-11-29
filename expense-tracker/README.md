Implementation of the project https://roadmap.sh/projects/expense-tracker

# Expense Tracker
A simple expense tracker application to manage your finances. This application will allow users to add, delete, and view their expenses. This application should also provide a summary of the expenses.

# Installation

```
pip install -r requirements.txt
```

# Running the application


### Adding an Expense
```
python3 app.py --operation add --description apple --amount 10
Expense added to datastore successfully. ID: 5
```

### Listing all the Expenses

```
python3 app.py --operation list
+----+-------------+--------+------------+
| id | description | amount |    date    |
+----+-------------+--------+------------+
| 1  |    Apples   | 100.0  | 2024-11-29 |
| 2  |    Apples   | 100.0  | 2024-11-29 |
| 3  |    Apples   | 100.0  | 2024-11-29 |
| 4  |    apple    |  10.0  | 2024-11-29 |
| 5  |    apple    |  10.0  | 2024-11-29 |
+----+-------------+--------+------------+
```

### Summary of all the Expenses

```
python3 app.py --operation summary
Total Expenses: 320.0
```

### Summary for a specific month

```
python3 app.py --operation summary --month 11
Total Expenses: 320.0
```

### Updating an Expense:

```
python3 app.py --operation update --id 4 --description 'Orange' --amount=30
Expense with ID 4 has been updated successfully!
```

### Deleting an Expense:

```
python3 app.py --operation delete --id 4
Expense added to datastore successfully. ID: 4
```
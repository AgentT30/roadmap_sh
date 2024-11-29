import os
import sys
import csv
import json
import argparse
from typing import List
from datetime import datetime
from prettytable import PrettyTable

class Expense:

    def __init__(self, id:int):
        self.list_of_stored_expenses = get_stored_expenses()
        self.get_or_create_expense(id)


    def get_or_create_expense(self, id: int) -> None:
        if id:
            for expense in self.list_of_stored_expenses:
                if expense['id'] == id:
                    self.id = id
                    self.description = expense['description']
                    self.amount = expense['amount']
                    self.date = expense['date']
                    self.category = expense['category']
        else:
            try:
                self.id = max([expense['id'] for expense in self.list_of_stored_expenses]) + 1
            except:
                self.id = 1
            self.description = None
            self.amount = None
            self.date = str(datetime.now().date())
            self.category = None

    def add_expense(self, description:str, amount: float, category: str) -> int:
        self.description = description
        self.category = category
        self.amount = amount

        expense_to_be_saved = {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "date": self.date,
            "category": self.category
        }

        with open("./monthly_budget.json", 'r') as read_file:
            monthly_budget_values = json.loads(read_file.read())

        current_month = datetime.strptime(self.date, "%Y-%m-%d").month
        if monthly_budget_values[str(current_month)] < get_expense_summary(current_month) + self.amount:
            print(f"WARNING: You are exceeding the budget set for the month!")

        self.list_of_stored_expenses.append(expense_to_be_saved)

        with open("./expenses.json", 'w') as write_file:
            json.dump(self.list_of_stored_expenses, write_file, indent=4)

        return self.id
    
    
    def delete_expense(self) -> int:
        for index, expense in enumerate(self.list_of_stored_expenses):
            if expense['id'] == self.id:
                del self.list_of_stored_expenses[index]

                with open("./expenses.json", 'w') as write_file:
                    json.dump(self.list_of_stored_expenses, write_file, indent=4)

                return self.id
        else:
            print(f"Expense with id {self.id} not found to be deleted!")

    
    def update_expense(self, description: str, amount: float, category:str) -> int:
        for index, expense in enumerate(self.list_of_stored_expenses):
            if expense['id'] == self.id:
                self.list_of_stored_expenses[index]['amount'] = amount
                self.list_of_stored_expenses[index]['category'] = category
                self.list_of_stored_expenses[index]['description'] = description

                with open("./expenses.json", 'w') as write_file:
                    json.dump(self.list_of_stored_expenses, write_file, indent=4)

                return self.id
        else:
            print(f"Expense with id {self.id} not found to be updated!")

def get_stored_expenses() -> List[dict]:
    """
    Retrieves the list of stored expenses from the 'expenses.json' file.

    The function first checks if the file exists. If it does, it reads the data from the file.
    If the file does not exist, it creates a new file by initializing an empty list in it.
    The function then returns the list of stored expenses.
    """
    if os.path.exists("./expenses.json"):
        with open("./expenses.json", 'r') as read_file:
            data = json.loads(read_file.read())


    else:
        data = []
        with open("./expenses.json", 'w') as write_file:
            json.dump(data, write_file, indent=4)

    return data

def get_expense_summary(month: int=None) -> float:
    """
    Calculates and returns the total amount of all stored expenses.

    This function iterates over the list of stored expenses retrieved from 
    the 'expenses.json' file, sums up the 'amount' of each expense, and 
    returns the total sum.

    Returns:
        float: The total amount of all stored expenses.
    """
    total_expenses = 0

    for expense in get_stored_expenses():
        if month:
            if datetime.strptime(expense['date'], '%Y-%m-%d').month == month:
                total_expenses += expense['amount']
        else:
            total_expenses += expense['amount']

    return total_expenses

def set_monthly_budget(month: int, budget: float) -> None:
    try:
        with open("./monthly_budget.json", 'r') as read_file:
            monthly_budget_values = json.loads(read_file.read())

        monthly_budget_values[month] = budget

        with open("./monthly_budget.json", 'w') as write_file:
            json.dump(monthly_budget_values, write_file, indent=4)
    except Exception as e:
        print(f"Error updating the budget: {str(e)}")


if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument('--operation', type=str, choices=['set_budget', 'add', 'list', 'summary','update', 'delete', 'export'], required=True)
    argparse.add_argument('--id', type=int)
    argparse.add_argument('--amount', type=float)
    argparse.add_argument('--description', type=str)
    argparse.add_argument('--month', type=int)
    argparse.add_argument('--category', type=str, choices=['groceries','rent','travel','junk_food', 'misc'])

    args = argparse.parse_args()

    operation = args.operation

    if operation == 'set_budget':
        month = input("Month? (1-12): ")

        try:
            budget = float(input("Budget?: "))
        except ValueError:
            print("The budget value must be a number!")
            sys.exit(0)

        set_monthly_budget(month, budget)
    elif operation == 'list':
        stored_expenses = get_stored_expenses()

        expense_table = PrettyTable()
        expense_table.field_names = stored_expenses[0].keys()

        for expense in stored_expenses:
            expense_table.add_row(expense.values())

        print(expense_table)
    elif operation == 'summary':
        print(f"Total Expenses: {get_expense_summary(args.month)}")
    elif operation == 'add':
        description = args.description
        category = args.category
        amount = args.amount

        if not description:
            print(f"An description is required for an expense")
            sys.exit(0)

        if not amount:
            print(f"Amount is required for an expense")
            sys.exit(0)

        if not category:
            print(f"Category not provided for the expense. Defaulting the category to 'misc'")
            category = 'misc'

        if amount < 0:
            print(f"Invalid amount {amount}. Amount cannot be negative!")

        
        expense_obj = Expense(None)
        added_expense_id = expense_obj.add_expense(description, amount, category)

        print(f"Expense added to datastore successfully. ID: {added_expense_id}")
    elif operation == 'update':
        id = args.id
        description = args.description
        amount = args.amount

        if not id:
            print(f"ID is required to be able to update an expense")
            sys.exit(0)

        if not description or not amount:
            print(f"Description/Amount is required to be able to update an expense")
            sys.exit(0)

        expense_to_be_updated = Expense(id)
        updated_expense_id = expense_to_be_updated.update_expense(description, amount)

        print(f"Expense with ID {updated_expense_id} has been updated successfully!")
    elif operation == 'delete':
        id = args.id

        if not id:
            print(f"ID is required to be able to delete an expense")
            sys.exit(0)

        expense_to_be_deleted = Expense(id)
        deleted_expense_id = expense_to_be_deleted.delete_expense()

        print(f"Expense with ID {deleted_expense_id} has been deleted successfully!")
    elif operation == 'export':
        csv_filename = input("Enter the CSV Filename: ")
        expense_data = get_stored_expenses()

        with open(f"./{csv_filename}.csv", 'w') as write_file:
            csv_writer = csv.DictWriter(write_file, expense_data[0].keys())

            csv_writer.writeheader()
            for expense in expense_data:
                csv_writer.writerow(expense)

        print(f"Exported the data to {csv_filename}.csv file!")
    else:
        print(f"Invalid operation!")

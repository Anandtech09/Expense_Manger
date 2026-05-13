# FastAPI -The Expense Management application is designed to help users track their expenses and manage their financial activities.
# 1. Functional Requirements
'''1.1 Expense Model- The application should have a data model named `Expense` with the following attributes:- 
   `name` (string): Name of the expense.
   - `amount` (float): Amount spent for the expense.
   - `category` (string): Category to which the expense belongs.'''

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_current_username
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ExpenseModel(BaseModel):
    name: str
    amount: float
    category: str

'''1.2 Create Expense REST API- Implement an API endpoint to create an expense.
- Endpoint: `POST /expenses/`- Input: JSON payload containing `name`, `amount`, and `category`.
- Output: Return a JSON response with the newly created expense details, including an `expense_id`.'''

expenses = []
@app.post("/expenses/")
async def create_expense(expense: ExpenseModel):
    expense.expense_id = len(expenses) + 1
    expenses.append(expense)
    return {"expense_id": expense.expense_id}

'''1.3, Get Expenses API- Implement an API endpoint to retrieve a list of all expenses.
- Endpoint: `GET /expenses/`- Output: Return a JSON response containing a list of all expenses.'''


@app.get("/expenses")
def get_expenses():
    return {"expenses": expenses}

'''1.4, Filter Expenses by Month, Week, Day, Category API-
 Implement an API endpoint to retrieve expenses for a specific month.
 - Endpoint: `GET /expenses/month/{year}/{month}/`
 - Input: Year and Month.
 - Output: Return a JSON response containing a list of expenses for the specified month.'''


@app.get("/expenses/month/{year}/{month}")
def get_expenses_by_month(year: int, month: int):
    return {"expenses": [expense for expense in expenses if expense.date.month == month and expense.date.year == year]}

'''1.5, Total Expense, Total Salary, and Remaining Amount API
- Implement an API endpoint to retrieve total expenses, total salary, and remaining amount.
- Endpoint: `GET /totals/`- Output: Return a JSON response containing the total expense, total salary, and remaining amount.'''

salaries = []
@app.get("/totals/")
async def get_totals():
    total_expense = sum([expense.amount for expense in expenses])
    total_salary = sum([salary.amount for salary in salaries])
    remaining_amount = total_salary - total_expense
    return {"total_expense": total_expense, "total_salary": total_salary, "remaining_amount": remaining_amount}



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
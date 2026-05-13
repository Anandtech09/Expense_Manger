# The Expense Management application
## The Expense Management application is designed to help users track their expenses and manage their financial activities. 
## 1. Functional Requirements
### 1.1 Expense Model- The application should have a data model named `Expense` with the following attributes:- `name` (string): Name of the expense.- `amount` (float): Amount spent for the expense.- `category` (string): Category to which the expense belongs. 
### 1.2 Create Expense REST API- Implement an API endpoint to create an expense.- Endpoint: `POST /expenses/`- Input: JSON payload containing `name`, `amount`, and `category`.- Output: Return a JSON response with the newly created expense details, including an `expense_id`.

### 1.3 Get Expenses API- Implement an API endpoint to retrieve a list of all expenses.- Endpoint: `GET /expenses/`- Output: Return a JSON response containing a list of all expenses. 
### 1.4 Filter Expenses by Month, Week, Day, Category API- Implement an API endpoint to retrieve expenses for a specific month.- Endpoint: `GET /expenses/month/{year}/{month}/`- Input: Year and Month.- Output: Return a JSON response containing a list of expenses for the specified month.


### 1.5 Total Expense, Total Salary, and Remaining Amount API- Implement an API endpoint to retrieve total expenses, total salary, and remaining amount.- Endpoint: `GET /totals/`- Output: Return a JSON response containing the total expense, total salary, and remaining amount.


## 2. Non-functional Requirements 
### 2.1 Database IntegrationUse any SQL-based database of choice(SQLite, PSQL,etc.) 
### 2.2 Authentication (Optional)Implement a basic authentication mechanism using OAuthSecure the `POST /expenses/` and `GET /expenses/` endpoints with authentication

## To run project
`bash 
cd main
python main.py`


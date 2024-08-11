# Employee Management System

#### Overview
This Python script provides a simple Employee Management System that allows users to add new employees, view all employees, and manage employee data in a CSV file. The system automatically generates a unique ID for each new employee and stores employee details like name, phone number, email, age, date of birth, salary, and joining date.

### Code Explanation

#### Imports
```python
import os
from utils import read_employee_data, add_employees
from tabulate import tabulate
```
- **`import os`**: This module is used to interact with the operating system, such as checking if a file exists.
- **`from utils import read_employee_data, add_employees`**: We import two functions from a `utils` module:
  - `read_employee_data`: Reads existing employee data from the CSV file.
  - `add_employees`: Adds new employee data to the CSV file.
- **`from tabulate import tabulate`**: This module is used to display employee data in a nicely formatted table.

---

#### Variables and Initial Data
```python
employee_database = "data/employees.csv"
data_header = ["id", "name", "phone", "email", "age", "dob", "salary", "joining_date"]

existing_employee = [
    { 'id': '1', 'name': 'Ruchi Singh', 'phone': '123-456-7890', 'email': "ruchisingh.devops@gmail.com", 'age': 18, 'dob': "02/10/2004", 'salary': 10, 'joining_date': "10/10/2010"},
    { 'id': '2', 'name': 'Amity', 'phone': '9958125355', 'email': "amity_hoon@gmail.com", 'age': 20, 'dob': "10/12/2004", 'salary': 100, 'joining_date': "10/10/2004"},
    { 'id': '3', 'name': 'Kokur', 'phone': '1234567890', 'email': "boh_boh@gmail.com", 'age': 12, 'dob': "3/03/2008", 'salary': 100, 'joining_date': "10/10/2010"}
]
```
- **`employee_database`**: This variable stores the path to the CSV file where employee data will be saved.
- **`data_header`**: This is a list of column names (headers) for the CSV file.
- **`existing_employee`**: This list contains some initial employee data, each represented as a dictionary with the following fields: `id`, `name`, `phone`, `email`, `age`, `dob`, `salary`, `joining_date`.

---

#### Adding Initial Employees to the CSV File
```python
add_employees(file_path=employee_database, data=existing_employee, append=True, headers=data_header)
```
- **`add_employees` Function**: This function is called to add the initial `existing_employee` data to the CSV file.
  - **`file_path=employee_database`**: Specifies the file where the data will be written.
  - **`data=existing_employee`**: The list of employees to be added.
  - **`append=True`**: Specifies that new data should be appended to the file if it already exists.
  - **`headers=data_header`**: Specifies the headers for the CSV file.

---

#### Displaying the Main Menu
```python
def display_menu():
    print("\nEmployee Management System -- Version 1.0.0")
    print("1. Add New Employee")
    print("2. View All Employees")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice
```
- **`display_menu` Function**: This function shows the main menu to the user with three options:
  - Add a new employee.
  - View all employees.
  - Exit the program.
- **`choice`**: The user's choice is captured and returned by the function.

---

#### Generating a New Employee ID
```python
def generate_new_emp_id(employees):
    if not employees:
        return '1'
    max_id = max(int(emp['id']) for emp in employees)
    return str(max_id + 1)
```
- **`generate_new_emp_id` Function**: This function generates a unique ID for each new employee.
  - **If `employees` is empty**: The function returns `'1'` as the first ID.
  - **If `employees` is not empty**: The function finds the maximum existing ID and increments it by 1 to generate the new ID.

---

#### Adding a New Employee
```python
def add_new_employee():
    print("\nAdd New Employee")
    
    employees = read_employee_data(employee_database)
    emp_id = generate_new_emp_id(employees)  # Auto-generate employee ID
    
    name = input("Enter Employee Name: ")
    phone = input("Enter Employee Phone: ")
    email = input("Enter Employee Email: ")
    age = input("Enter Employee Age: ")
    dob = input("Enter Employee Date of Birth (dd/mm/yyyy): ")
    salary = input("Enter Employee Salary: ")
    joining_date = input("Enter Employee Joining Date (dd/mm/yyyy): ")
    
    new_employee = {
        'id': emp_id,
        'name': name,
        'phone': phone,
        'email': email,
        'age': age,
        'dob': dob,
        'salary': salary,
        'joining_date': joining_date
    }
    
    add_employees(file_path=employee_database, data=[new_employee], append=True, headers=data_header)
    print(f"Employee {name} added successfully with ID {emp_id}.")
```
- **`add_new_employee` Function**: This function collects information about a new employee and adds it to the CSV file.
  - **`employees`**: Reads existing employee data from the CSV file.
  - **`emp_id`**: Automatically generates a new ID for the employee.
  - **User Inputs**: Prompts the user to enter details like name, phone, email, age, date of birth, salary, and joining date.
  - **`new_employee`**: A dictionary containing the new employee's details, including the auto-generated ID.
  - **`add_employees`**: The function is called to add the new employee to the CSV file, appending the data if the file already exists.

---

#### Viewing All Employees
```python
def view_all_employees():
    print("\nAll Employees")
    employees = read_employee_data(employee_database)
    if not employees:
        print("No employees found.")
        return
    
    table_data = [[emp['id'], emp['name'], emp['phone'], emp['email'], emp['age'], emp['dob'], emp['salary'], emp['joining_date']] for emp in employees]
    
    print(tabulate(table_data, headers=data_header, tablefmt="pretty"))
```
- **`view_all_employees` Function**: This function displays all employees in a tabular format.
  - **`employees`**: Reads all employee data from the CSV file.
  - **If no employees are found**: A message is printed to indicate that no employees exist.
  - **`table_data`**: Prepares the employee data for display.
  - **`tabulate` Function**: This function is used to print the employee data in a nicely formatted table.

---

#### Main Program Loop
```python
while True:
    user_choice = display_menu()
    
    if user_choice == '1':
        add_new_employee()
    elif user_choice == '2':
        view_all_employees()
    elif user_choice == '3':
        print("Exiting Employee Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
```
- **Main Loop**: This loop continuously displays the menu until the user chooses to exit.
  - **`user_choice`**: Captures the user's menu selection.
  - **Option 1**: Calls `add_new_employee` to add a new employee.
  - **Option 2**: Calls `view_all_employees` to view all employees.
  - **Option 3**: Exits the program.
  - **Invalid Choice**: If the user enters an invalid option, an error message is displayed, and the menu is shown again.

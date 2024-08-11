import os
from utils import read_employee_data, add_employees
from tabulate import tabulate

employee_database = "data/employees.csv"
data_header = ["id", "name", "phone", "email", "age", "dob", "salary", "joining_date"]

existing_employee = [
    { 'id': '1', 'name': 'Ruchi Singh', 'phone': '123-456-7890', 'email': "ruchisingh.devops@gmail.com", 'age': 18, 'dob': "02/10/2004", 'salary': 10, 'joining_date': "10/10/2010"},
    { 'id': '2', 'name': 'Amity', 'phone': '9958125355', 'email': "amity_hoon@gmail.com", 'age': 20, 'dob': "10/12/2004", 'salary': 100, 'joining_date': "10/10/2004"},
    { 'id': '3', 'name': 'Kokur', 'phone': '1234567890', 'email': "boh_boh@gmail.com", 'age': 12, 'dob': "3/03/2008", 'salary': 100, 'joining_date': "10/10/2010"}
]

add_employees(file_path=employee_database, data=existing_employee, append=True, headers=data_header)

def display_menu():
    print("\nEmployee Management System -- Version 1.0.0")
    print("1. Add New Employee")
    print("2. View All Employees")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def generate_new_emp_id(employees):
    if not employees:
        return '1'
    max_id = max(int(emp['id']) for emp in employees)
    return str(max_id + 1)

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
    
    # TODO Validate the input
    add_employees(file_path=employee_database, data=[new_employee], append=True, headers=data_header)
    print(f"Employee {name} added successfully with ID {emp_id}.")

def view_all_employees():
    print("\nAll Employees")
    employees = read_employee_data(employee_database)
    if not employees:
        print("No employees found.")
        return
    
    table_data = [[emp['id'], emp['name'], emp['phone'], emp['email'], emp['age'], emp['dob'], emp['salary'], emp['joining_date']] for emp in employees]
    
    print(tabulate(table_data, headers=data_header, tablefmt="pretty"))

while True:
    user_choice = display_menu()
    
    if user_choice == '1':
        add_new_employee()
    elif user_choice == '2':
        view_all_employees()
    elif user_choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select a valid option.")

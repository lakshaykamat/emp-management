import csv
import os

def read_employee_data(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []


def add_employees(file_path, data, append=True, headers=None):
    existing_employees = read_employee_data(file_path)
    unique_ids = {employee['id'] for employee in existing_employees}
    
    # Filter out duplicate employees
    new_employees = []
    for employee in data:
        if employee['id'] in unique_ids:
            print(f"Skipping duplicate employee with ID {employee['id']} name: {employee['name']}")
            continue
        unique_ids.add(employee['id'])
        new_employees.append(employee)

    if not new_employees:
        print("No new employees to add.")
        return

    mode = 'a' if append and os.path.isfile(file_path) else 'w'
    
    with open(file_path, mode, newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers if headers else data[0].keys())
        
        # Write headers if the file is being created or overwritten
        if mode == 'w':
            writer.writeheader()
        
        # Write the new employees
        writer.writerows(new_employees)

    print(f"Added {len(new_employees)} new employees.")
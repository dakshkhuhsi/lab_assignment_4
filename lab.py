class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

def sort_employees(employees, sort_param):
    if sort_param == 1:  # Sort by Age
        return sorted(employees, key=lambda x: x.age)
    elif sort_param == 2:  # Sort by Name
        return sorted(employees, key=lambda x: x.name)
    elif sort_param == 3:  # Sort by Salary
        return sorted(employees, key=lambda x: x.salary)
    else:
        return employees

def print_employee_data(employees):
    print("Employee ID\tName\tAge\tSalary (PM)")
    for employee in employees:
        print(f"{employee.emp_id}\t{employee.name}\t{employee.age}\t{employee.salary}")

if __name__ == "__main__":
    employee_data = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    print("Choose a sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    sort_param = int(input("Enter the sorting parameter (1/2/3): "))

    sorted_employees = sort_employees(employee_data, sort_param)
    print_employee_data(sorted_employees)

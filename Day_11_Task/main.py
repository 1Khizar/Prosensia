from employee import Employee
from manager import EmployeeManager

def main():
     
    manager = EmployeeManager()
    
    while True:
        print("""
        1. Add Employee
        2. List Employees
        3. Search by Name/Dept
        4. Sort by Salary
        5. Generate Report
        6. Exit
                """)
            
        user_choice = int(input("Enter your choice (1-6): "))

        if user_choice == 1:
            name = input("Enter the name of employee : ")
            department = input(f"Enter the department of {name} : ")
            salary = input(f"Enter the salary of {name} : ")
            joining_year = input(f"Enter the joining_year of {name} : ")
            
            manager.add_employee(name, department, salary, joining_year)

        elif user_choice == 2:
            manager.list_employees()

        elif user_choice == 3:
            employee_name = input("Enter the name of employee : ")
            manager.search_employee_by_name(employee_name)
            
        elif user_choice ==4:
            manager.sort_by_salary()
        
        elif user_choice == 5:
            manager.generate_report()
        
        elif user_choice ==6:
            break
        
        else:
            print("Invalid input! Try again")
            
main()
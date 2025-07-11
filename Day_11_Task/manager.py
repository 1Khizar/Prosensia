from employee import Employee

class EmployeeManager:
    def __init__(self):
        self.filename = 'employee_data.txt'

    def add_employee(self, name, department, salary, joining_year):
        try:
            with open(self.filename, 'a') as file:
                file.write(f"{name},{department},{salary},{joining_year}\n")
            print("Employee added successfully.")
            
        except Exception as e:
            print("Error while adding employee:", e)

    def list_employees(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                if not lines:
                    print("No employee records found.")
                else:
                    for item in lines:
                        parts = item.strip().split(',')
                        if len(parts) != 4:
                            print(f"Skipping invalid line: {item.strip()}" )
                            continue
                                  
                        name, department, salary, joining_year = parts
                        emp = Employee(name, department, salary, joining_year)
                        emp.display()

        except FileNotFoundError:
            print("No employee data file found. Try adding a record first.")
    
    def search_employee_by_name(self, search_name):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                
                found = False
                for data in lines:
                    parts = data.strip().split(',')
                    if len(parts) != 4:
                        print(f"Skipping invalid line: {data.strip()}")
                        continue
                    name, department, salary, joining_year = data.strip().split(',')
                    if search_name == name:
                        emp = Employee(name, department, salary, joining_year)
                        found = True
                        return emp.display()
                    
                if not found:
                    print(f"{search_name} is not found!")
        except FileNotFoundError:
            print("File not found")
            
    def sort_by_salary(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                
                if not lines:
                    print("The employee list is empty.")
                else:
                    data = []
                    for line in lines:
                        parts = line.strip().split(',')
                        if len(parts) != 4:
                            print(f"Skipping invalid line: {line.strip()}")
                            continue
                        name, department, salary, joining_year = line.strip().split(',')
                        emp = Employee(name, department, float(salary), int(joining_year))
                        data.append(emp)
            sorted_employees_list = sorted(data, key = lambda e : e.salary  )
            print("\n--- Employees Sorted by Salary ---")
            for emp in sorted_employees_list:
                emp.display()
               
        except FileNotFoundError:
            print("File not found")
    
    def generate_report(self):
        
        try:
            with open(self.filename, 'r') as file1:
                lines = file1.readlines()
                report =[]
                
                if not lines:
                    print("The employee list is empty.")
                    return 
                else:
                    for line in lines:
                        parts = line.strip().split(',')
                        if len(parts) != 4:
                            continue
                        name, department, salary, joining_year = line.strip().split(',')
                        emp = Employee(name, department, float(salary), int(joining_year))
                        report.append(emp)
                        
                total_employee = len(report)
                total_salary = sum(emp.salary for emp in report)
                average_salary = total_salary /total_employee
                
            try:
                with open('report.txt', 'w') as file2:
                    file2.write("EMPLOYEE SUMMARY REPORT\n")
                    file2.write("=========================\n")
                    file2.write(f"Total Employees : {total_employee}\n")
                    file2.write(f"Average Salary  : ${average_salary:.2f}\n")
                print("Report generated successfully.")

            except FileNotFoundError:
                print('The report file is not found')
            
        except FileNotFoundError:
            print("File not found")
            

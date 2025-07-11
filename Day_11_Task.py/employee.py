class Employee:
    def __init__(self, name, department, salary, joining_year):
        self.name = name
        self.department = department  
        self.salary = float(salary)  
        self.joining_year = int(joining_year)

    def display(self):
        print(f"Name: {self.name} | Department: {self.department} | Salary: ${self.salary:.2f} | Year: {self.joining_year}")
       

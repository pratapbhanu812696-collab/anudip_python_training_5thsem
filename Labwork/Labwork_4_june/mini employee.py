#10. Mini Employee Payroll System
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def calculate_tax(self):
        if self.salary > 50000:
            return self.salary * 0.2  # 20% tax for salaries above 50,000
        elif self.salary > 30000:
            return self.salary * 0.1  # 10% tax for salaries between 30,000 and 50,000
        else:
            return 0  # No tax for salaries below or equal to 30,000

    def display_payroll(self):
        tax = self.calculate_tax()
        net_salary = self.salary - tax
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Gross Salary: ${self.salary}")
        print(f"Tax: ${tax}")
        print(f"Net Salary: ${net_salary}")
# Example usage
employee1 = Employee("John Doe", "E001", 60000)
employee2 = Employee("Jane Smith", "E002", 45000)
employee3 = Employee("Emily Davis", "E003", 25000)
employee1.display_payroll()
print()
employee2.display_payroll()
print()
employee3.display_payroll()

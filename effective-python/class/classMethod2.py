class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + "@email.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "Emloyee", 60000)

emp_str_1 = "Corey-Schafer-70000"
# Employee.set_raise_amt(1.05)
new_emp = Employee.from_string(emp_str_1)
#print(Employee.fullname())
print(emp_1.fullname())
print(emp_2.fullname())
print(new_emp.raise_amt)
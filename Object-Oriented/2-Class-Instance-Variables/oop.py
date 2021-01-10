class Employee:

    num_of_emps = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee.raise_amount)


print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1.fullname())
# print(Employee.fullname(emp_1))

# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)

# This how fun work in background
# print(Employee.fullname(emp_1))

# print(Employee.raise_amount)

# Here check if instance have attr if not then check class inheritance
# print(emp_1.pay)
# print(emp_1.raise_amount)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_2.raise_amount)

# Here we check name space
print(Employee.__dict__)
# print(emp_1.__dict__)
# print(emp_2.__dict__)

# Here change value
Employee.raise_amount = 1.07

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# Second change to use then in method we have to use self or we will get value none
emp_1.raise_amount = 1.03
# print(emp_1.__dict__)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_2.raise_amount)

print(Employee.num_of_emps)

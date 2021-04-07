#    **********CONSTRUCTOR**********

class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender

    def employee_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self.salary)
        print("Gender:",self.gender)

e1=Employee("arnab",23,45000,"male")
e1.employee_details()

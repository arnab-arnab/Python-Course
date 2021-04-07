class Employee:
    company="Google"

    def __init__(self,name,salary,subunit):  #<-- Constructor
        print("Employee is created")
        self.name=name
        self.salary=salary
        self.subunit=subunit

    def EmployeeDetails(self):
        print(self.name)
        print(self.salary)
        print(self.subunit)

    def getSalary(self):
        print(f"Salary of employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet():       # Here we do not need to use self as we are using static method
        print("Good morning sir")

    @staticmethod
    def time():
        print("Check bottom right of this lappy , you will get the time")

harry=Employee("Arnab",100000,"Cameras")
harry.EmployeeDetails()
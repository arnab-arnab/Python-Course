class Employee:
    company="Google"
    def getSalary(self):
        print(f"Salary of employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet():       # Here we do not need to use self as we are using static method
        print("Good morning sir")

    @staticmethod
    def time():
        print("Check bottom right of this lappy , you will get the time")

harry=Employee()
harry.salary=100000
harry.greet()


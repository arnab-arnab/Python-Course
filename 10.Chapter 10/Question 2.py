class calculator:
    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"Square of {self.num} is {self.num **2}")

    def cube(self):
        print(f"Cube of {self.num} is {self.num **3}")
    def sqrt(self):
        print(f"Square root of {self.num} is {self.num **0.5}")

a=calculator(9)
a.square()
a.cube()
a.sqrt()
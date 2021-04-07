# **********MULTIPLE INHERITANCE********* #

class a1:
    def assign_value_1(self,a):
        self.a=a

    def show_value_1(self):
        print(self.a)

class b1:
    def assign_value_2(self,b):
        self.b=b

    def show_value_2(self):
        print(self.b)


class derieved(a1,b1):
    def assign_value_3(self,c):
        self.c=c

    def show_value_3(self):
        print(self.c)

d1=derieved()
d1.assign_value_1("I")
d1.assign_value_2("love")
d1.assign_value_3("you")

d1.show_value_1()
d1.show_value_2()
d1.show_value_3()
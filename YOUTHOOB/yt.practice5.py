class parent():
    def assign_name(self,name):
        self.name=name
    def show_name(self):
        print("Name:",self.name)

class child(parent):
    def assign_age(self,age):
        self.age=age
    def show_age(self):
        print("Age:",self.age)

class grandchild(child):
    def assign_sex(self,sex):
        self.sex=sex
    def show_sex(self):
        print("Sex",self.sex)

gc=grandchild()
gc.assign_name("Arnab")
gc.assign_age(12)
gc.assign_sex("male")

gc.show_name()
gc.show_age()
gc.show_sex()
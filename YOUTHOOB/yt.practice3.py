# ********** OVERWRITING __INIT__ METHOD ********** #

class vehicles:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost

    def show_details(self):
        print("milage:",self.mileage)
        print("cost",self.cost)

V1=vehicles(500,50000)
V1.show_details()

class Cars(vehicles):
    def __init__(self,tyres,hp,mileage,cost):
        super().__init__(mileage,cost)
        self.tyres=tyres
        self.hp=hp

    def show_new_details(self):
        print("Number of tyres:",self.tyres)
        print("hp:",self.hp)


c1=Cars(4,300,50,300000)
c1.show_details()
c1.show_new_details()
# ********** INHERITANCE ********** #

class vehicles:
    def __init__(self,milage,cost):
        self.milage=milage
        self.cost=cost

    def show_details(self):
        print("milage:",self.milage)
        print("cost",self.cost)

V1=vehicles(500,50000)
V1.show_details()

class Cars(vehicles):
    def model(self):
        print("Sasta wala gaari")

c1=Cars(200,20000)
c1.show_details()

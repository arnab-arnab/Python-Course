class Phone:
    def set_colour(self,colour):
        self.colour=colour
    def set_cost(self,cost):
        self.cost=cost
    def show_colour(self):
        print(self.colour)
    def show_cost(self):
        print(self.cost)

p=Phone()
p.colour="black"
p.set_cost(5000)
p.show_colour()
p.show_cost()
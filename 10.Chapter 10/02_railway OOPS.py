class railwayform:
    formType="railway form"
    def printData(self):
        print(f"Name is {self.name}")    # f string
        print(f"Train is {self.train}")

arnabsapplication=railwayform()    # Creating an object
arnabsapplication.name="arnab"     # adding my data to the object
arnabsapplication.train="Rajdhani express"

arnabsapplication.printData()
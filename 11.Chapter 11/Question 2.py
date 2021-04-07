class animals:
    animalType="Mammals"

class pets(animals):
    colour="White"

class dogs(pets):
    @staticmethod
    def bark():
        print("Bhow bhoooo")

d=dogs()
d.bark()
class programmer:
    company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getDetails(self):
        print(f"The name is {self.name} and the product is {self.product}")

arnab=programmer("Arnab", "github")
echo=programmer("Echo", "skype")
arnab.getDetails()
echo.getDetails()
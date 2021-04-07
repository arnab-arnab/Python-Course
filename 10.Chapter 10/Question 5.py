class train:
    def __init__(self,ticket,status,infornation):
        self.ticket=ticket
        self.status=status
        self.information=infornation

    def book_a_ticket(self):
        print(f"{self.ticket} tickets booked successfully")

    def get_status(self):
        print(f"{self.status} seats confirmed")

    def fare_info(self):
        print(f"{self.information *1000} is the total fare")

traveller=train(2,2,2)
traveller.book_a_ticket()
traveller.get_status()
traveller.fare_info()
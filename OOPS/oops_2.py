class Mobile:
    def __init__(self,brand,Ram):
        self.brand = brand
        self.Ram= Ram

    def Display(self):
        print(f'the mobile brand is {self.brand} and ram is {self.Ram}')

mob1=Mobile("Apple","4gb")
mob1.Display()
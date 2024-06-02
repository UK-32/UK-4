class Phone:

    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class Smartphone(Phone):
    pass

s=Smartphone(2000,"Apple",12)
print(s.camera)

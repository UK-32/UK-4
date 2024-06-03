class Car:
    def __init__(self, brand, model, owner_name, wife_name,daughter_name, son_name):
        self.brand = brand
        self.model = model
        self.owner_name = owner_name
        self.wife_name = wife_name
        self.daughter_name = daughter_name
        self.son_name = son_name

        print(f"Welcome to the Sajid family")

    def greet(self):
        print(f"Hello {self.owner_name}, I am your {self.brand} {self.model}. Enjoy your drive!")
        if self.wife_name:
            print(f"Hello to your wife, {self.wife_name}!")
        if self.daughter_name:
            print(f"Hello to your daughter, {self.daughter_name}!")
        if self.son_name:
            print(f"Hello to your son, {self.son_name}!")

# Creating instances of the Car class
car1 = Car("Toyota", "Passo", "Sajid", "Hira", "Zainab", "Taha")
car1.greet()


print(f"Have a safe journey.")

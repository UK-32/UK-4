class Atm:
    
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.sno = 0

        self.sno += 1
        
        print(id(self))
        
        self.menu()

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        self.__pin = new_pin
        print("Pin changed")
    
    def menu(self):
        while True:
            user_input = input("""
                    Hello, how would you like to proceed?
                    1. Enter 1 to create pin 
                    2. Enter 2 to deposit
                    3. Enter 3 to withdraw
                    4. Enter 4 to check balance
                    5. Enter 5 to exit
            """)
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Bye")
                break
            else:
                print("Invalid input, please try again.")
        
    def create_pin(self):
        new_pin = input("Enter your pin: ")
        self.set_pin(new_pin)
        print("Pin set successfully")
        
    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.get_pin():
            amount = int(input("Enter the amount: "))
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid pin")
            
    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.get_pin():
            amount = int(input("Enter the amount: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Operation successful")
            else:
                print("Insufficient funds")
        else:
            print("Invalid pin")
                
    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.get_pin():
            print(f"Your balance is: {self.__balance}")
        else:
            print("Invalid pin")
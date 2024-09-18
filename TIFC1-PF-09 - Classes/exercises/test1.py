class rest:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.serve = 0
    def descripe(self):
        print(f"{self.name} is {self.type}")
    def open(self):
        print(f"{self.name} is open")
    def servey(self,number):
        self.serve = number
        print(self.serve)

rest1 = rest("najem", "kebab shop")
rest1.descripe()
rest1.open()
print(f"{rest1.name} is {rest1.type} and serve {rest1.serve} people")
rest1.name = "sham"
rest1.serve = 50
print(f"{rest1.name} is {rest1.type} and serve {rest1.serve} people")  
rest1.servey()
class Restaurant:
    def __init__(self, Restaurant_name, Cuisine_type):
        self.Restaurant_name = Restaurant_name
        self.Cuisine_type = Cuisine_type
        self.Number_served = 0

    def describe_restaurant(self):
                    """Prints the restaurant's name and the type of cuisine."""
                    print(f"Restaurant Name: {self.Restaurant_name}")
                    print(f"Cuisine Type: {self.Cuisine_type}")

    def open_restaurant(self):
               print(f"{self.Restaurant_name} is open")
    def set_number_served(self, number):
            self.Number_served = number
            print(f"{self.Number_served} people served")
    def increment_number_served(self, increment):
            self.number_served += increment
restaurant1 = Restaurant("The Great Diner", "American")
restaurant2 = Restaurant("Pizza Palace", "Italian")
restaurant3 = Restaurant("Sushi Central", "Japanese")
restaurant4 = Restaurant("Curry Corner", "Indian")
# print(restaurant1.Restaurant_name)
# print(restaurant1.Cuisine_type)

restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()

print(f"Number of customers served at {restaurant2.Restaurant_name}: {restaurant2.Number_served}")
restaurant2.number_served = 50  # Updating the value manually
print(f"Updated number of customers served: {restaurant2.number_served}")
restaurant2.set_number_served(11)
print(f"Number of customers served after using set_number_served(): {restaurant2.number_served}")
restaurant2.increment_number_served(22)
print(f"Number of customers served after incrementing: {restaurant2.number_served}")







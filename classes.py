# Class for Cars
class Car:
    def __init__(self, brand, model, capacity):
        self.brand = brand
        self.model = model
        self.capacity = capacity  # in seating

    # Method to get car info
    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, capacity: {self.capacity} seater."

# Usage
car = Car("Toyota", "Camry", 5)
print(car.get_info())  # To get car info

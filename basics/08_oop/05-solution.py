#5. Polymorphism
#Problem: Demonstrate polymorphism by defining a method fuel_type  in both Car and ElectricCar classes, but with different behaviours.

class Car:
    def __init__(self, brand, model):
        self.__brand=brand
        self.model=model
    def get_brand(self):
        return self.__brand
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

        
    def fuel_type(self):
        return "Electric Charge"
          
            
Tesla=ElectricCar("Teslaaa", "Model S", "44kw")
# print(Tesla.brand)
print(Tesla.fuel_type())


safari=Car("Tata", "Safari")
print(safari.fuel_type())

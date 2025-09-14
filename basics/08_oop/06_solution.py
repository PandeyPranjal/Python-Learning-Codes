#6. Class Variables
#Problem. Add a class variable to Car that keeps track of the number of cars craeted.


class Car:
    total_car=0
    def __init__(self, brand, model):
        self.__brand=brand
        self.model=model
        Car.total_car+=1
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
Car("Mahindra", "Scorpio")
Car("Suzuki", "Wagonr")


safari=Car("Tata", "Safari")
print(safari.fuel_type())
print(Car.total_car)

#3. Inheritance
#Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
class Car:
    def __init__(self, brand , model):
        self.brand=brand
        self.model=model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self,brand, model,  battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
        
        
my_car=Car("Mahindra", "Thar")
print(my_car.brand)
print(my_car.model)
ev=ElectricCar("Tesla", "ModelS", "85kWH")
print(ev.brand)
print(ev.model)
print(ev.battery_size)
print(ev.full_name())
        
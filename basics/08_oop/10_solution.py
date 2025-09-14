#10. Multiple Inheritance 
#Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
class Battery:
    def __init__(self,battery):
        self.battery=battery
    
    def battery_info(self):
        return "This is the battery info."
class Engine:
    def __init__(self, engine):

        self.engine=engine
    def engine_info(self):
        return "This is all about Engine."
class ElectricCar(Battery, Engine):
    def __init__(self, battery, engine):
        Battery.__init__(self, battery)
        Engine.__init__(self, engine)
my_car=ElectricCar("83kwh", "Efficient")
print(my_car.battery_info())
print(my_car.engine_info())
    
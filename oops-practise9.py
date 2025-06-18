class Engine:
	def __init__(self, horse_power):
		self.horse_power = horse_power

class Wheel:
	def __init__(self, wheel_size):
		self.wheel_size = wheel_size

class Car:
	def __init__(self, name, horse_power, wheel_size):
		self.name =  name
		self.engine = Engine(horse_power)
		self.wheel = [Wheel(wheel_size) for wheel in range(4)]

	def display_car(self):
		return f"{self.name} has {self.engine.horse_power}hp {self.wheel[0].wheel_size}in"

car1 = Car("mustang", 500, 18)
print(car1.display_car())
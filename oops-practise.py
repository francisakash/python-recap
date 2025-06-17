class Car:
	def __init__(self, model:str, make:int, color:str):
		self.model = model
		self.make = make
		self.color = color

	def describe(self):
		print(f"Model: {self.model}, make: {self.make}, color: {self.color}")

car1 = Car("Mustang", 2025, "Blue")
car1.describe()
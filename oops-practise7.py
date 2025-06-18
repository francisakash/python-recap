from abc import ABC, abstractmethod

class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return 3.14 * self.radius ** 2

class Square(Shape):
	def __init__(self, width):
		self.width = width

	def area(self):
		return self.width * self.width

class Triangle(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height =height 

	def area(self):
	 	return (self.width * self.height)/2

class Pizza(Circle):
	def __init__(self, toppings, radius):
		super().__init__(radius)
		self.toppings = toppings

shapes = [Circle(4), Square(5), Triangle(4, 3), Pizza("paporini", 17)]

for shape in shapes:
	print(f"{shape.area()} cm^2")
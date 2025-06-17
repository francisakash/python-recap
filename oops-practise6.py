class Shape:
	def __init__(self, color:str, is_filled:bool):
		self.color = color
		self.is_filled = is_filled

	def describe(self):
		print(f"It is {self.color} color and it is {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
	def __init__(self, color, is_filled, radius):
		super().__init__(color, is_filled)
		self.radius = radius

	def describe(self):
		print(f"This circle is {self.radius * self.radius} cm^2")
		super().describe()

class Square(Shape):
	def __init__(self, color, is_filled, width):
		super().__init__(color, is_filled)
		self.width = width

	def describe(self):
		print(f"This square is {self.width * self.width} cm^2")
		super().describe()

class Triangle(Shape):
	def __init__(self, color, is_filled, width, height):
		super().__init__(color, is_filled)
		self.width = width
		self.height = height

	def describe(self):
		print(f"This square is {(self.width * self.height)/2} cm^2")
		super().describe()

circle = Circle("red", True, 5)
square = Square("blue", False, 7)
triangle = Triangle("orange", True, 8, 9)

circle.describe()
square.describe()
triangle.describe()
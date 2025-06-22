class Rectangle:
	def __init__(self, width, height):
		self._width = width
		self._height = height

	@property
	def width(self):
		return f"{self._width:.1f}"
	@property
	def height(self):
		return f"{self._height:.1f}"

	@width.setter
	def width(self, new_width):
		if new_width <= 0:
			return "width should be greater than 0"
		else:
			self._width = new_width

	@height.setter
	def height(self, new_height):
		if new_height > 0:
			self._height = new_height
		else:
			return "height should be greater than 0"

	@width.deleter
	def width(self):
		del self._width
		print("Width has been deleted")

	@height.deleter
	def height(self):
		del self._height
		print("height has been deleted")

rectangle = Rectangle(4, 3)

rectangle.width = 5
rectangle.height = 7

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height
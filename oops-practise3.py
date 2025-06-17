class Animal:

	def __init__(self, name):
		self.name = name
		self.is_alive = True

class Dog(Animal):
	def speak(gulp):
		print(f"{gulp.name} is saying woof")

class Cat(Animal):
	def speak(self):
		print(f"{self.name} is saying meow")

class Mouse(Animal):
	def speak(self):
		print(f"{self.name} is saying squeek")

dog1 = Dog("Bob")
cat1 = Cat("Tom")
mouse1 = Mouse("Jerry")

dog1.speak()

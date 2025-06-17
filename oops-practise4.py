class Animal:
	def __init__(self, name):
		self.name = name

	def eat(self):
		print(f"{self.name} is eating")

	def sleep(self):
		print(f"{self.name} is sleeping")

class Pray(Animal):
	def flee(self):
		print(f"{self.name} is fleeing")

class pradetor(Animal):
	def hunt(self):
		print(f"{self.name} is hunting")

class Rabbit(Pray):
	pass
class Hawk(pradetor):
	pass
class Fish(Pray, pradetor):
	pass

rabbit = Rabbit("moonie")
hawk = Hawk("mr hawk")
fish = Fish("matsumoto")

fish.eat()
fish.sleep()
fish.flee()
fish.hunt()
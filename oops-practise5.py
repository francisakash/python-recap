from abc import ABC, abstractmethod

class Vehical(ABC):

	@abstractmethod
	def start(self):
		pass

	@abstractmethod
	def stop(self):
		pass

class Car(Vehical):
	def start(self):
		print("car is start")

	def stop(self):
		print("car is stopped")


BMW = Car()
BMW.start()
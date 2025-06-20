class Employee:
	def __init__(self, name, position):
		self.name = name
		self.position = position

	def get_info(self):
		return f"{self.name} = {self.position}"

	@staticmethod
	def is_valid_position(position):
		valid_postion = ["captain", "cook", "swordsman", "navigator"]
		return position in valid_postion

print(Employee.is_valid_position("cook"))

employee1 = Employee("Luffy", "captain")
employee2 = Employee("Zoro", "swordsman")
employee3 = Employee("Sanji", "cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

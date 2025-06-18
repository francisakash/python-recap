class Company:
	class Employee:
		def __init__(self, name, position):
			self.name = name
			self.position = position

		def get_details(self):
			return f"{self.name} {self.position}"

	def __init__(self, name):
		self.name = name
		self.employees = []

	def add_employees(self, name, position):
		new_employee = self.Employee(name, position)
		self.employees.append(new_employee)

	def list_employee(self):
		return [emoployee.get_details() for emoployee in self.employees]

company = Company("Oscorp")

company.add_employees("harry", "M.D")
company.add_employees("Peter", "Spider man")

print(company.list_employee())
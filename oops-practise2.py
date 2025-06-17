class Student:

	class_year = 2026
	total_student = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age
		Student.total_student += 1

student1 = Student("Cupcake", 12)
student2 = Student("Alan", 12)

print(f"Total student: {Student.total_student}")
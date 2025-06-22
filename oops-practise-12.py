class Student:
	total_student = 0
	total_gpa = 0

	def __init__(self, name, gpa):
		self.name = name
		self.gpa = gpa
		Student.total_student += 1
		Student.total_gpa += gpa

	def show_details(self):
		return f"{self.name} {self.gpa}"

	@classmethod
	def about_class(cls):
		if cls.total_student == 0:
			return 0
		else:
			return f"Total student:{cls.total_student} | Average GPA:{cls.total_gpa/cls.total_student:.2f}"

student1 = Student("luke", 3.8)
student2 = Student("mohai", 2.9)

print(student1.show_details())
print(Student.about_class())
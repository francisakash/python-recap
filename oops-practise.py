class Git:
	def __init__(self, num):
		self.num = num

	def get_details(self):
		print(f"version {self.num}")

v1 = Git(2)
v1.get_details()
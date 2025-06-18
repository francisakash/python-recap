class Library:
	def __init__(self, name):
		self.name = name
		self.books = []

	def add_book(self, book):
		self.books.append(book)

	def list_book(self):
		for book in self.books:
			print(f"{book.name} by {book.author}")

class Book:
	def __init__(self, name, author):
		self.name = name
		self.author = author

library = Library("Thirunagar Public library")

book1 = Book("Atomic habit", "James clear")
book2 = Book("Thinking fast and slow", "Daniel Khaneman")
book3 = Book("Deep work", "Carl Newport")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
library.list_book()
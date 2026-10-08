class LibraryBook:
    def __init__(self, title, author, availability_status):
        self.title = title
        self.author = author
        self.availability_status = availability_status


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, book):
        if book.availability_status == "Available":
            book.availability_status = "Issued"
            print(f"{book.title} has been issued.")
        else:
            print(f"{book.title} is already issued.")

    def return_book(self, book):
        book.availability_status = "Available"
        print(f"{book.title} has been returned.")

    def display_available_books(self):
        for book in self.books:
            if book.availability_status == "Available":
                print(f"Title: {book.title}, Author: {book.author}")


book1 = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", "Available")
book2 = LibraryBook("To Kill a Mockingbird", "Harper Lee", "Available")
book3 = LibraryBook("1984", "George Orwell", "Available")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("Available Books:")
library.display_available_books()

print()

library.issue_book(book1)

print("\nAvailable Books After Issuing:")
library.display_available_books()

print()

library.return_book(book1)
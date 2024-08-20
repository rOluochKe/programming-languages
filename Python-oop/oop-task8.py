"""
Title: Library Management System

Description:
This code represents a library management system that allows you to manage a collection of books. The system provides functionalities for adding books, displaying all books, searching for books by author, and searching for books within a specific year range.

#####

Book Class:
The Book class serves as the base class for different types of books.

-It has attributes for title, author, and year.

-The display_info method is used to print the title, author, and year of a book.

###

FictionBook Class:
The FictionBook class is a subclass of the Book class. It adds an additional attribute called genre.

-The display_info method is overridden to include the genre when printing book information.

###

NonFictionBook Class:
The NonFictionBook class is another subclass of the Book class. It adds an attribute called topic.

-Similar to the FictionBook class, the display_info method is overridden to include the topic in the book information.

###

Library Class:
-The Library class represents the library management system. It has a list to store the books in the library.

-The add_book method is used to add a book to the library. The display_all_books method prints the information of all the books in the library.

-The search_by_author method searches for books by a specific author and displays their information.

-The search_by_year_range method searches for books published within a given year range and displays their information.

#####

Outside your classes, a Library object is created. Four books, including both fiction and non-fiction, are instantiated and added to the library. The display_all_books method is called to print the information of all the books in the library. The search_by_author method is then used to find and display books written by a specific author. Finally, the search_by_year_range method is used to find and display books published within a given year range.

This code provides a basic library management system where you can add books, view all books, search for books by author, and search for books published within a specific time period. It allows for efficient organization and retrieval of book information in a library setting.
"""


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Year: {self.year}')


class FictionBook(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def info(self):
        super().info()
        print(f'Genre: {self.genre}')


class NonFictionBook(Book):
    def __init__(self, title, author, year, topic):
        super().__init__(title, author, year)
        self.topic = topic

    def info(self):
        super().info()
        print(f'Topic: {self.topic}')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.info()
            print()

    def search_author(self, author):
        found_books = []
        for book in self.books:
            if book.author == author:
                found_books.append(book)
        if found_books:
            print(f'Books by {author}:')
            for book in found_books:
                book.info()
                print()
        else:
            print("No books found by this author!")

    def search_year(self, start_year, end_year):
        found_books = []
        for book in self.books:
            if start_year <= book.year <= end_year:
                found_books.append(book)

        if found_books:
            print(f'Books between {start_year} and {end_year}:')
            for book in found_books:
                book.info()
                print()

        else:
            print("Errors")


library = Library()

book1 = FictionBook("Harry Potter and the Sorcerer's Stone",
                    "J.K. Rowling", 1997, "Fantasy")

book2 = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")

book3 = NonFictionBook("Sapiens: A Brief History of Humankind",
                       "Yuval Noah Harari", 2014, "Anthropology")

book4 = NonFictionBook(
    "The Power of Now", "Eckhart Tolle", 1997, "Spirituality")


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# library.display_books()

library.search_author("F. Scott Fitzgerald")
library.search_year(2000, 2020)

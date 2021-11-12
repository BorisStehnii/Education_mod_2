class Author:

    def __init__(self, name_author: str, country: str, birthday: int) -> None:
        self.name_author = name_author
        self.country = country
        self.birthday = birthday
        self.books_author = []

    def __repr__(self) -> str:
        return f"Name: {self.name_author}; Country: {self.country}; Birthday: {self.birthday}"


class Book:

    def __init__(self, name_book: str, year: int, author: Author) -> None:
        self.name_book = name_book
        self.year = year
        self.author = author
        self.amount = 0

    def __repr__(self) -> str:
        return f"<<Name:{self.name_book}; Year:{self.year}; Author:{self.author.name_author};" \
               f" Amount copy:{self.amount}>>"


class Library:

    def __init__(self, name_library: str) -> None:
        self.name_library = name_library
        self.books_library = []
        self.author_library = []

    def new_book(self, name_book_: str, year_: int, author: Author) -> Book:
        book = Book(name_book_, year_, author)
        control = True
        for ind, book_ in enumerate(self.books_library):
            if name_book_ == book_.name_book and year_ == book_.year and author == book_.author:
                self.books_library[ind].amount += 1
                book = book_
                control = False
        if control:
            book.amount = 1
            self.books_library.append(book)
            if author in self.author_library:
                self.author_library.remove(author)
            author.books_author.append(book)
            self.author_library.append(author)

        return book

    def group_by_author(self, author: Author) -> list:
        return author.books_author

    def group_by_year(self, year: int) -> list:
        list_year_book = []
        for ind, book in enumerate(self.books_library):
            if year == book.year:
                list_year_book.append(book)
        return list_year_book

    def __repr__(self) -> str:
        return f"Name library: {self.name_library};\nBooks: {self.books_library};\n Author: {self.author_library}"


library = Library("Library")
author = Author("Boris", "UA", 1997)
author_2 = Author("Den", "UA", 1999)
print(library.new_book("ABC", 2020, author))
print(library.new_book("ABC", 2020, author))
print(library.new_book("AB", 2021, author))
print(library.new_book("ABC", 2020, author))
print(library.new_book("AB", 2020, author))
print(library.group_by_author(author))
print(library.author_library)
print(library.group_by_year(2020))
print(library.new_book("ABC", 2020, author_2))
print(library.new_book("AB_D", 2019, author_2))
print(library.group_by_year(2020))


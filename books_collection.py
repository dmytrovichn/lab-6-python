from book import Book


class BooksCollection(object):

    def __init__(self):
        self.__books = []
        self.__index = 0

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, books):
        if type(books) != list:
            print("Error Param books should be list with elements of class Book")
        self.__books = books

    def __str__(self):
        str_books = ''
        for book in self.__books:
            str_books = f"{str_books}{book}\n"

        return str_books

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__books):
            raise StopIteration

        book = self.__books[self.__index]
        self.__index += 1
        return book

    def read(self, path):
        try:
            with open(path, 'r') as f:
                lines = f.readlines()
                if lines:
                    try:
                        for line in lines:
                            name, author, size = line.replace("\n", "").split(",")
                            book = Book(name, author, int(size))
                            self.__books.append(book)
                    except BaseException as e:
                        print(e)
                else:
                    print(f"{path} is empty")
        except FileNotFoundError as e:
            print(f"{e}, Try change your path: {path}")

    def write(self, path):
        try:
            with open(path, 'w') as f:
                for book in self.__books:
                    f.write(f"{book.name}, {book.author}, {book.size}\n")
        except FileNotFoundError as e:
            print(f"{e}, Try change your path: {path}")

    def add(self, book):
        self.__books.append(book)

    def delete(self, index=0):
        if index >= len(self.__books):
            print(f"Wrong index Collection len is {len(self.__books)}")

        self.__books.pop(index)

    def update(self, index, book):
        self.__books[index] = book

    def sort(self):
        self.__books.sort()

    def search(self, author):
        books = list(filter(lambda book: book == author, self.__books))
        return books

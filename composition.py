from book import Book


class Composition(Book):

    def __init__(self, name="None", author="None", size=0, genre="None"):
        self.__genre = genre
        super().__init__(name, author, size)

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    def enter_data(self):
        Book.enter_data(self)
        self.__genre = input("Enter genre: ")

    def __str__(self):
        return f"{Book.__str__(self)} Genre: {self.__genre}\n"

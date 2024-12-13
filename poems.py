from book import Book


class Poems(Book):

    def __init__(self, name="None", author="None", size=0, poems_count=0):
        self.__poems_count = poems_count
        super().__init__(name, author, size)

    @property
    def poems_count(self):
        return self.__poems_count

    @poems_count.setter
    def poems_count(self, poems_count):
        self.__poems_count = poems_count

    def enter_data(self):
        Book.enter_data(self)
        self.__poems_count = input("Enter genre: ")

    def __str__(self):
        return f"{Book.__str__(self)} Poems count: {self.__poems_count}\n"

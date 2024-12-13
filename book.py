class Book(object):

    def __init__(self, name="None", author="None", size=0):
        self.__name = name
        self.__author = author
        self.__size = size

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    @property
    def size(self):
        return self.__size

    @name.setter
    def name(self, name):
        self.__name = name

    @author.setter
    def author(self, author):
        self.__author = author

    @size.setter
    def size(self, size):
        self.__size = size

    def enter_data(self):
        self.__name = input("Enter name: ")
        self.__author = input("Enter author: ")
        self.__size = int(input("Enter size: "))

    def __str__(self):
        return f"Book: {self.__name}\n Author: {self.__author}\n Page size: {self.__size}\n"

    def __lt__(self, other):
        return self.__size < other.size

    def __gt__(self, other):
        return self.__size > other.size

    def __le__(self, other):
        return self.__size <= other

    def __ge__(self, other):
        return self.__size >= other

    def __eq__(self, other):
        return self.__author.lower() == other.lower()

    def __ne__(self, other):
        return self.__author.lower() != other.lower()


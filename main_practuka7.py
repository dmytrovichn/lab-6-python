from composition import Composition
from poems import Poems
from books_collection import BooksCollection

# c = Composition("Енеїда", "Котляревський", 440, "Бурлеск травестійна поема")
# print(c)
#
# p = Poems("Кобзар", "Шевченко", 720, 235)
# print(p)

books_collection = BooksCollection()
books_collection.read('books.txt')
books_collection.write('copy_books.txt')
print(books_collection)
# for book in books_collection:
#     print(book)

t = int(input("You want work with books? 1-yes, 0-no\n"))

while t == 1:
    action = int(input(
        "1-add element\n"
        "2-delete element\n"
        "3-update element\n"
        "4-sort by size\n"
        "5-search by author\n"
    ))

    if action == 1:
        books_collection.add()
        print(books_collection)
    elif action == 2:
        print(f"Collection len is {len(books_collection.books)}")
        index = int(input("Enter index: \n"))
        books_collection.delete(index)
        print(books_collection)
    elif action == 3:
        print(f"Collection len is {len(books_collection.books)}")
        index = int(input("Enter index: \n"))
        try:
            book = books_collection.books[index]
        except IndexError:
            continue

        if int(input("You want change name: 1-yes 0-no\n")) == 1:
            book.name = input("Enter name:\n")
        if int(input("You want change author: 1-yes 0-no\n")) == 1:
            book.author = input("Enter author:\n")
        if int(input("You want change size: 1-yes 0-no\n")) == 1:
            book.size = int(input("Enter size:\n"))
        books_collection.update(index, book)
        print(books_collection)
    elif action == 4:
        books_collection.sort()
        print(books_collection)
    elif action == 5:
        author = input("Enter last name for search by author: \n")
        books = books_collection.search(author)
        for book in books:
            print(book)
    else:
        print("Wrong action number(\n")

    t = int(input("You want continue work with books? 1-yes, 0-no\n"))




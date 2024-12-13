from book import Book


def print_books(books):
    for book in books:
        print(book)


books = []
with open('books.txt', 'r') as f:
    lines = f.readlines()
    if lines:
        try:
            for line in lines:
                name, author, size = line.replace("\n", "").split(",")
                book = Book(name, author, int(size))
                books.append(book)
        except BaseException as e:
            print(e)

    else:
        print("books.txt is empty")

print_books(books)

t = int(input("You want work with books? 1-yes, 0-no\n"))

while t == 1:
    action = int(input(
        "1-sort by name\n"
        "2-sort by author\n"
        "3-sort by size\n"
        "4-search by author\n"
    ))

    if action == 1:
        books.sort(key=lambda x: x.name)
        print_books(books)
    elif action == 2:
        books.sort(key=lambda x: x.author)
        print_books(books)
    elif action == 3:
        books.sort()
        print_books(books)
    elif action == 4:
        author = input("Enter last name for search by author: \n")
        author_books = filter(lambda book: book == author, books)
        print_books(author_books)
    else:
        print("Wrong action number(\n")

    t = int(input("You want continue work with books? 1-yes, 0-no\n"))


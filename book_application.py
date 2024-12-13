from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from books_collection import BooksCollection
from book import Book

# Create empty books collection
books_collection = BooksCollection()


def show_all():
    books.delete(0, END)
    for book in books_collection:
        books.insert(END, book)


def sort_by_size():
    books_collection.sort()
    books.delete(0, END)
    for book in books_collection:
        books.insert(END, book)


def delete_book():
    index = books.curselection()[0]
    books_collection.delete(index)
    books.delete(index)


def open_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    if not filename:
        return
    try:
        books_collection.read(filename)
        for book in books_collection:
            books.insert(END, book)
        showinfo(
            title='Open file',
            message="Successfully"
        )

    except FileNotFoundError:
        showinfo(
            title='Open file',
            message="Unsuccessful"
        )


def save_file():
    f = fd.asksaveasfile(
        mode='a',
        initialfile='Books.txt',
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt")])
    if f is None:
        return
    try:
        books_collection.write(f.name)
        showinfo(
            title='Saving to collection',
            message="Successfully"
        )

    except FileNotFoundError:
        showinfo(
            title='Saving to collection',
            message="Unsuccessful"
        )


# Application
root = Tk()
root.title('Books Store')
root.resizable(False, False)
root.geometry('640x480+400+100')

# # Main Window
scrollbar = Scrollbar()
scrollbar.pack(side=RIGHT, fill=Y)
books = Listbox(yscrollcommand=scrollbar.set)

for book in books_collection:
    books.insert(END, book)
books.pack(padx=2, pady=2, fill=BOTH, expand=True)


# # Add Window
def add_book_window():
    def save_book():
        if not book_name.get():
            showinfo(
                title='Wrong data',
                message="Please enter the book name"
            )
            return

        if not author.get():
            showinfo(
                title='Wrong data',
                message="Please enter the author"
            )
            return

        if not size.get():
            showinfo(
                title='Wrong data',
                message="Please enter the size"
            )
            return
        try:
            book = Book(book_name.get(), author.get(), int(size.get()))
            books_collection.add(book)
            books.insert(END, book)
            add_window.destroy()
            showinfo(
                title='Saving book',
                message="Successfully"
            )
        except ValueError:
            showinfo(
                title='Wrong data',
                message="Size Type should be a integer"
            )
            return

    add_window = Toplevel(root)
    add_window.resizable(False, False)
    add_window.title("Add book")
    add_window.geometry("340x160+400+100")
    Label(add_window, text="Please enter all data and click save").grid(row=0, column=1)
    Label(add_window, text='Book Name').grid(row=2, stick='w')
    Label(add_window, text='Author').grid(row=4, stick='w')
    Label(add_window, text='Size').grid(row=6, stick='w')
    book_name = Entry(add_window)
    author = Entry(add_window)
    size = Entry(add_window)
    book_name.grid(row=2, column=1)
    author.grid(row=4, column=1)
    size.grid(row=6, column=1)
    Button(add_window, text="Save", fg="black", command=save_book).grid(row=8, column=1)


# # Update Window
def update_book_window():
    def save_book():
        try:
            if book_name.get():
                book.name = book_name.get()
            if author.get():
                book.author = author.get()
            if size.get() and int(size.get()):
                book.size = int(size.get())

            books_collection.update(index, book)
            books.delete(index)
            books.insert(index, book)
            add_window.destroy()
            showinfo(
                title='Updating book',
                message="Successfully"
            )
        except ValueError:
            showinfo(
                title='Wrong data',
                message="Size Type should be a integer"
            )
            return

    add_window = Toplevel(root)
    add_window.resizable(False, False)
    add_window.title("Update book")
    add_window.geometry("420x210+400+100")

    index = books.curselection()[0]
    book = books_collection.books[index]

    Label(add_window, text="Please enter data that you want and click update").grid(row=0, column=1)
    Label(add_window, text=book).grid(row=1, column=1)
    Label(add_window, text='Book Name').grid(row=2, stick='w')
    Label(add_window, text='Author').grid(row=4, stick='w')
    Label(add_window, text='Size').grid(row=6, stick='w')
    book_name = Entry(add_window)
    author = Entry(add_window)
    size = Entry(add_window)
    book_name.grid(row=2, column=1)
    author.grid(row=4, column=1)
    size.grid(row=6, column=1)
    Button(add_window, text="Update", fg="black", command=save_book).grid(row=8, column=1)


# # Search By Author Window
def search_by_author_window():
    def search_by_author():
        author_name = author.get()
        search_books = books_collection.search(author_name)
        if not search_books:
            showinfo(
                title='Searching by author',
                message=f"Not found any books for {author_name}"
            )
            return

        books.delete(0, END)
        for book in search_books:
            books.insert(END, book)
        showinfo(
            title='Searching by author',
            message=f"Found {len(search_books)} books for {author_name}"
        )
        add_window.destroy()

    add_window = Toplevel(root)
    add_window.resizable(False, False)
    add_window.title("Search by author")
    add_window.geometry("250x100+400+100")
    Label(add_window, text="Please enter author").grid(row=0, column=1)
    Label(add_window, text='Author').grid(row=2, stick='w')
    author = Entry(add_window)
    author.grid(row=2, column=1)
    Button(add_window, text="Search", fg="black", command=search_by_author).grid(row=4, column=1)


# # bar menu
menu = Menu(root)
root.config(menu=menu)
books_menu = Menu(menu)
menu.add_cascade(label='Books', menu=books_menu)
books_menu.add_command(label='Add', command=add_book_window)
books_menu.add_command(label='Delete', command=delete_book)
books_menu.add_command(label='Update', command=update_book_window)

filter_menu = Menu(menu)
menu.add_cascade(label='Filters', menu=filter_menu)
filter_menu.add_command(label='Sort By Size', command=sort_by_size)
filter_menu.add_command(label='Search By Author', command=search_by_author_window)
filter_menu.add_command(label='Show All', command=show_all)


file_menu = Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)

root.mainloop()

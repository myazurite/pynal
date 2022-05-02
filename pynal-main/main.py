import os

books = []
borrowed_books = []
genres=[]

class Book:
    def __init__(self, name, genre, author, status):
        self._name = name
        self._genre = genre
        self._author = author
        self._status = status

    def get_name(self):
        return self._name

    def get_genre(self):
        return self._genre

    def get_author(self):
        return self._author

    def get_status(self):
        return self._status

    def set_name(self, name):
        self._name = name

    def set_author(self, author):
        self._author = author

    def set_genre(self, genre):
        self._genre = genre

    def set_status(self, status):
        self._status = status

    def __str__(self):
        return f"Book title: {self._name}\nGenre: {self._genre}\nAuthor: {self._author}\nStatus: {self._status}"


def read_book_from_file():
    f = open("BookInfo.txt", 'r')
    while 1:
        line = f.readline()
        name = line.strip()
        line = f.readline()
        genre = line.strip()
        line = f.readline()
        author = line.strip()
        line = f.readline()
        status = line.strip()
        if not name:
            break
        bookInfo = Book(name, genre, author, status)
        books.append(bookInfo)
    f.close()
    os.remove("BookInfo.txt")


def add_borrowed_book():
    for i in books:
        if i.get_status() == "false":
            borrowed_books.append(i.get_name())


def add_genre():
    for i in books:
        genres.append(i.get_genre())
    return list(dict.fromkeys(genres))



def borrow_book():
    bkname = input("Enter book name: ")
    found = 0
    for i in books:
        if (i.get_name() == bkname):
            found = 1
            if (i.get_status() == "true"):
                print("Book borrow!")
                borrowed_books.append(bkname)
            else:
                print("Book is not available!")
    if found == 0:
        print("Book not found")


def return_book():
    bkname = input("Enter book name: ")
    found = 0
    for i in books:
        if (i.get_name() == bkname):
            found = 1
            if (i.get_status() == "false"):
                print("Book returned!")
                i.set_status("true")
            else:
                print("Book is already returned!")
    for i in borrowed_books:
        if i == bkname:
            borrowed_books.remove(i)
    if found == 0:
        print("Book not found")


def modify_book():
    bkname = input("Enter book name: ")
    for i in books:
        if i.get_name() == bkname:
            while 1:
                print("1.change name")
                print("2.change genre")
                print("3.change author")
                print("4.exit")
                choice = int(input("Enter choice: "))
                if choice == 1:
                    newname = input("enter new name: ")
                    i.set_name(newname)
                if choice == 2:
                    newgenre = input("enter new genre: ")
                    i.set_name(newgenre)
                if choice == 3:
                    newauthor = input("enter new author: ")
                    i.set_name(newauthor)
                if choice == 4:
                    break


def add_more_book():
    name = input("enter title: ")
    genre = input("enter genre: ")
    dup_genre = 0
    for i in genres:
        if i.get_genre() == genre:
            dup_genre = 1
            break
    if dup_genre == 0:
        genres.append(genre)
    author = input("enter author: ")
    status = input("enter status: ")
    bookInfo = Book(name, genre, author, status)
    books.append(bookInfo)
def show_book():
    for i in books:
        print(i)
def del_book():
    name = input("Enter book name: ")
    for i in books:
        if i.get_name() == name:
            books.remove(i)
def menu():
    while 1:
        print("1.Show books")
        print("2.Add book")
        print("3.Issue book")
        print("4.Return book")
        print("5.Delete Book")
        print("6.exit")
        choice=int(input("Enter your choice"))
        if choice ==1:
            show_book()
        elif choice == 2:
            add_more_book()
        elif choice == 3:
            borrow_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            del_book()
        elif choice == 6:
            break
read_book_from_file()
add_borrowed_book()
genres = add_genre()
f = open("BookInfo.txt", 'w+')
for i in books:
    f.write(i.get_name() + "\n")
    f.write(i.get_genre() + "\n")
    f.write(i.get_author() + "\n")
    f.write(i.get_status() + "\n")
f.close()

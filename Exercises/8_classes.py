# Library Management System

# Create a Library class that can store information about books, each book has title, author and availability

# 1. Create class Book with attributes:
#    -Title
#    -Author
#    -Availability

# 2. Create class Library that can:
#    - Add new book to the library
#    - Search for a book
#    - Checkout a book by changing its availability
#    - Display available books
#    - Display the list of all books


class Book:
    def __init__(self, *, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True  # Always true when first created in this case

    def __str__(self):
        return f"{self.title} By {self.author} - {"Available" if self.is_available else "Checked out"}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, *, title: str, author: str):
        new_book = Book(title=title, author=author)
        self.books.append(new_book)
        print(f"{title} by {author} was added")

    def search_book(self, *, query: str):
        for book in self.books:
            if book.title.lower() == query.lower():
                if book.is_available:
                    print(f"Book {book.title} is available")
                else:
                    print(f"Book {book.title} is checked out")
            else:
                return f"No book matches {query} was found in our database"

    def checkout(self, *, query: str):
        for book in self.books:
            if book.title.lower() == query.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"{book.title} was checked out")
                    return
                else:
                    print(f"{book.title} is already checked out")
                    return
            else:
                print(f"{query} wasn't found")
                return

    def fetch_available_books(self):
        available_books = [book.title for book in self.books if book.is_available]
        print("Available Books: ", available_books)

    def fetch_all_books(self):
        if self.books:
            print("Available books:")
            for book in self.books:
                print(book)
        else:
            print("No Available books")


def main():
    library = Library()

    while True:
        print("1. Add a book.")
        print("2. Search for a book.")
        print("3. Checkout a book.")
        print("4. Display available books.")
        print("5. Display all books")
        print("6. Quit the system")

        option = int(input("\n Enter ur option: "))

        if option == 6:
            break
        elif option == 1:
            title = input("Enter the title of the book ")
            author = input("Enter the author of the book ")
            library.add_book(title=title, author=author)
        elif option == 2:
            query = input("Enter the title of the book ")
            library.search_book(query=query)
        elif option == 3:
            query = input("Enter the title of the book to check it out ")
            library.checkout(query=query)
        elif option == 4:
            library.fetch_available_books()
        elif option == 5:
            library.fetch_all_books()


main()

class Book:
    def __init__(self, title, author):
        """
        Initialize a Book instance.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out

    def __str__(self):
        """User-friendly string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self._books = []  # Private list of books

    def add_book(self, book):
        """
        Add a Book instance to the library.

        Args:
            book (Book): The book to add.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by its title.

        Args:
            title (str): Title of the book to check out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # Book not found or already checked out

    def return_book(self, title):
        """
        Return a book by its title.

        Args:
            title (str): Title of the book to return.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # Book not found 

    def list_available_books(self):
        """Print all books that are currently available."""
        available_books = [str(book) for book in self._books if book.is_available()]
        if available_books:
            for book_str in available_books:
                print(book_str)
        else:
            print("No books are currently available.")

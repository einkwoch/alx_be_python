class Book:
    """Represents a book with a title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available."""
        return not self._is_checked_out


class Library:
    """A library system that manages books."""

    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        """Add a new Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title if available."""
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                book.check_out()
                return f'You have checked out "{book.title}".'
        return f'"{title}" is not available.'

    def return_book(self, title):
        """Return a checked-out book by its title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    return f'You have returned "{book.title}".'
                return f'"{title}" was not checked out.'
        return f'"{title}" not found in library.'

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book.title for book in self._books if book.is_available()]
        if available_books:
            return available_books
        return ["No books available."]
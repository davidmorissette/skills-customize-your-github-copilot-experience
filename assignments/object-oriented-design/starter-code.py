# Starter Code for Object-Oriented Design Assignment

class LibraryItem:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.available = True

    def display_info(self):
        # Print the item details and availability
        pass

    def checkout(self):
        # Mark the item as checked out
        pass

    def return_item(self):
        # Mark the item as available again
        pass


class Book(LibraryItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def display_info(self):
        # Print the book details
        pass


class Movie(LibraryItem):
    def __init__(self, title, year, director):
        super().__init__(title, year)
        self.director = director

    def display_info(self):
        # Print the movie details
        pass


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        # Add a library item to the collection
        pass

    def list_items(self):
        # Print details for all items in the library
        pass

    def checkout_item(self, title):
        # Find an item by title and check it out if available
        pass

    def return_item(self, title):
        # Find an item by title and return it if it is checked out
        pass


# Example usage:
# library = Library()
# book = Book('The Time Machine', 1895, 'H. G. Wells')
# movie = Movie('Back to the Future', 1985, 'Robert Zemeckis')
# library.add_item(book)
# library.add_item(movie)
# library.list_items()
# library.checkout_item('The Time Machine')
# library.return_item('The Time Machine')

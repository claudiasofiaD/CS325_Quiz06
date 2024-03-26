from abc import ABC, abstractmethod

class SearchBooksInterface(ABC):
    @abstractmethod
    def search_books(self):
        pass

class LibrarianInterface(SearchBooksInterface):
    @abstractmethod
    def add_book(self):
        pass

    @abstractmethod
    def remove_book(self):
        pass

    @abstractmethod
    def borrow_book(self):
        pass

    @abstractmethod
    def return_book(self):
        pass

    @abstractmethod
    def generate_reports(self):
        pass

class GuestUser(SearchBooksInterface):
    def search_books(self):
        print("Searching books")

class Librarian(LibrarianInterface):
    def add_book(self):
        print("Adding book")

    def remove_book(self):
        print("Removing book")

    def borrow_book(self):
        print("Borrowing book")

    def return_book(self):
        print("Returning book")

    def generate_reports(self):
        print("Generating reports")

    def search_books(self):
        print("Searching books")

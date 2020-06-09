from book import Book
from repository import Repository


class BookService():

    def get_bookList(self):
        print("LISTAR LIBROS")
        return Repository.booksList

    def crearLibro(self):
        name = input("Ingrese el nombre del libro: ")
        authorName = input("ingrese el autor del libro: ")
        memberLegajo = int(input("ingrese el legajo: "))
        return Book(name, authorName, memberLegajo)

    def add_book(self, book=None):
        print("\n----AGREGAR LIBRO")
        if book is None:
            book = self.crearLibro
            Key = -1
        for bookKey in Repository.booksList:
            Key = bookKey
        Key = Key + 1
        Repository.booksList[Key] = book.__dict__

    def update_book(self, bookKey=None, book=None):
        print("\n----MODIFICAR LIBRO")
        if bookKey is None:
            bookKey = int(input("Ingrese una key: "))
        if book is None:
            book = self.crearLibro()
        Repository.booksList[bookKey] = book.__dict__

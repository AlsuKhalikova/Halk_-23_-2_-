from typing import List 
from pydantic import BaseModel
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book(BaseModel):
    id_: int
    name: str
    pages: int


# TODO написать класс Library
class Library(BaseModel):
    books: List[Book] = []

    def get_next_book_id(self):
        next_id = None
        if not self.books:
            return 1
        if self.books:
            for index in list(enumerate(self.books)):
                i = index[0]
                next_id = self.books[i].id_ + 1
            return next_id

    def get_index_by_book_id(self, idy):
        for index in list(enumerate(self.books)):
            i = index[0]
            if self.books[i].id_ == idy:
                return i
        else:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

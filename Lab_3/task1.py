class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self.author!r})"

    @property
    def prop1(self) -> str:
        return self._name

    @prop1.setter
    def prop1(self, _name) -> None:
        if not isinstance(_name, str):
            raise TypeError("Название книги должно быть строкой")

    @property
    def prop2(self) -> str:
        return self._author

    @prop2.setter
    def prop2(self, _author) -> None:
        if not isinstance(_author, str):
            raise TypeError("Автор книги должен быть строкой")


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def prop3(self) -> int:
        return self._pages

    @prop3.setter
    def prop3(self, _pages) -> None:
        if not isinstance(_pages, int):
            raise TypeError("Количество страниц в книге должно быть целым числом")
        if _pages <= 0:
            raise ValueError("Количество страниц в книге должно быть больше 0")

    def __str__(self):
        return super().__str__() + f", количество страниц {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def prop4(self) -> float:
        return self._duration

    @prop4.setter
    def prop4(self, _duration) -> None:
        if not isinstance(_duration, float):
            raise TypeError("Длительность книги должна быть вещественным числом")
        if _duration <= 0:
            raise ValueError("Длительность книги должна быть больше 0 секунд")

    def __str__(self):
        return super().__str__() + f", длительность {self._duration}"

# TODO: описать базовый класс
class Person:
    def __init__(self, surname: str, name: str, age: int):
        """
        :param surname: фамилия
        :param name: имя
        :param age: возраст(полное количество лет)
        """
        self.surname = surname
        self.name = name
        self.age = age

        if not isinstance(surname, str):
            raise TypeError("фамилия должна быть строкой")
        if not isinstance(name, str):
            raise TypeError("имя должно быть строкой")
        if not isinstance(age, int):
            raise TypeError("возраст должен быть целым числом")
        if age <= 0:
            raise ValueError("возраст должен быть больше 0 лет")

    def __str__(self):
        """
        Магический метод __str__
        """
        print(f"Имя: {self.name}, Фамилия: {self.surname}, возраст: {self.age} лет")

    def __repr__(self):
        """
        Магический метод __repr__. Полученная строка является валидным кодом
        """
        return f"person({self.surname!r}, {self.name!r}, {self.age!r})"

    def add_year(self, age=1) -> None:
        """
        Функция добавляет некоторое количество лет человеку (по умолчанию 1 год)
        """
        self.age += age
        if self.age > 100:
            raise ValueError("Возраст не может превышать 100 лет")
        if age < 0:
            raise ValueError("Нельзя прибавлять нулевое или отрицательное количество лет")


# TODO: описать дочерний класс
class Employee(Person):
    def __init__(self, surname, name, age, position: str, salary: float):
        super().__init__(surname, name, age)
        super().add_year(age)
        """
        :param position: должность
        :param salary: зарплата(в рублях)
        метод add_year унаследован из базового класса Person
        """

        self.position = position
        self.salary = salary

        if not isinstance(position, str):
            raise TypeError("должность должна быть строкой")
        if not isinstance(salary, float):
            raise TypeError("зарплата должна быть вещественным числом")
        if salary < 28750:
            raise ValueError("зарплата не может быть меньше МРОТ")

        def __str__(self):
            """
            Манический метод __str__. Для объектов типа Employee
            дополнительно к параметрам имя, фамилия, возраст добавляются
            путем конкатенации строк должность, зарплата
            """
            print(super.__str__(self) + f", Должность: {self.position}, " + f"Зарплата: {self.salary}")

        def __repr__(self):
            """
            Магический метод __repr__. Для объектов типа Employee
            дополнительно к параметрам имя, фамилия, возраст добавляются
            путем конкатенации строк должность, зарплата. Полученная строка является валидным кодом
            """
            return super.__repr__() + f", {self.position!r}" + f"{self.salary!r}"





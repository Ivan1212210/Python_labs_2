# TODO: Подробно описать три произвольных класса


# TODO: описать класс
class Person:
    def __init__(self, name: str, age: int, ex_pet: bool):
        """
        :param name: имя
        :param age: возраст (с точностью до лет)
        :param ex_pet: имеет ли человек домашнее животное
        """
        self.name = name
        self.age = age
        self.ex_pet = ex_pet

        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if (age > 100) or (age < 1):
            raise ValueError("Возраст не может быть меньше одного года или больше ста лет")

    def show_name(self) -> None:
        """
        Выводит имя человека
        """
        print(self.name)

    def add_year(self, age: int = 1) -> None:
        """
        :param age: возраст
        """
        self.age += age
        if self.age > 100:
            raise ValueError("Возраст не может превышать 100 лет")
        if age < 0:
            raise ValueError("Нельзя прибавлять нулевое или отрицательное количество лет")

    def is_pet(self) -> bool:
        """
        Выводит, есть ли у человека домашнее животное
        """
        if self.ex_pet:
            """
            :param ex_pet: показывает, есть ли у человека домашнее животное
            """
            print("У человека есть домашнее животное")
        else:
            print("У человека нет домашнего животного")
        return self.ex_pet


# TODO: описать ещё класс
class Teapot:
    def __init__(self, volume: float, colour: str, water_temperature: int):
        """
        :param volume: объем чайника (в литрах)
        :param colour: цвет чайника
        :param water_temperature: температура воды в чайнике (в Цельсиях с точностью до целого)
        Пример:
            >>> my_teapot = Teapot(1.8, "black", 24)
        """
        self.volume = volume
        self.colour = colour
        self.water_temperature = water_temperature
        if not isinstance(volume, (float, int)):
            raise TypeError
        if (volume <= 0) or (volume > 2):
            raise ValueError("В чайник помещается не больше двух литров воды")
        if not isinstance(colour, str):
            raise TypeError("Цвет должен быть строкой")
        if not isinstance(water_temperature, int):
            raise TypeError("Температура воды должна быть целым числом")
        if (water_temperature > 100) or (water_temperature < 1):
            ValueError("Вода в чайнике может иметь температуру от 1 до 100 градусов Цельсия")

    def set_temperature(self, water_temperature: int = 100) -> None:
        """
        :param water_temperature: температура воды в чайнике
        """
        self.water_temperature = water_temperature
        if not isinstance(water_temperature, int):
            raise TypeError("Температура должна быть целым числом")
        if (water_temperature > 100) or (water_temperature < 40):
            raise ValueError("Можно выставить температуру воды в чайнике от 40 до 100 градусов")

    def show_colour(self) -> None:
        """
        Выводит цвет чайника
        """
        print(self.colour)

    def calculate_percentage_of_fullness(self, cur_volume: float) -> float:
        """
        :param cur_volume: количество воды в чайнике в настоящий момент
        """
        percentage_of_water: float = cur_volume / self.volume * 100
        if (cur_volume <= 0) or (cur_volume > 2):
            raise ValueError("Объем воды в чайнике должен быть не отрицательным или больше 2 литров")
        if not isinstance(cur_volume, float):
            raise TypeError("Объем воды в чайнике должен быть действительным числом")
        return percentage_of_water


# TODO: и ещё один
class Country:
    def __int__(self, name: str, population: int, currency: str, area: float):
        """
        :param name: азвание страны
        :param population: население страны
        :param currency: официальная валюта страны
        :param area: площадь территории страны (в квадратных километрах)
        """
        self.name = name
        self.population = population
        self.currency = currency
        self.area = area
        if not isinstance(population, int):
            raise TypeError("Количество человек должно быть целым числом")
        if population < 1:
            raise ValueError("Население страны не может быть меньше одного человек")
        if not isinstance(currency, str):
            raise TypeError("Валюта страны должна быть строкой")
        if not isinstance(area, float):
            raise TypeError
        if area < 0.0001:
            raise ValueError("Площадь стрны не может быть меньше 100 квадратных метров")

    def calculate_density_of_population(self, area: float, population: int = 1000000) -> float:
        """
        :param area: площадь территории страны
        :param population: население страны
        """
        density_of_population: float = round(self.population / self.area)
        """
        :param density_of_population: плотность населения страны
        """
        if not isinstance(population, int) or not isinstance(area, float):
            raise TypeError("Население страны или площадь территории не соответсвует необходимым типам данных")
        return density_of_population

    def show_currency(self) -> None:
        """
        Выводит валюту страны
        """
        print(self.currency)

    def show_name(self) -> None:
        """
        Выводит название страны
        """
        print(self.name)

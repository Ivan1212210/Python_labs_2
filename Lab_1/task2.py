from task_1 import*  # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
    # TODO: инстанцировать все описанные классы, создав три объекта C().
    person_1 = Person("Ivan", 18, True)
    teapot_1 = Teapot(1.8, "red", 24)
    country_1 = Country()

    try:
        # TODO: вызвать метод с некорректными аргументами(b)
        person_1.add_year(-3)

    except:
        print('Ошибка: неправильные данные')

    try:
        # TODO: вызвать метод с некорректными аргументами (a)
        teapot_1.set_temperature(150)
    except:
        print('Ошибка: неправильные данные')

    try:
        # TODO: вызвать метод с некорректными аргументами (a)
        country_1.calculate_density_of_population(-8, ...)
    except:
        print('Ошибка: неправильные данные')




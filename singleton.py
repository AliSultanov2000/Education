class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


# Вставить сюда пример кода

from sklearn.impute import SimpleImputer


imp = SimpleImputer(missing_values=np.nan, strategy='mean')
example_data = np.array([[np.nan, 1, 2],
                            [3, np.nan, 4],
                            [5, 6, np.nan]])

imp.fit_transform(example_data)


# Импутация на тесте. Данные заполняются статистиками, которые вычислены на трейне. НА ТЕСТЕ СТАТИСТИКИ НЕ СЧИТАЮТСЯ!
imp.transform([[np.nan, 1, 4], [10, np.nan, 11], [11, np.nan, 13]])

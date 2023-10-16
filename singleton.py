class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


    
# ИСПОЛЬЗОВАНИЕ def в Pipeline 
# ВАЖНО 1: def в Pipeline следует использовать только для этапов трансформирования (где нету обучения fit, fit_transform)
# ВАЖНО 2: При использовании кастомной функции def, ф-я заворачивается в ООП FunctionTransformer класс, где имеются методы fit, fit_transform и тд, эти методы классы служат как "заглушка", чтобы конвейер смог и далее работать безотказно! 
# ВАЖНО 3: функция должна обязательно что-то return-ить
# ВАЖНО 4: Внутри ф-ии аргумент обзываем как X, y не надо вообще указывать в аргументах (в отличие от ООП, где надо явно прописывать y=None) - но если хочется, то можно, чтобы стандартизировать код
# ВАЖНО 5: Если в кастомную функцию хотим добавить инверсивную функцию, то при обёртке необходимо явно указать эту инверсивную функцию, иначе инверсия работать не будет (ошибки тоже не будет!)


from sklearn.preprocessing import FunctionTransformer

def transf_func(X: pd.DataFrame, y=None):
    return X + 30  # Добавляю + 30 чтобы сравнить с медианой из ООП ПРИМЕРА 1


transformer1 = FunctionTransformer(transf_func)  # Оборачиваем кастомную функцию transf_func в ООП класс FunctionTransformer


# def - ПРИМЕР 3 - для сравнения с ООП (СОВПАЛО). fit не запускаю так как нет обучения. Если запустить fit - ничего не изменится
pipocka3 = Pipeline([('transform', transformer1)])
pipocka3.transform(df100)

# def - ПРИМЕР 4 - для сравнения с ООП (УРА, СОВПАЛО). fit запускаю так как MinMaxScaler нуждается в обучении (вычисление статистик). 
pipocka4 = Pipeline([('transform', transformer1), ('norm', MinMaxScaler())])
pipocka4.fit(df100)
pipocka4.transform(df100)


# Проверка того, что в MinMaxScaler попали трансформированные данные
print(f'Минимум: {pipocka4[1].data_min_}')
print(f'Максимум: {pipocka4[1].data_max_}')

def inverse_func(X):
    return X - 30  # Функция инверсии

transformer2 = FunctionTransformer(transf_func, inverse_func=inverse_func)  # Оборачиваем кастомную функцию transf_func в ООП класс FunctionTransformer

pipocka5 = Pipeline([('transform', transformer2), ('norm', MinMaxScaler())])
pipocka5.fit(df100)  # Вычисление статистик для MinMaxScaler
pipocka5.inverse_transform(np.array([[0.  ],
                                     [0.25],
                                     [0.5 ],
                                     [0.75],
                                     [1.  ]]))

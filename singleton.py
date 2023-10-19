class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


    

    


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

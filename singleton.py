class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer


X = pd.DataFrame({'age': [10, 20, 30, 40], 'balance': [400, 600, 800, 1000], 'kernel': ['White', 'Black', 'Green', 'Yellow'], 'sex': ['male', 'female', 'male', 'female']})



def change_num1(X: pd.DataFrame, y=None):
    """Функция для работы с колонкой age"""
    return X + 10 

def change_num2(X: pd.DataFrame, y=None):
    """Функция для работы с колонкой balance"""
    return X - 100


trans1 = FunctionTransformer(change_num1)
trans2= FunctionTransformer(change_num2)


ct = ColumnTransformer([("tr1", trans1, ["age"]), ("tr2", trans2, ["balance"]), ("tr3", OneHotEncoder(), ['kernel', 'sex'])])
ct.fit_transform(X)

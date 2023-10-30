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


from sklearn.linear_model import LogisticRegression


# Определяем данные
X = pd.DataFrame({'age': [10, 20, 30, 40, 50, 60], 'balance': [400, 600, 800, 1000, 1200, 1400], 'kernel': ['White', 'Black', 'Green', 'Yellow', 'White', 'Black'], 'sex': ['male', 'female', 'male', 'female', 'male', 'female']})
y = [1, 1, 1, 0, 0, 0]


# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=42) 

class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance


    
class RemoveOutliers(TransformerMixin):
    """Класс для удаления выбросов интерквартильным методом"""

    def __init__(self):
        """init хранятся статистики по всем признакам!"""
        self.q_25 = None   
        self.q_50 = None 
        self.q_75 = None
    




from sklearn.base import TransformerMixin

class DataTransform(TransformerMixin):
    def __init__(self):
        self.median = None

    def fit(self, X: pd.DataFrame, y=None):
        self.median = X.median()
        return self
        
    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X + self.median
        return X
    

df100 = pd.DataFrame([10, 20, 30, 40, 50])

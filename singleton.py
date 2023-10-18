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
    

    def fit(self, X: pd.DataFrame, y=None): 
        """fit вычисляем статистики по всем признакам на train"""
        self.q_25 = X.quantile(q=0.25)
        self.q_50 = X.quantile(q=0.50)
        self.q_75 = X.quantile(q=0.75)
        return self
    
    
    def transform(self, X: pd.DataFrame):
        """Замена выбросов на квантили по всем признакам как на train, так и на test"""
        for column in X.columns:
            q_3 = self.q_75[column]
            q_1 = self.q_25[column]
            iqr = q_3 - q_1
            upper_bound = q_3 + 1.5 * iqr
            lower_bound = q_1 - 1.5 * iqr
            X.loc[X[column] > upper_bound, column] = q_3
            X.loc[X[column] < lower_bound, column] = q_1
        return X

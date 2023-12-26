"""
Учебный файл с реализацией основных паттернов проектирование, так как: 
   - Синглтон;
   - Адаптер;
   - Фасад; 
   - Строитель;
   - Фабрика;
   - Декоратор;
"""



class Singleton:
    """Класс для демонстрации паттерна проектирования Singleton"""
    __instance = None  # В этой переменной будет храниться новый объект
    def __new__(cls, *args):  # перегружаем метод __new__ от родительского класса object
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Запускаем __new__ от object, в противном случае не запускаем от object
        return cls.__instance



class CustomLogisticRegression:
    """Реализация логистической регрессии"""

    def __init__(self, max_iter=100, learning_step=0.1,  epsilon=0.001,  treshold=0.5):
        self.max_iter = max_iter
        self.learning_step = learning_step
        self.epsilon = epsilon
        self.treshold = treshold
 
        self.current_weights = None  # Здесь сохраняются итоговые веса
        self.__initial_weights = None
        self.__next_weights = None

        
    def predict_proba(self, X: np.array):
        z = (X @ self.current_weights)
        return 1 / (1 + np.exp(-z))
        

    def predict(self, X: np.array):
        probabilities = self.predict_proba(X)
        return np.where(probabilities > 0.5, 1, 0)


    def fit(self, X_train: np.array, y_train: np.array):

        n_objects = X_train.shape[0]
        n_features = X_train.shape[1]
        self.__initial_weights = np.random.randn(n_features)

        self.__next_weights = self.__initial_weights        
        for iter in range(self.max_iter):
            self.current_weights = self.__next_weights
            # Вычисляем predict_proba
            y_pred_pr = self.predict_proba(X_train)
            # Вычисляем Logloss
            logloss = - (1 / n_objects) * np.sum(y_train * np.log(y_pred_pr) + (1 - y_train) * np.log(1 - y_pred_pr))
            # Вычисляем prdict
            y_pred = self.predict(X_train) 
            # Вычисляем вектор-градиент
            gradients = X_train.T @ (y_train - y_pred)
            # Обновляем веса
            self.__next_weights = self.current_weights - self.learning_step * gradients

            print(f"Итерация: {iter}")
            print(f"Текущая точка {self.current_weights} | Следующая точка {self.__next_weights}")
            print(f"Logloss {logloss}")
            print("--------------------------------------------------------")

            # Останавилваем обучение когда веса не меняются
            difference_weights_norm = np.linalg.norm(self.__next_weights  - self.current_weights, ord=2)  
            if difference_weights_norm <= self.epsilon: 
                break
        
        print(f'Найденные веса, обеспечивающие минимум функции потерь (Logloss): {self.current_weights}')

        

    def score(self, X_test: np.array, y_test: np.array):
        y_pred = self.predict(X_test)
        return accuracy_score(y_test, y_pred)
    
lr = CustomLogisticRegression()
lr.fit(X_train, y_train)
